from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
app = FastAPI(title="Twitter Sentiment Analysis API")
try:
    classifier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
except Exception as e:
    print(f"Lỗi khi tải mô hình: {e}")

class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {
        "name": "Twitter Sentiment Analysis API",
        "description": "API này sử dụng mô hình Twitter RoBERTa để phân tích cảm xúc văn bản (Tích cực, Tiêu cực, Trung tính).",
        "model_used": "cardiffnlp/twitter-roberta-base-sentiment-latest"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok", 
        "message": "Hệ thống đang hoạt động bình thường."
    }

@app.post("/predict")
def predict_sentiment(input_data: TextInput):
    if not input_data.text or not input_data.text.strip():
        raise HTTPException(status_code=400, detail="Văn bản đầu vào không được để trống.")
    try:
        result = classifier(input_data.text)
        return {
            "input_text": input_data.text,
            "prediction": result[0]['label'],
            "confidence_score": round(result[0]['score'], 4)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi suy luận mô hình: {str(e)}")

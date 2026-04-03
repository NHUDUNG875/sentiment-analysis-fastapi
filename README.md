
https://github.com/user-attachments/assets/15198601-3b21-4f0b-9aa2-5b95f3b112da
# [LAB 1] - APPLICATION PROGRAMMING INTERFACE 

## 1. Thông tin sinh viên 
* **Họ và tên:** Nguyễn Hoàng Như Dung
* **Mã số sinh viên:** 24120175
* **Giảng viên thực hành:** Lê Đức Khoan 

## 2. Thông tin mô hình 
* **Tên mô hình:** `cardiffnlp/twitter-roberta-base-sentiment-latest`
* **Liên kết Hugging Face:** [Twitter RoBERTa Sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest)

## 3. Mô tả chức năng hệ thống 
Hệ thống sử dụng FastAPI để xây dựng Web API phân tích cảm xúc từ văn bản tiếng Anh. Mô hình sẽ phân loại dữ liệu đầu vào thành các nhãn: Positive (Tích cực), Negative (Tiêu cực), hoặc Neutral (Trung tính).

## 4. Hướng dẫn cài đặt thư viện 
Chạy lệnh sau để cài đặt các thư viện trong file `requirements.txt`:
```bash
pip install -r requirements.txt
```
## 5. Hướng dẫn chạy chương trình 
Bước 1: Khởi động Server API 
Mở terminal và chạy lệnh sau để bật hệ thống:
```bash
python -m uvicorn main:app --reload
```
Hệ thống sẽ chạy tại địa chỉ: http://127.0.0.1:8000. 


Bước 2: Kiểm thử API 


Mở một terminal mới (trong khi server vẫn đang chạy) và thực hiện lệnh để kiểm tra các chức năng:
```bash
python test_api.py
```

## 6. Ví dụ Request và Response 
Dưới đây là kết quả mẫu khi gọi API POST /predict:

**Request:**
```bash
{
    "text": "I absolutely love the new design! It's so beautiful"
}
```

**Response:**
```bash
{
    "input_text": "I absolutely love the new design! It's so beautiful", 
    "prediction": "positive", 
    "confidence_score": 0.9856
}
```

## 7. Liên kết video demo:

https://github.com/user-attachments/assets/9e718f81-6554-4bf4-a1d2-5c56dde6f534



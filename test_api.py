import requests
url = "http://127.0.0.1:8000/predict"
test_cases = [
    {"name": "Test 1 (Positive)", "data": {"text": "I absolutely love the new design! It's so beautiful"}},
    {"name": "Test 2 (Negative)", "data": {"text": "The customer service was terrible. I am very disappointed."}},
    {"name": "Test 3 (Lỗi rỗng)", "data": {"text": "   "}} 
]

print("--- Kiểm tra thử API phân tích cảm xúc ---")

for case in test_cases:
    print(f"\nĐang chạy: {case['name']}")
    print(f"Dữ liệu gửi đi: {case['data']}")
    response = requests.post(url, json=case['data'])
    
    if response.status_code == 200:
        print("Kết quả JSON trả về:")
        print(response.json())
    else:
        print(f"Báo lỗi từ Server (Status {response.status_code}):")
        print(response.json())

# do Mô hình này chỉ đang kiểm tra tiếng anh nên khi dùng tiếng việt để kiểm tra sẽ cho ra kết quả Trung Tính 
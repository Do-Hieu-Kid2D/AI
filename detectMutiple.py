import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import cv2
import numpy as np
from keras.models import load_model

# Load mô hình đã huấn luyện
model = load_model('litterTrain.keras')

# Đường dẫn đến thư mục chứa các ảnh cần dự đoán
folder_path = 'images/test/8'

# Tạo một danh sách để lưu kết quả dự đoán của mỗi ảnh
predictions_list = []

# Duyệt qua từng tệp ảnh trong thư mục
i = 1
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Kiểm tra tệp có phải là ảnh
        image_path = os.path.join(folder_path, filename)
        # Đọc hình ảnh
        image = cv2.imread(image_path)
        # Tiền xử lý hình ảnh
        image = cv2.resize(image, (20, 20))  # Resize hình ảnh về kích thước 20x20
        image = image.astype('float32') / 255  # Chuẩn hóa giá trị pixel về khoảng 0-1
        # Thêm một chiều mới cho hình ảnh để phù hợp với đầu vào của mô hình
        image = np.expand_dims(image, axis=0)
        # Dự đoán số trên hình ảnh
        predictions = model.predict(image)
        # Lấy số có xác suất cao nhất
        predicted_number = np.argmax(predictions)
        # Tên tệp ảnh
        print(f"===> Lần {i}: image:", filename)
        i += 1
        # Kết quả dự đoán và xác suất
        print("Dự đoán:", predicted_number)
        print("Xác suất:", predictions[0][predicted_number] * 100, "%")
        print("--------------------------------")
        # Lưu kết quả dự đoán vào danh sách
        predictions_list.append((filename, predicted_number, predictions[0][predicted_number] * 100))

# Tính toán và in ra bảng tổng kết dự đoán
print("Bảng tổng kết dự đoán:")
print("Số\tSố lần dự đoán\tTỉ lệ (%)")
predictions_count = {}
total_predictions = len(predictions_list)

for _, predicted_number, _ in predictions_list:
    if predicted_number in predictions_count:
        predictions_count[predicted_number] += 1
    else:
        predictions_count[predicted_number] = 1

for number, count in predictions_count.items():
    percentage = (count / total_predictions) * 100
    print(f" {number}\t\t{count}\t\t\t {percentage:.2f}")


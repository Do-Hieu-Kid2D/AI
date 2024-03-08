import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import cv2
import numpy as np
from keras.models import load_model

# Load mô hình đã huấn luyện
model = load_model("litterTrain.keras")

# Đọc hình ảnh mới cần dự đoán

image = cv2.imread('myMake/so3.jpg')


# print(image)
# cv2.imshow("One image",image)
# cv2.waitKey(0)

# Tiền xử lý hình ảnh
image = cv2.resize(image, (20, 20))  # Resize hình ảnh về kích thước 20x20
image = image.astype('float32') / 255  # Chuẩn hóa giá trị pixel về khoảng 0-1

# Thêm một chiều mới cho hình ảnh để phù hợp với đầu vào của mô hình
image = np.expand_dims(image, axis=0)

# Dự đoán số trên hình ảnh mới
predictions = model.predict(image)

# Lấy số có xác suất cao nhất
predicted_number = np.argmax(predictions)

print("Số được dự đoán:", predicted_number)

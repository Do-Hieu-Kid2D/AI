import cv2
import os

# Tạo thư mục 'images' nếu nó không tồn tại
if not os.path.exists('images'):
    os.makedirs('images')

# Tạo thư mục 'train' trong 'images' nếu nó không tồn tại
train_dir = 'images/train'
if not os.path.exists(train_dir):
    os.makedirs(train_dir)

# Tạo thư mục cho mỗi số từ 0 đến 9 trong thư mục 'train'
for i in range(10):
    digit_dir = os.path.join(train_dir, str(i))
    if not os.path.exists(digit_dir):
        os.makedirs(digit_dir)

# Tạo thư mục 'test' trong 'images' nếu nó không tồn tại
test_dir = 'images/test'
if not os.path.exists(test_dir):
    os.makedirs(test_dir)

# Tạo thư mục cho mỗi số từ 0 đến 9 trong thư mục 'test'
for i in range(10):
    digit_dir = os.path.join(test_dir, str(i))
    if not os.path.exists(digit_dir):
        os.makedirs(digit_dir)

# Đọc ảnh
image = cv2.imread('digits.png')

# Chiều rộng và chiều cao của mỗi số
number_width = 20
number_height = 20

# Số hàng và số cột
rows = 50
columns = 50

# Biến đếm cho số ảnh đã cắt
count = 0

# Cắt ảnh và lưu vào các thư mục tương ứng
for i in range(rows):
    for j in range(columns):
        if i<5:
            if j < 40:
                cv2.imwrite(f'images/train/0/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
            else:
                # Lưu vào thư mục 'test' cho các số còn lại
                cv2.imwrite(f'images/test/0/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
        if 5 <= i <10:
            if j < 40:
                cv2.imwrite(f'images/train/1/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
            else:
                # Lưu vào thư mục 'test' cho các số còn lại
                cv2.imwrite(f'images/test/1/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
        if 10 <= i < 15:
            if j < 40:
                cv2.imwrite(f'images/train/2/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
            else:
                # Lưu vào thư mục 'test' cho các số còn lại
                cv2.imwrite(f'images/test/2/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
        if 15 <= i < 20:
            if j < 40:
                cv2.imwrite(f'images/train/3/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
            else:
                # Lưu vào thư mục 'test' cho các số còn lại
                cv2.imwrite(f'images/test/3/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
        if 20 <= i < 25:
            if j < 40:
                cv2.imwrite(f'images/train/4/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
            else:
                # Lưu vào thư mục 'test' cho các số còn lại
                cv2.imwrite(f'images/test/4/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
        if 25 <= i < 30:
            if j < 40:
                cv2.imwrite(f'images/train/5/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
            else:
                # Lưu vào thư mục 'test' cho các số còn lại
                cv2.imwrite(f'images/test/5/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
        if 30 <= i < 35:
            if j < 40:
                cv2.imwrite(f'images/train/6/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
            else:
                # Lưu vào thư mục 'test' cho các số còn lại
                cv2.imwrite(f'images/test/6/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
        if 35 <= i < 40:
            if j < 40:
                cv2.imwrite(f'images/train/7/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
            else:
                # Lưu vào thư mục 'test' cho các số còn lại
                cv2.imwrite(f'images/test/7/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
        if 40 <= i < 45:
            if j < 40:
                cv2.imwrite(f'images/train/8/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
            else:
                # Lưu vào thư mục 'test' cho các số còn lại
                cv2.imwrite(f'images/test/8/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
        if 45 <= i < 50:
            if j < 40:
                cv2.imwrite(f'images/train/9/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
            else:
                # Lưu vào thư mục 'test' cho các số còn lại
                cv2.imwrite(f'images/test/9/{count}.jpg', image[i*number_height:(i+1)*number_height, j*number_width:(j+1)*number_width])
        count += 1

print("Đã cắt và lưu các số thành công: ", count)

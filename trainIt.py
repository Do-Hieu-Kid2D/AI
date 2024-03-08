import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Khởi tạo mô hình CNN
model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(20, 20, 3)))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Flatten())

model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))  # 10 lớp đầu ra cho các số từ 0 đến 9

# Compile mô hình
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Tạo các đối tượng ImageDataGenerator để tăng cường dữ liệu huấn luyện
train_datagen = ImageDataGenerator(rescale=1./255)  # Tái tổ chức lại giá trị pixel về khoảng 0-1

# Tính toán tổng số lượng ảnh
total_images_per_class = 200  # Số lượng ảnh cho mỗi lớp
num_classes = 10  # Số lượng lớp
total_images = total_images_per_class * num_classes  # Tổng số lượng ảnh

# Sử dụng công thức để tính số lượng batch cần phải tạo ra trong mỗi epoch
batch_size = 32  # Kích thước mỗi batch
steps_per_epoch = total_images // batch_size  # Số lượng batch cần phải tạo ra

print("steps_per_epoch: " , steps_per_epoch)

# Load dữ liệu huấn luyện từ các thư mục
train_generator = train_datagen.flow_from_directory(
    'images/train',
    target_size=(20, 20),
    batch_size=batch_size,
    class_mode='categorical')

# Huấn luyện mô hình với số lượng batch tính toán được
# model.fit_generator(
#     train_generator,
#     steps_per_epoch=steps_per_epoch,  # Số lượng batch cần phải tạo ra
#     epochs=10)  # Số lần lặp lại huấn luyện

# Huấn luyện mô hình với số lượng batch tính toán được
history = model.fit(
    train_generator,
    steps_per_epoch=steps_per_epoch,  # Số lượng batch cần phải tạo ra
    epochs=10)  # Số lần lặp lại huấn luyện

# Lấy thông tin loss và accuracy từ history
loss = history.history['loss']
accuracy = history.history['accuracy']

# Vẽ biểu đồ loss và accuracy trên cùng một đồ thị với màu tùy chỉnh
plt.plot(loss, label='Loss', color='#ff3300')  # Đường loss sẽ được vẽ màu đỏ
plt.plot(accuracy, label='Accuracy', color='#00b300')  # Đường accuracy sẽ được vẽ màu xanh
plt.title('Training Loss and Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Rate')
plt.legend()

# Chỉ định số lượng điểm trên trục hoành và nhãn tương ứng
epochs = range(10)  # Từ epoch 0 đến epoch 9
plt.xticks(epochs, [str(i+1) for i in epochs])  # Gán nhãn từ 1 đến 10 cho các epoch

plt.show()

# Lưu mô hình đã huấn luyện
model.save('litterTrain.keras')

print("Đã lưu: litterTrain.keras")
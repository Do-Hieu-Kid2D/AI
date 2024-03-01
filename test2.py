from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import LambdaCallback

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

# Tạo các đối tượng ImageDataGenerator để tăng cường dữ liệu huấn luyện ==> (nếu cần)
train_datagen = ImageDataGenerator(rescale=1./255)  # Tái tổ chức lại giá trị pixel về khoảng 0-1

# Load dữ liệu huấn luyện từ các thư mục
train_generator = train_datagen.flow_from_directory(
    'images/train',
    target_size=(20, 20),
    batch_size=32,
    class_mode='categorical')

# Huấn luyện mô hình
model.fit_generator(
    train_generator,
    steps_per_epoch=200,  # Số bước mỗi epoch (200 ảnh/số * 10 số)
    epochs=10)  # Số lần lặp lại huấn luyện

# Lưu mô hình đã huấn luyện
model.save('number_recognition_model.h5')

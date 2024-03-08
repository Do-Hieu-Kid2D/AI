import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from keras.models import load_model
from PIL import Image, ImageTk

# Load mô hình đã huấn luyện
model = load_model("litterTrain.keras")


def predict_number():
    # Chọn ảnh từ hộp thoại mở tệp
    file_path = filedialog.askopenfilename()

    # Đọc ảnh
    image = cv2.imread(file_path)

    # Tiền xử lý hình ảnh
    image = cv2.resize(image, (20, 20))  # Thay đổi kích thước ảnh thành 20x20
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Chuyển đổi màu từ BGR sang RGB (PIL sử dụng RGB)

    # Dự đoán số trên hình ảnh
    predictions = model.predict(image[np.newaxis, :, :, :])
    predicted_number = np.argmax(predictions)

    # Tạo một ảnh mới với kích thước lớn hơn để hiển thị
    large_image = cv2.resize(image, (150, 150))

    # Hiển thị ảnh và kết quả dự đoán
    img = Image.fromarray(large_image)
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image = img
    result_label.configure(text="Số được dự đoán: " + str(predicted_number))


# Tạo giao diện
root = tk.Tk()
root.title("Dự đoán số từ ảnh litterTrain")
root.geometry("360x300")  # Đặt kích thước của cửa sổ là 400x400

# Đặt cửa sổ ở giữa màn hình
# Đặt cửa sổ ở giữa màn hình dựa trên góc trái của cửa sổ
window_width = root.winfo_width()
window_height = root.winfo_height()
position_right = int((root.winfo_screenwidth() - window_width) / 2)
position_down = int((root.winfo_screenheight() - window_height) / 2)
root.geometry("+{}+{}".format(position_right, position_down))


btn = tk.Button(root, text="Chọn ảnh", command=predict_number)
btn.pack()

panel = tk.Label(root)  # Không cần thiết lập kích thước ở đây
panel.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()

import pygame
import os

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 200, 200

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Khung
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
pygame.display.set_caption("Vẽ 20x20")

# Danh sách các điểm vẽ
draw_points = []

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Bắt đầu vẽ khi chuột được nhấn
            draw_points.append(event.pos)
        elif event.type == pygame.MOUSEMOTION:
            # Nếu chuột di chuyển, thêm các điểm vẽ mới
            if event.buttons[0]:  # Kiểm tra nút chuột trái có được nhấn không
                draw_points.append(event.pos)
        elif event.type == pygame.KEYDOWN:
            # Nếu người dùng ấn phím 's', lưu hình ảnh
            if event.key == pygame.K_s:
                pygame.image.save(screen, os.path.join(os.getcwd(), "drawn_image.png"))
                print("Đã lưu hình ảnh.")
            # Nếu người dùng ấn phím 'r', xóa màn hình
            elif event.key == pygame.K_r:
                screen.fill(BLACK)
                draw_points = []

    # Vẽ các điểm được lưu trữ
    if len(draw_points) > 1:
        pygame.draw.lines(screen, WHITE, False, draw_points, 5)

    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc Pygame
pygame.quit()

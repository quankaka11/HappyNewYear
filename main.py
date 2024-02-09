import pygame
import sys
from Phao import *
from CountDown import *

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Window")
#Thêm âm thanh
music = pygame.mixer.music.load("intro.ogg")
pygame.mixer.music.play(-1)

# Hàm vẽ màn hình chính
def draw_main_screen():
    screen.fill((255, 255, 255))  # Màu nền trắng
    # Vẽ hình ảnh
    image = pygame.image.load('tet.jpg')
    image = pygame.transform.scale(image, (width, height))
    screen.blit(image, (0, 0))
    # Vẽ nút CountDown
    pygame.draw.rect(screen, (255, 255, 0), (width // 2 - 75, height * 0.9, 150, 50))  # Màu và kích thước nút
    font = pygame.font.Font(None, 36)  # Cỡ chữ
    text = font.render('CountDown', True, (0, 0, 0))  # Màu chữ đen
    screen.blit(text, (width // 2 - 70, height * 0.92))  # Vị trí chữ
    

# Vòng lặp chính của Pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Kiểm tra xem có nhấn vào nút CountDown không
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if width // 2 - 75 < mouse_x < width // 2 + 75 and height * 0.9 < mouse_y < height * 0.9 + 50:
                #Dừng âm thanh
                pygame.mixer.music.stop()
                # Thực hiện hành động khi nhấn nút CountDown
                countDown()
                #Bắn pháo hoa
                start()
    
    draw_main_screen()
    pygame.display.flip()

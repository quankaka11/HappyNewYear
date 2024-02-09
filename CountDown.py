import pygame
import sys

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

#Tạo hàm đến ngược countDown
def countDown():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
     
    #thêm âm thanh 
    music = pygame.mixer.music.load("Count_Down.ogg")
    pygame.mixer.music.play()
    
    #them chu
    font = pygame.font.Font(None, 50)  # Cỡ chữ
    den_led = font.render('HAPPY NEW YEAR', True, (255, 50, 55))  # 
    denX = 750
    denY = 100

    font = pygame.font.Font(None, 50)  # Cỡ chữ
    den_led2 = font.render('AN KHANG THINH VUONG', True, (255, 50, 55))  # 
    dX = 50
    dY = 550

    pygame.display.set_caption("CountDown")
    font = pygame.font.Font(None, 100)
    #Tạo biến đếm ngược
    time = 10
    dem = 1000
    
    while True:
        
        a,b,c = 255, 255, 255
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if time % 3 == 1:
            a -= 70
            b = 0
            c -= 100
        elif time % 3 == 0:
            b = 255
            a = 0
            c -= 50
        else:
            c = 255
            a = 150
            b = 100 
        #Tạo màn hình đếm ngược
        screen.fill((0, 0, 0))
        #hinh anh
        image = pygame.image.load("Lock.jpg")
        image = pygame.transform.scale(image,(800,600))
        screen.blit(image,(0,0))

        text = font.render(str(time), True, (a, b, c))
        screen.blit(text, (375, 275))
        
        screen.blit(den_led, (denX, denY))
        denX -= 10

        screen.blit(den_led2, (dX, dY))
        dX += 5

        pygame.display.flip()
        pygame.time.wait(100)
        dem -= 100
        if dem == 0:
            dem = 1000
        if dem == 1000:
            time -= 1
        if time == 0:
            break
        
    #Thêm âm thanh đếm ngược
    # music = pygame.mixer.music.load("intro.ogg")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.stop()
if __name__ == "__main__":
    countDown()
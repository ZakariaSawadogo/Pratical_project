import pygame
import sys
import subprocess

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Learn")

FONT = pygame.font.SysFont("arial", 64)
SMALL_FONT = pygame.font.SysFont("arial", 32)
TITLE_FONT = pygame.font.SysFont("arial", 48, italic=True, bold=True)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

pygame.mixer.music.load("sounds/home_music.wav")
pygame.mixer.music.play(-1)

class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, win):
        pygame.draw.rect(win, WHITE, self.rect, 2)
        txt = SMALL_FONT.render(self.text, True, WHITE)
        win.blit(txt, (self.rect.x + (self.rect.width - txt.get_width()) // 2,
                       self.rect.y + (self.rect.height - txt.get_height()) // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def main_menu():
    while True:
        WIN.fill(BLACK)
        title = TITLE_FONT.render("Typing Learn", True, WHITE)
        WIN.blit(title, ((WIDTH - title.get_width()) // 2, 40))

        btn1 = Button("Falling Word", 300, 150, 200, 50)
        btn2 = Button("Falling Letter", 300, 230, 200, 50)
        btn3 = Button("Exit", 300, 310, 200, 50)

        btn1.draw(WIN)
        btn2.draw(WIN)
        btn3.draw(WIN)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if btn1.is_clicked(pos):
                    pygame.mixer.music.stop()
                    subprocess.run([sys.executable, "Falling_word.py"])
                    pygame.mixer.music.play(-1)
                elif btn2.is_clicked(pos):
                    pygame.mixer.music.stop()
                    subprocess.run([sys.executable, "Falling_letter.py"])
                    pygame.mixer.music.play(-1)
                elif btn3.is_clicked(pos):
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main_menu()

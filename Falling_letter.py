import pygame
import random
import sys
import subprocess


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("sounds/home_music.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Letter")

FONT = pygame.font.SysFont("arial", 64)
SMALL_FONT = pygame.font.SysFont("arial", 32)
TITLE_FONT = pygame.font.SysFont("arial", 48, italic=True, bold=True)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)

clock = pygame.time.Clock()

sounds = {
    "keypress": pygame.mixer.Sound("sounds/keyboard_key.wav"),
    "correct": pygame.mixer.Sound("sounds/correct_word.wav"),
    "incorrect": pygame.mixer.Sound("sounds/incorrect_word.wav"),
    "lose_heart": pygame.mixer.Sound("sounds/heart_lose.wav"),
    "gain_heart": pygame.mixer.Sound("sounds/healing.wav"),
    "game_over": pygame.mixer.Sound("sounds/game_over.wav"),
}

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

class FallingLetter:
    def __init__(self):
        self.reset()

    def reset(self):
        self.letter = chr(random.randint(ord('A'), ord('Z')))
        self.x = random.randint(50, WIDTH - 50)
        self.y = -50
        self.speed = 2

    def update(self):
        self.y += self.speed

    def draw(self, win):
        text = FONT.render(self.letter, True, WHITE)
        win.blit(text, (self.x, self.y))

def draw_hearts(win, hp):
    for i in range(hp):
        heart = SMALL_FONT.render("\u2665", True, RED)
        win.blit(heart, (10 + i * 30, 10))

def game_loop():
    letter = FallingLetter()
    run = True
    hp = 5
    score = 0
    missed = 0
    level = 1

    while run:
        clock.tick(60)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                sounds["keypress"].play()
                key = pygame.key.name(event.key).upper()
                if key == letter.letter:
                    score += 1
                    letter.reset()
                    missed = 0
                    #sounds["correct"].play()
                    if score % 5 == 0:
                        level += 1
                        letter.speed += 0.5
                        if hp < 5:
                            hp += 1
                            sounds["gain_heart"].play()
                else:
                    missed += 1
                    sounds["incorrect"].play()

        letter.update()

        if letter.y > HEIGHT:
            missed += 1
            letter.reset()

        if missed >= 2:
            hp -= 1
            missed = 0
            sounds["lose_heart"].play()

        if hp <= 0:
            sounds["game_over"].play()
            game_over_screen(score, level)
            return

        letter.draw(WIN)
        draw_hearts(WIN, hp)

        score_text = SMALL_FONT.render(f"Score: {score}", True, WHITE)
        level_text = SMALL_FONT.render(f"Niveau: {level}", True, WHITE)
        WIN.blit(score_text, (WIDTH - 200, 10))
        WIN.blit(level_text, (WIDTH - 200, 40))

        pygame.display.update()

def game_main_menu():
    while True:
        WIN.fill(BLACK)
        title = TITLE_FONT.render("Falling Letter", True, WHITE)
        WIN.blit(title, ((WIDTH - title.get_width()) // 2, 40))

        btn_play = Button("Play", 300, 180, 200, 50)
        btn_home = Button("Home", 300, 260, 200, 50)
        btn_exit = Button("Exit", 300, 340, 200, 50)

        btn_play.draw(WIN)
        btn_home.draw(WIN)
        btn_exit.draw(WIN)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if btn_play.is_clicked(pos):
                    game_loop()
                elif btn_home.is_clicked(pos):
                    pygame.mixer.music.stop()
                    subprocess.run([sys.executable, "principal.py"])
                    pygame.quit()
                    sys.exit()
                elif btn_exit.is_clicked(pos):
                    pygame.quit()
                    sys.exit()


def game_over_screen(score, level):
    run = True
    sounds["game_over"].play()
    while run:
        WIN.fill(BLACK)
        game_over_text = FONT.render("GAME OVER", True, RED)
        score_text = SMALL_FONT.render(f"Score: {score}", True, WHITE)
        level_text = SMALL_FONT.render(f"Level Reached: {level}", True, WHITE)
        restart_text = SMALL_FONT.render("Press R to restart", True, WHITE)
        quit_text = SMALL_FONT.render("Press Q to quit", True, WHITE)

        texts = [game_over_text, score_text, level_text, restart_text, quit_text]
        for i, t in enumerate(texts):
            rect = t.get_rect(center=(WIDTH // 2, 200 + i * 50))
            WIN.blit(t, rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_loop()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    game_main_menu()

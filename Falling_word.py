
import pygame
import random
import pygame
import sys
import os
import subprocess





pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("sounds/home_music.wav")
pygame.mixer.music.set_volume(0.5)   # volume facultatif
pygame.mixer.music.play(-1)          # -1 = boucle infinie
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Typer")

WORD_FONT = pygame.font.SysFont("arial", 36)
SMALL_FONT = pygame.font.SysFont("arial", 32)
INFO_FONT = pygame.font.SysFont("arial", 24)
TITLE_FONT = pygame.font.SysFont("arial", 40, italic=True, bold=True)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

clock = pygame.time.Clock()

LANGUAGES = [
    ("English", "English", "flags/english.png"),
    ("Français", "French", "flags/french.png"),
    ("Español", "Spanish", "flags/spanish.png"),
    ("Türkçe", "Türkçe", "flags/turkish.png"),
    ("Kurdish", "Kurdish", "flags/kurdish.png"),
    ("Deutsch", "German", "flags/german.png")
]

correct_sound = pygame.mixer.Sound("sounds/correct_word.wav")
incorrect_sound = pygame.mixer.Sound("sounds/incorrect_word.wav")
lose_heart_sound = pygame.mixer.Sound("sounds/heart_lose.wav")
gain_heart_sound = pygame.mixer.Sound("sounds/healing.wav")
game_over_sound = pygame.mixer.Sound("sounds/game_over.wav")
key_sound = pygame.mixer.Sound("sounds/keyboard_key.wav")

def load_words(lang_code):
    try:
        with open(f"words/{lang_code}.txt", "r", encoding="utf-8") as f:
            return [line.strip().upper() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Erreur : fichier words/{lang_code}.txt introuvable.")
        pygame.quit()
        sys.exit()

def draw_button(rect, text, flag_path=None):
    pygame.draw.rect(WIN, GRAY, rect)
    pygame.draw.rect(WIN, WHITE, rect, 2)
    if flag_path:
        flag = pygame.image.load(flag_path)
        flag = pygame.transform.scale(flag, (40, 30))
        WIN.blit(flag, (rect.x + 10, rect.y + 10))
        label = SMALL_FONT.render(text, True, WHITE)
        WIN.blit(label, (rect.x + 60, rect.y + 15))
    else:
        label = SMALL_FONT.render(text, True, WHITE)
        WIN.blit(label, (rect.centerx - label.get_width() // 2, rect.centery - label.get_height() // 2))

def language_menu():
    selected_lang = None
    buttons = []
    gap_x, gap_y = 50, 30
    btn_width, btn_height = 300, 60

    positions = [
        (100, 150), (400, 150),
        (100, 230), (400, 230),
        (100, 310), (400, 310),
        (100, 400), (400, 400)
    ]

    for i, pos in enumerate(positions):
        if i < 6:
            lang = LANGUAGES[i]
            buttons.append((pygame.Rect(pos[0], pos[1], btn_width, btn_height), lang[0], lang[1], lang[2]))
        elif i == 6:
            buttons.append((pygame.Rect(pos[0], pos[1], btn_width, btn_height), "Home", None, None))
        else:
            buttons.append((pygame.Rect(pos[0], pos[1], btn_width, btn_height), "Exit", None, None))

    while True:
        WIN.fill(BLACK)
        title = TITLE_FONT.render("Typing Learn", True, WHITE)
        WIN.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        for btn in buttons:
            draw_button(btn[0], btn[1], btn[3])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons:
                    if btn[0].collidepoint(event.pos):
                        if btn[1] == "Exit":
                            pygame.quit()
                            sys.exit()
                        elif btn[1] == "Home":
                            pygame.mixer.music.stop()
                            subprocess.run(["python", "principal.py"])
                            pygame.quit()
                            sys.exit()
                        else:
                            return btn[2]  # retourne le code langue


class FallingWord:
    def __init__(self, word_list):
        self.word_list = word_list
        self.reset()
        self.color = WHITE
        self.color_change_speed = 5
        self.color_direction = 1

    def reset(self):
        self.word = random.choice(self.word_list)
        self.x = random.randint(50, WIDTH - 200)
        self.y = -50
        self.speed = 1.2

    def update(self):
        self.y += self.speed
        r, g, b = self.color
        g += self.color_direction * self.color_change_speed
        if g >= 255:
            g = 255
            self.color_direction = -1
        elif g <= 100:
            g = 100
            self.color_direction = 1
        self.color = (r, g, b)

    def draw(self, win):
        text = WORD_FONT.render(self.word, True, self.color)
        win.blit(text, (self.x, self.y))


def draw_hearts(win, hp):
    for i in range(hp):
        heart = SMALL_FONT.render("♥", True, RED)
        win.blit(heart, (10 + i * 30, 10))


def main():
    lang_code = language_menu()
    WORD_LIST = load_words(lang_code)
    word = FallingWord(WORD_LIST)

    run = True
    hp = 5
    score = 0
    consecutive_correct = 0
    typing = ""
    level = 1
    message = ""
    message_timer = 0
    message_color = GREEN

    while run:
        clock.tick(60)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                key_sound.play()
                if event.key == pygame.K_BACKSPACE:
                    typing = typing[:-1]
                elif event.key == pygame.K_RETURN:
                    if typing.upper() == word.word:
                        score += 1
                        consecutive_correct += 1
                        message = "Doğru!"
                        message_timer = 60
                        message_color = GREEN
                        correct_sound.play()

                        if consecutive_correct >= 3:
                            hp += 1
                            consecutive_correct = 0
                            message = "Can kazandın!"
                            message_timer = 120
                            message_color = BLUE
                            gain_heart_sound.play()

                        if score % 5 == 0:
                            level += 1
                            word.speed += 0.2
                            message = f"Seviye {level}!"
                            message_timer = 90
                            message_color = YELLOW

                        word.reset()
                    else:
                        consecutive_correct = 0
                        message = "Hatalı!"
                        message_timer = 60
                        message_color = RED
                        incorrect_sound.play()

                    typing = ""
                elif event.unicode.isprintable():
                    typing += event.unicode

        word.update()

        if word.y > HEIGHT:
            consecutive_correct = 0
            hp -= 1
            message = "Kaçırdın!"
            message_timer = 60
            message_color = RED
            word.reset()
            incorrect_sound.play()

        if hp <= 0:
            run = False

        word.draw(WIN)
        draw_hearts(WIN, hp)

        typing_text = INFO_FONT.render(f">> {typing}", True, WHITE)
        WIN.blit(typing_text, (20, HEIGHT - 50))

        score_text = SMALL_FONT.render(f"Puan: {score}", True, WHITE)
        level_text = SMALL_FONT.render(f"Seviye: {level}", True, WHITE)
        streak_text = SMALL_FONT.render(f"Seri: {consecutive_correct}/3", True, WHITE)
        WIN.blit(score_text, (WIDTH - 200, 10))
        WIN.blit(level_text, (WIDTH - 200, 40))
        WIN.blit(streak_text, (WIDTH - 200, 70))

        if message_timer > 0:
            message_timer -= 1
            message_text = SMALL_FONT.render(message, True, message_color)
            message_rect = message_text.get_rect(center=(WIDTH // 2, 100))
            WIN.blit(message_text, message_rect)

        pygame.display.update()

    game_over_screen(score, level)


def game_over_screen(score, level):
    run = True
    pygame.mixer.music.stop()
    game_over_sound.play()
    while run:
        WIN.fill(BLACK)
        game_over_text = WORD_FONT.render("OYUN BİTTİ", True, RED)
        score_text = SMALL_FONT.render(f"Toplam Puan: {score}", True, WHITE)
        level_text = SMALL_FONT.render(f"Ulaşılan Seviye: {level}", True, WHITE)
        restart_text = SMALL_FONT.render("Yeniden başlamak için R'ye basın", True, WHITE)
        quit_text = SMALL_FONT.render("Çıkmak için Q'ya basın", True, WHITE)

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pygame.mixer.music.load("sounds/home_music.wav")
                    pygame.mixer.music.play(-1)
                    main()
                if event.key == pygame.K_q:
                    run = False
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()

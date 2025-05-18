# 🎮 Typing Learn

**Typing Learn**, **Python ve Pygame** ile geliştirilmiş, kullanıcılara klavyede hızlarını ve hassasiyetlerini artırmada yardımcı olan ve aynı zamanda eğlendiren bir eğitim oyunudur.

## 👨‍💻 Ekip Bilgisi

- **Zakaria SAWADOGO** – [github.com/ZakariaSawadogo](https://github.com/ZakariaSawadogo)
- **Manar Ahmad SALEM** – [github.com/ManarSalem99](https://github.com/ManarSalem99)

## 📁 Projenin Yapısı
Pratical_Project/
│
├── main.py
├── Falling_word.py
├── Falling_letter.py
│
├── words/
│ ├── English.txt
│ ├── French.txt
│ ├── Spanish.txt
│ ├── German.txt
│ ├── Kurdish
│ └── Turkish.txt
│
├── sounds/
│ ├── home_music.wav
│ ├── correct_word.wav
│ ├── incorrect_word.wav
│ ├── game_over.wav
│ ├── healing.wav
│ ├── heart_lose.wav
│ └── keyboard_key
│
├── flags/
│ ├── english.png
│ ├── french.png
│ ├── exit.png
│ ├── german.png
│ ├── kurdish.png
│ ├── spanish.png
│ ├── arabic.png
│ ├── home.png
│ └── turkish.png
│
└── README.md


## 🎮 Oynanış

### 1. Ana menu

<img src=“Screenshots/Main_menu.png” width=“600”>

- Düşen Kelime**: Düşen kelimeler, oyuncu onları ekranın altına ulaşmadan önce yazmalıdır.
- Düşen Harf**: Düşen harfler, oyuncu onları ekranın altına ulaşmadan önce yazmalıdır.
- Çıkış**: Oyundan çıkın.


### 2. Falling word

<img src=“Screenshots/Falling_word_gameplay.png” width=“600”>

- Puan kazanmak için düşen kelimeleri yazın.
- Art arda 3 doğru cevaptan sonra kalp kazanın.
- Bir kelime yere düşerse veya cevap yanlışsa kalp kaybedin.
- Zorluk her 5 doğru kelimede bir artar.

<img src=“Screenshots/Falling_word_languageChoice.png” width=“600”>

Oyuncu kelimelerin dilini seçebilir:
- 🇬🇧 İngilizce
- 🇫🇷 Fransızca
- 🇹🇷 Türkçe
- 🇪🇸 İspanyolca
- 🇩🇪 Almanca
- 🇹🇯 Kürtçe

### 3 Falling letter

<img src="Screenshots/Falling_letter_gameplay.png“ width=”600">

- Puan kazanmak için düşen harfleri yazın.
- Art arda 5 doğru cevaptan sonra kalp kazanın.
- Art arda 2 harf yere düşerse veya 2 cevap yanlışsa kalpleri kaybedin.
- Zorluk her 5 doğru harfte bir artar (düşme hızı ve düşen harf sayısı artar).

### 4. Game over

<img src=“Screenshots/game_over.png” width=“600”>

Skor ve ulaşılan seviyenin görüntülenmesi.

## 🛠️ Kullanılan teknolojiler

- Python 3.10+**
- Pygame
- Git & GitHub**

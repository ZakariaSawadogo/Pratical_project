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
C:.
├───.idea
│   └───inspectionProfiles
├───.venv
│   ├───include
│   │   └───site
│   │       └───python3.13
│   │           └───pygame
│   │               └───include
│   ├───Lib
│   │   └───site-packages
│   │       ├───arabic_reshaper
│   │       │   └───__pycache__
│   │       ├───arabic_reshaper-3.0.0.dist-info
│   │       ├───bidi
│   │       │   └───__pycache__
│   │       ├───pip
│   │       │   ├───_internal
│   │       │   │   ├───cli
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───commands
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───distributions
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───index
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───locations
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───metadata
│   │       │   │   │   ├───importlib
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───models
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───network
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───operations
│   │       │   │   │   ├───build
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───install
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───req
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───resolution
│   │       │   │   │   ├───legacy
│   │       │   │   │   ├───resolvelib
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───utils
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───vcs
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   ├───_vendor
│   │       │   │   ├───cachecontrol
│   │       │   │   │   ├───caches
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───certifi
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───distlib
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───distro
│   │       │   │   ├───idna
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───msgpack
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───packaging
│   │       │   │   │   ├───licenses
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───pkg_resources
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───platformdirs
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───pygments
│   │       │   │   │   ├───filters
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───formatters
│   │       │   │   │   ├───lexers
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───styles
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───pyproject_hooks
│   │       │   │   │   ├───_in_process
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───requests
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───resolvelib
│   │       │   │   │   ├───compat
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───rich
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───tomli
│   │       │   │   ├───truststore
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───urllib3
│   │       │   │   │   ├───contrib
│   │       │   │   │   │   ├───_securetransport
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───packages
│   │       │   │   │   │   ├───backports
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───util
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───pip-25.0.1.dist-info
│   │       ├───pygame
│   │       │   ├───docs
│   │       │   │   ├───generated
│   │       │   │   │   ├───c_api
│   │       │   │   │   ├───ref
│   │       │   │   │   ├───tut
│   │       │   │   │   ├───_images
│   │       │   │   │   ├───_sources
│   │       │   │   │   │   └───ref
│   │       │   │   │   └───_static
│   │       │   │   └───__pycache__
│   │       │   ├───examples
│   │       │   │   ├───data
│   │       │   │   └───__pycache__
│   │       │   ├───tests
│   │       │   │   ├───fixtures
│   │       │   │   │   ├───fonts
│   │       │   │   │   └───xbm_cursors
│   │       │   │   ├───run_tests__tests
│   │       │   │   │   ├───all_ok
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───everything
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───exclude
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───failures1
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───incomplete
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───incomplete_todo
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───infinite_loop
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───print_stderr
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───print_stdout
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───timeout
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───test_utils
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   ├───threads
│   │       │   │   └───__pycache__
│   │       │   ├───_sdl2
│   │       │   │   └───__pycache__
│   │       │   ├───__pycache__
│   │       │   └───__pyinstaller
│   │       │       └───__pycache__
│   │       ├───pygame-2.6.1.dist-info
│   │       ├───python_bidi-0.6.6.dist-info
│   │       │   └───licenses
│   │       └───__pycache__
│   └───Scripts
├───flags
├───sounds
├───words
└───__pycache__

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

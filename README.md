# John Williams Movie Guesser

A sleek, desktop-based trivia game designed to test your knowledge of the legendary film composer John Williams. The app plays a random 15-second snippet from his most iconic scores, and it’s up to you to identify the film.

## Features
* **Randomized Snippets:** Every round picks a random starting point in a track, ensuring the game stays challenging.
* **Minimalist GUI:** A clean, light-mode interface built with Tkinter.
* **Reveal Mode:** After guessing, you can play the full track starting from 5 seconds before your snippet to hear the context of the music.
* **Automated Folder Management:** The script automatically generates the necessary directory structure for your music library.

##Important: Music Files Not Included
**To comply with copyright laws, this repository does not include any audio files.** Users must provide their own music from their personal collection. The game is compatible with `.mp3`, `.m4a`, and `.wav` formats.

## Getting Started

### Prerequisites
* **Operating System:** Windows (The game uses the Windows Multimedia API (`winmm.dll`) for low-latency audio playback).
* **Python:** Version 3.x.
* **Libraries:** No external pip installations are required! It uses built-in libraries like `tkinter` and `ctypes`.

### Installation & Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/john-williams-guesser.git
    cd john-williams-guesser
    ```
2.  **Run the script once to generate folders:**
    ```bash
    python main.py
    ```
    This will create a `movies/` directory with subfolders for each supported film.
3.  **Add your music:**
    Place your audio files into their respective movie folders:
    * `movies/A New Hope/`
    * `movies/The Empire Strikes Back/`
    * `movies/Raiders of the Lost Ark/`
    * *(And so on...)*

### How to Play
1.  Launch the game: `python main.py`.
2.  Click **PLAY CLIP** to hear a 15-second random segment of a John Williams track.
3.  Select the movie you think the music belongs to.
4.  View your result and click **PLAY TO END** if you want to keep the vibe going, or **Next Round** to keep playing.

## Supported Movies
Currently, the game tracks the following scores:
* **Star Wars:** Episodes IV, V, VI, I, II, III, and VII.
* **Indiana Jones:** Raiders, Temple of Doom, and Last Crusade.

## Disclaimer
This project is for educational and personal use only. All rights to the music and film titles belong to their respective owners (Lucasfilm Ltd., Disney, etc.). Please support the artists by purchasing their music through official channels.

## Gallery
<img width="1211" height="1173" alt="image" src="https://github.com/user-attachments/assets/f35a415b-6325-4414-a60b-32d432549cce" />
<img width="1183" height="1154" alt="image" src="https://github.com/user-attachments/assets/449d54ba-aa7b-4710-bd84-5e586c99aaee" />
<img width="1147" height="1116" alt="image" src="https://github.com/user-attachments/assets/c72a27cf-dea6-4899-8530-fabc8bd88f9d" />

# John Williams Movie Guesser

John Williams is a fantastic composer, and I love his work, but if you watch enough of his movies, you'll notice that they tend to sound the same. I built this game to test my and my friend's knowledge of his work, and it's been fun and pretty difficult! The game will play a clip from one of his soundtracks, and it's up to you to guess which movie it's from! Enjoy!

## Features
* **Randomized Snippets:** Every round picks a random starting point in a track, ensuring the game stays challenging with infinite replayability.
* **Reveal Mode:** After guessing, you can play the full track to see how wrong you were.
* **Automated Game Adjustment:** The script automatically generates the guess buttons from the folder names.

## Important: Music Files Not Included
**To comply with copyright laws, this repository does not include any audio files.** Users must provide their own music from their personal collection. The game is compatible with `.mp3`, `.m4a`, and `.wav` formats.

## Getting Started

### Prerequisites
* **Operating System:** Windows.
* **Python:** Version 3.x.
* **Libraries:** No external pip installations are required! It uses built-in libraries like `tkinter` and `ctypes`.

### Installation & Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/john-williams-guesser.git
    cd john-williams-guesser
    ```
2.  **Make a movies folder:**
     In the same directory as `main.py`, create a `movies/` folder with subfolders for each supported film.
    
4.  **Add your music:**
    Place your audio files into their respective movie folders:
    * `movies/A New Hope/`
    * `movies/The Empire Strikes Back/`
    * `movies/Raiders of the Lost Ark/`
    * *(And so on...)*

### How to Play
1.  Launch the game: `python main.py`.
2.  Click **PLAY CLIP** to hear a 15-second random segment of a John Williams track.
3.  Select the movie you think the music belongs to.
4.  View your result and click **PLAY TO END** if you want to keep listening, or **Next Round** to keep playing.

## Disclaimer
This project is for entertainment and personal use only. All rights to the music and film titles belong to their respective owners (Lucasfilm Ltd., Disney, etc.). Please support the artists by purchasing their music through official channels (or search internet archive or https://download-sountracks.com or i'll just put this here... drive.google.com/file/d/14Ot4LIhdgMPtKlPMpKCOzkcFPT1SQHcj/view?usp=sharing)

## Gallery
<img width="1211" height="1173" alt="image" src="https://github.com/user-attachments/assets/f35a415b-6325-4414-a60b-32d432549cce" />
<img width="1183" height="1154" alt="image" src="https://github.com/user-attachments/assets/449d54ba-aa7b-4710-bd84-5e586c99aaee" />
<img width="1147" height="1116" alt="image" src="https://github.com/user-attachments/assets/c72a27cf-dea6-4899-8530-fabc8bd88f9d" />

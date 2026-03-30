import tkinter as tk
from tkinter import ttk
import os
import random
import ctypes

winmm = ctypes.windll.winmm

def get_short_path_name(long_name):
    buf_size = 1024
    buf = ctypes.create_unicode_buffer(buf_size)
    ctypes.windll.kernel32.GetShortPathNameW(long_name, buf, buf_size)
    return buf.value if buf.value else long_name

CLIP_DURATION = 15  # Change this value to adjust the play clip length (in seconds)

MOVIES = [
    "A New Hope",
    "The Empire Strikes Back",
    "Return of the Jedi",
    "The Phantom Menace",
    "Attack of the Clones",
    "Revenge of the Sith",
    "The Force Awakens",
    "Raiders of the Lost Ark",
    "The Temple of Doom",
    "The Last Crusade"
]

class AudioPlayer:
    def __init__(self, file_path):
        self.file_path = get_short_path_name(os.path.abspath(file_path))
        self.start_ms = None
        self.length_ms = 0
        
        winmm.mciSendStringW('close myaudio', None, 0, 0)
        winmm.mciSendStringW(f'open "{self.file_path}" alias myaudio', None, 0, 0)
        buf = ctypes.create_unicode_buffer(256)
        winmm.mciSendStringW('status myaudio length', buf, 255, 0)
        try:
            self.length_ms = int(buf.value)
        except ValueError:
            self.length_ms = 0
            
    def play_snippet(self, duration_sec=CLIP_DURATION):
        # Stop any existing
        winmm.mciSendStringW('close myaudio', None, 0, 0)
        # Open file
        winmm.mciSendStringW(f'open "{self.file_path}" alias myaudio', None, 0, 0)
        
        if self.start_ms is None:
            duration_ms = int(duration_sec * 1000)
            if self.length_ms > duration_ms:
                self.start_ms = random.randint(0, self.length_ms - duration_ms)
            else:
                self.start_ms = 0
            
        duration_ms = int(duration_sec * 1000)
        end_ms = self.start_ms + duration_ms
        winmm.mciSendStringW(f'play myaudio from {self.start_ms} to {end_ms}', None, 0, 0)

    def play_full(self, start_ms=0):
        winmm.mciSendStringW('close myaudio', None, 0, 0)
        winmm.mciSendStringW(f'open "{self.file_path}" alias myaudio', None, 0, 0)
        winmm.mciSendStringW(f'play myaudio from {start_ms} to {self.length_ms}', None, 0, 0)

class GuesserApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("John Williams Movie Guesser")
        self.geometry("700x650")
        self.configure(bg="#ffffff") # Light mode background
        
        style = ttk.Style(self)
        try:
            style.theme_use('clam') # Clean look if available
        except tk.TclError:
            pass
        
        # Light mode styles
        style.configure("TFrame", background="#ffffff")
        style.configure("TLabel", background="#ffffff", foreground="#333333", font=("Segoe UI", 12))
        style.configure("Header.TLabel", font=("Segoe UI", 24, "bold"), foreground="#2c3e50")
        style.configure("Result.TLabel", font=("Segoe UI", 36, "bold"))
        
        self.movies_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "movies")
        
        # Make sure directory exists just in case
        if not os.path.exists(self.movies_dir):
            os.makedirs(self.movies_dir)
            for m in MOVIES:
                os.makedirs(os.path.join(self.movies_dir, m), exist_ok=True)
        
        self.frames = {}
        
        # Initialize Both Screens
        for F in (GameFrame, ResultFrame):
            frame = F(self, self)
            self.frames[F] = frame
            # Grid handles overlapping layout perfectly
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.current_movie = None
        self.current_player = None
        
        self.load_new_clip()
        self.show_frame(GameFrame)
        
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
        
    def rebuild_playlist(self):
        self.playlist = []
        if os.path.exists(self.movies_dir):
            for m in MOVIES:
                folder_path = os.path.join(self.movies_dir, m)
                if os.path.exists(folder_path):
                    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.mp3', '.m4a', '.wav'))]
                    for f in files:
                        self.playlist.append((m, os.path.join(folder_path, f), f))
        
        random.shuffle(self.playlist)

    def pick_random_clip(self):
        if not hasattr(self, 'playlist') or not self.playlist:
            self.rebuild_playlist()
            
        if not self.playlist:
            return None, None, None
            
        return self.playlist.pop()

    def load_new_clip(self):
        movie, path, filename = self.pick_random_clip()
        
        if not movie:
            self.current_movie = None
            self.current_song = None
            self.current_player = None
            self.frames[GameFrame].status_label.config(text="No MP3 files found! Add some to the movies/ folder.")
        else:
            self.current_movie = movie
            self.current_song = os.path.splitext(filename)[0]
            self.current_player = AudioPlayer(path)
            self.frames[GameFrame].status_label.config(text="Clip ready! Press Play.")

    def play_clip(self):
        if self.current_player:
            self.current_player.play_snippet(duration_sec=CLIP_DURATION)
            
    def make_guess(self, guessed_movie):
        # Ignore if no files available
        if not self.current_movie:
            return 
            
        winmm.mciSendStringW('stop myaudio', None, 0, 0)
            
        is_correct = (guessed_movie == self.current_movie)
        
        # Update and switch to Result frame
        result_frame = self.frames[ResultFrame]
        result_frame.update_result(is_correct, self.current_movie, self.current_song)
        self.show_frame(ResultFrame)
        
    def next_round(self):
        winmm.mciSendStringW('close myaudio', None, 0, 0)
        self.load_new_clip()
        self.show_frame(GameFrame)


class GameFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        header = ttk.Label(self, text="John Williams Movie Guesser", style="Header.TLabel")
        header.pack(pady=(30, 5))
        
        self.status_label = ttk.Label(self, text="Loading...")
        self.status_label.pack(pady=5)
        
        # Play clip button
        play_btn = tk.Button(self, text=f"▶ PLAY CLIP ({CLIP_DURATION}s)", font=("Segoe UI", 16, "bold"), 
                              bg="#3498db", fg="white", activebackground="#2980b9", 
                              activeforeground="white", relief="flat", cursor="hand2",
                              command=self.controller.play_clip, padx=30, pady=15)
        play_btn.pack(pady=20)
        
        instruction = ttk.Label(self, text="Guess the movie:", font=("Segoe UI", 12, "italic"))
        instruction.pack(pady=(10, 5))
        
        grid_frame = ttk.Frame(self)
        grid_frame.pack(pady=10)
        
        for i, movie in enumerate(MOVIES):
            row = i // 3
            col = i % 3
            
            btn = tk.Button(grid_frame, text=movie, font=("Segoe UI", 11),
                            bg="#f8f9fa", fg="#333", activebackground="#e2e6ea",
                            relief="ridge", width=22, height=2, cursor="hand2",
                            command=lambda m=movie: self.controller.make_guess(m))
            btn.grid(row=row, column=col, padx=8, pady=8)


class ResultFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Container to center elements in this frame
        self.container = ttk.Frame(self)
        self.container.place(relx=0.5, rely=0.5, anchor="center")
        
        self.result_label = ttk.Label(self.container, style="Result.TLabel", justify="center")
        self.result_label.pack(pady=10)
        
        self.info_label = ttk.Label(self.container, font=("Segoe UI", 18), justify="center")
        self.info_label.pack(pady=5)
        
        self.song_label = ttk.Label(self.container, font=("Segoe UI", 14, "italic"), foreground="#7f8c8d", justify="center", wraplength=600)
        self.song_label.pack(pady=(0, 20))
        
        self.play_btn = tk.Button(self.container, text="▶ PLAY TO END", font=("Segoe UI", 14, "bold"), 
                              bg="#3498db", fg="white", activebackground="#2980b9", 
                              activeforeground="white", relief="flat", cursor="hand2",
                              command=self.play_end_clip, padx=20, pady=10)
        self.play_btn.pack(pady=10)
        
        self.next_btn = tk.Button(self.container, text="Next Round ➡", font=("Segoe UI", 16, "bold"),
                                  bg="#2ecc71", fg="white", activebackground="#27ae60",
                                  activeforeground="white", relief="flat", cursor="hand2",
                                  padx=30, pady=15,
                                  command=self.controller.next_round)
        self.next_btn.pack(pady=20)
        
    def update_result(self, is_correct, actual_movie, song_name):
        self.song_label.config(text=f"Track: {song_name}")
            
        if is_correct:
            self.result_label.config(text="RIGHT!", foreground="#27ae60")
            self.info_label.config(text=f"Great job, it was indeed\n{actual_movie}!")
        else:
            self.result_label.config(text="WRONG!", foreground="#e74c3c")
            self.info_label.config(text=f"The correct answer was:\n{actual_movie}")

    def play_end_clip(self):
        player = self.controller.current_player
        if player and player.start_ms is not None:
            # Start exactly 5 seconds before the clip's original start time
            start_ms = max(0, player.start_ms - 5000)
            player.play_full(start_ms)


if __name__ == "__main__":
    app = GuesserApp()
    app.mainloop()

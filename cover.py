from pydub import AudioSegment, utils
from pydub.playback import play
import speech_recognition as sr
import IPython
from youtubesearchpython import VideosSearch
from youtube_search import YoutubeSearch
from pytube import YouTube
from pydub import AudioSegment
import tkinter as tk
from threading import Thread
import time
from tkinter import messagebox
from PIL import ImageTk,Image,ImageSequence

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Enter artist name")
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for artist name
        self.artist_label = tk.Label(self, text="Enter artist name:")
        self.artist_label.config(font=("Arial", 20), fg="#ffffff", bg="#000000")  # Set label font, foreground and background colors
        self.artist_label.pack(pady=(20, 5), padx=5, anchor=tk.CENTER)

        self.artist_entry = tk.Entry(self)
        self.artist_entry.config(font=("Arial", 20), bg="#ffffff", fg="#000000", justify=tk.CENTER)  # Set entry font, foreground and background colors, and center text
        self.artist_entry.pack(pady=(5, 20), padx=5, ipady=10, anchor=tk.CENTER)

        # Button to submit artist name
        self.submit_button = tk.Button(self, text="Submit", command=lambda:yt(self.artist_entry.get()))
        self.submit_button.config(font=("Arial", 20), fg="#ffffff", bg="#0077cc")  # Set button font, foreground and background colors
        self.submit_button.pack(pady=(10, 20), padx=5, ipadx=50, ipady=10, anchor=tk.CENTER)

        # Center the frame within the window
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def call(self,t):
        self.submit_button.destroy()
        self.artist_entry.destroy()
        self.artist_label.destroy()
        self.artist_label = tk.Label(self, text=t)
        self.artist_label.config(font=("Arial", 20), fg="#ffffff",bg="#000000")  # Set label font, foreground and background colors
        self.artist_label.pack(pady=500, padx=5, anchor=tk.CENTER)
    def submit_artist(self):
        # Get artist name from entry
        artist_name = self.artist_entry.get()
        print(artist_name)
        self.call("ew")

        #self.artist_label.config(text="Sperating vocals from background...")
        # self.master.destroy()
        # root = tk.Tk()
        # root.state('zoomed')
        # app = AfterArtist(master=root)
        # app['background'] = '#000000'
        # app.mainloop()


from tkinter import messagebox


class AfterArtist(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x200")
        self.master.configure(bg='#000000')
        self.master.title("Options")
        self.pack(expand=True, fill="both", padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        # Label for options
        self.lbl_option = tk.Label(self, text="Select an option:", font=("Arial", 12))
        self.lbl_option.config(font=("Arial", 20), fg="#ffffff", bg="#000000")
        self.lbl_option.pack(pady=(20, 5), padx=5, anchor=tk.CENTER)
        # self.lbl_option.pack(pady=10)

        # TTS button
        self.btn_tts = tk.Button(self, text="Text-to-Speech", font=("Arial", 10), command=self.show_tts)
        self.btn_tts.config(width=20, height=2)
        self.btn_tts.pack(pady=10)

        # Song cover button
        self.btn_song = tk.Button(self, text="Song Cover", font=("Arial", 10), command=self.show_song)
        self.btn_song.config(width=20, height=2)
        self.btn_song.pack(pady=10)

        # Conversation button
        self.btn_conv = tk.Button(self, text="Conversation", font=("Arial", 10), command=self.show_conv)
        self.btn_conv.config(width=20, height=2)
        self.btn_conv.pack(pady=10)

    def show_tts(self):
        # Clear current widgets
        self.clear_widgets()

        # Label and Entry for TTS text
        self.lbl_tts = tk.Label(self, text="Enter text for TTS:", font=("Arial", 24), fg="#3F3F3F")
        self.lbl_tts.pack(pady=(50, 10), padx=10, anchor=tk.CENTER)
        self.entry_tts = tk.Entry(self, font=("Arial", 20), bg="#F1F1F1", fg="#3F3F3F", bd=0, highlightthickness=1,
                                  highlightcolor="#BFBFBF", highlightbackground="#BFBFBF")
        self.entry_tts.pack(pady=10, ipady=10, ipadx=20)

        # Button to submit TTS text
        self.btn_submit = tk.Button(self, text="Submit", font=("Arial", 16), bg="#4CAF50", fg="#FFFFFF", bd=0, padx=30,
                                    pady=10, command=self.submit_tts)
        self.btn_submit.pack(pady=20, ipady=5, ipadx=20)

        # Center the widgets
        self.lbl_tts.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.entry_tts.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.btn_submit.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def show_song(self):
        # Clear current widgets
        self.clear_widgets()

        # Label and Entry for song cover URL
        self.lbl_song = tk.Label(self, text="Enter song cover URL:", font=("Arial", 20), fg="#4c4c4c")
        self.lbl_song.pack(pady=(20, 5), padx=5, anchor=tk.CENTER)
        self.entry_song = tk.Entry(self, font=("Arial", 16))
        self.entry_song.pack(pady=5, ipady=5, ipadx=10)

        # Button to submit song cover URL
        self.btn_submit = tk.Button(self, text="Submit", font=("Arial", 14), bg="#1db954", fg="white",
                                    command=self.submit_song)
        self.btn_submit.pack(pady=10, ipady=5, ipadx=20)

        self.lbl_song.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.entry_song.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.btn_submit.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def show_conv(self):
        # Clear current widgets
        self.clear_widgets()

        # Label and Entry for conversation text
        self.lbl_conv = tk.Label(self, text="Enter conversation text:", font=("Arial", 20), fg="#4c4c4c")
        self.lbl_conv.pack(pady=(20, 5), padx=5, anchor=tk.CENTER)
        self.entry_conv = tk.Entry(self, font=("Arial", 16))
        self.entry_conv.pack(pady=5, ipady=5, ipadx=10)

        # Button to submit conversation text
        self.btn_submit = tk.Button(self, text="Submit", font=("Arial", 14), bg="#1db954", fg="white",
                                    command=self.submit_conv)
        self.btn_submit.pack(pady=10, ipady=5, ipadx=20)

        self.lbl_conv.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.entry_conv.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.btn_submit.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def submit_tts(self):
        # Get TTS text from entry
        tts_text = self.entry_tts.get()

    def submit_song(self):
        # Get song cover URL from entry
        song_url = self.entry_song.get()

    def submit_conv(self):
        # Get conversation text from entry
        conv_text = self.entry_conv.get()

    def clear_widgets(self):
        # Clear all current widgets
        for widget in self.winfo_children():
            widget.destroy()

# combining all clips in data
def combine():
    audio = AudioSegment.from_wav("separated audio/clip0/vocals.wav")
    for i in range(1, 10):
        try:
            audio += AudioSegment.from_wav(f"separated audio/clip{i}/vocals.wav")
        except:
            pass
    audio.export("full.wav", format="wav")


# extract most frequent speaker
def speakerdiarization():
    from pyannote.audio import Pipeline
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                        use_auth_token="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")
    diarization = pipeline("full.wav")
    speakers = []
    import numpy as np
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        speakers.append(speaker.split("_")[1])
    speakers = np.argmax(np.bincount(speakers))
    return diarization, speakers


# extracting audio clips of most frequent speaker
def clean(diarization, speakers):
    full = AudioSegment.from_wav("full.wav")
    import os
    try:
        os.makedirs("clean")
    except:
        pass
    i = 0
    if (speakers < 10):
        speakers = "0" + str(speakers)
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        # print(speaker.split("_")[1])
        if str(speakers) == speaker.split("_")[1]:
            # print("w")
            clip = full[turn.start * 1000:turn.end * 1000]
            clip.export(f"clean/clean{i}.wav", format="wav")
            i += 1
    return i


# combining all the clean clips
def preprocess(i):
    audio = AudioSegment.from_wav("clean/clean0.wav")
    while (i != 0):
        try:
            audio += AudioSegment.from_wav(f"clean/clean{i}.wav")
        except:
            pass
        i -= 1
    audio.export("preprocessed.wav", format="wav")
    return "preprocessed.wav"

#seperating vocals and instrumental
def vocal():
    from spleeter.separator import Separator
    import os
    try:
        os.makedirs("separated audio")
    except:
        pass
    separator = Separator('spleeter:2stems')
    for i in range(0,11):
        try:
            str1 = f"vocal{i}"
            str2 = f"instumental{i}"
            str3 = "wav"
            separator.separate_to_file(f'data/clip{i}.wav', 'separated audio')
        except:
            pass
# converting yt to audio
def yt(a):
    query = a
    max_results = 10
    app.call("ew")
    import os
    try:
        os.makedirs("yt audio")
    except:
        pass
    try:
        os.makedirs("data")
    except:
        pass
    results = VideosSearch(query, limit=max_results, language="en")
    results = results.result()
    urls = []
    for i in results["result"]:
        urls.append(f"https://www.youtube.com/watch?v={i['id']}")
    i = 0
    for url in urls:
        try:
            video = YouTube(url,use_oauth=True, allow_oauth_cache=True)
            if video.length <= 1800:
                audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
                audio.download(output_path="yt audio", filename=f"clip{i}.wav")
                audio_file = AudioSegment.from_file(f'yt audio/clip{i}.wav')
                audio_file.export(f'data/clip{i}.wav', format='wav')
                i += 1
        except:
            continue


# getting text of preprocessed clip for context
def text():
    text1 = ""
    for q in range(0, 10):
        audio_file = AudioSegment.from_file('preprocessed.wav')
        chunk_length_ms = 10000
        chunks = utils.make_chunks(audio_file, chunk_length_ms)
        for i, chunk in enumerate(chunks):
            r = sr.Recognizer()
            chunk.export('for text.wav', format='wav')
            with sr.AudioFile('for text.wav') as source:
                try:
                    audio_text = r.record(source)
                    text1 += r.recognize_google(audio_text)
                except:
                    continue

def data_for_cover():
    import os
    try:
        os.makedirs("dataset_raw")
        try:
            os.makedirs("dataset_raw/result")
        except:
            pass
    except:
        pass
    audio_file = AudioSegment.from_file('preprocessed.wav')
    chunk_length_ms = 10000
    q=0
    chunks = utils.make_chunks(audio_file, chunk_length_ms)
    for i, chunk in enumerate(chunks):
        chunk.export(f'dataset_raw/result/clip{q}.wav', format='wav')
        q+=1

# text to speech for input name
def textto(text, s):
    from TTS.api import TTS
    model_name = TTS.list_models()[6]
    tts = TTS(model_name=model_name, progress_bar=False, gpu=False)
    tts.tts_with_vc_to_file(text, speaker_wav=s, file_path="output.wav")
    # IPython.display.Audio("output.wav")

def song_cover():
    import os
    os.system("cd Documnets/ai song cover")
    os.system("svc pre-resample")
    os.system("svc pre-config")
    os.system("svc pre-hubert")
    os.system("svc train -t")
    os.system("svc infer songwav/song/vocals.wav -m logs/44k/G_0.pth -s result")

def song(url):
    import os
    try:
        os.makedirs("song")
    except:
        pass
    try:
        os.makedirs("songwav")
    except:
        pass
    video = YouTube(url,use_oauth=True, allow_oauth_cache=True)
    audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
    audio.download(output_path="song", filename=f"song.wav")
    audio_file = AudioSegment.from_file(f'song/song.wav')
    audio_file.export(f'songwav/song.wav', format='wav')
    from spleeter.separator import Separator
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(f'songwav/song.wav', 'songwav')
def final():
    song_path = AudioSegment.from_wav("songwav/song/accompaniment.wav")
    artist_voice_path = AudioSegment.from_wav("songwav/song/vocals.out.wav")

    combined_audio = song_path.overlay(artist_voice_path)
    combined_audio.export("song ft artist.wav", format="wav")
    song_ft = AudioSegment.from_wav("song ft artist.wav")
    play(song_ft)

# combinig all sample clips
def combineown():
    audio = AudioSegment.from_wav("samples/sample0.wav")
    for i in range(0, 10):
        try:
            audio += AudioSegment.from_wav(f"samples/sample{i}.wav")
        except:
            break
    audio.export("own.wav", format="wav")
    return "own.wav"


#yt("drake")
#vocal()
#combine()
# diarization,speakers = speakerdiarization()
# i = clean(diarization,speakers)
# s = preprocess(i)
#textto("sun is down freezing cold,you already know","preprocessed.wav")
#song("https://www.youtube.com/watch?v=pBVtSwb5G7M")
#data_for_cover()
#song_cover()
#final()
import tkinter as tk

import main


def show_song():
    return
def show_conv():
    return

def AfterArtist(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    lbl_option = tk.Label(root, text="Select an option:", font=("Gabriola", 40), bg = '#1d1d1d', fg = "#ffffff", relief="flat")
    lbl_option.place(x=0.67*screen_width, y=0.40*screen_height, anchor="center")
    btn_tts = tk.Button(root, text="Text-to-Speech", command= lambda : show_tts(root, lbl_option, btn_tts, btn_conv, btn_song), font=("Constantia", 25), fg="#00ff00", bg="#1d1d1d", relief="groove")
    btn_tts.place(x=0.67*screen_width, y=0.54*screen_height, anchor="center")
    btn_song = tk.Button(root, text="Song Cover", command= lambda : show_song(root, lbl_option, btn_tts, btn_conv, btn_song), font=("Constantia", 25), fg="#00ff00", bg="#1d1d1d", relief="groove")
    btn_song.place(x=0.67*screen_width, y=0.67*screen_height, anchor="center")
    btn_conv = tk.Button(root, text="Conversation", command= lambda : show_conv(root, lbl_option, btn_tts, btn_conv, btn_song), font=("Constantia", 25), fg="#00ff00", bg="#1d1d1d", relief="groove")
    btn_conv.place(x=0.67*screen_width, y=0.80*screen_height, anchor="center")


def destroyall(w1, w2, w3, w4):
       w1.destroy()
       w2.destroy()
       w3.destroy()
       w4.destroy()
       
def show_tts(root, w1, w2, w3, w4):
    # Clear current widgets
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        destroyall(w1, w2, w3, w4)

        # Label and Entry for TTS text
        lbl_tts = tk.Label(root, text="Enter text for TTS:", font=("Gabriola", 40), bg = '#1d1d1d', fg = "#ffffff", relief="flat")
        entry_tts = tk.Entry(root, font=("Arial", 20), bg="#343434", fg="#ffffff", justify=tk.CENTER, width=25 ,relief="flat")
        # Button to submit TTS text
        btn_submit = tk.Button(root, text="Submit", font=("Constantia", 25), fg="#FFC90E", bg="#1d1d1d", relief="groove", command= lambda : submit_tts(entry_tts))

        # Center the widgets
        lbl_tts.place(x=0.67*screen_width, y=0.44*screen_height, anchor="center")
        entry_tts.place(x=0.67*screen_width, y=0.58*screen_height, anchor="center")
        btn_submit.place(x=0.67*screen_width, y=0.72*screen_height, anchor="center")

    



def show_song(root, w1, w2, w3, w4):
        # Clear current widgets
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        destroyall(w1, w2, w3, w4)

        # Label and Entry for song cover URL
        lbl_song = tk.Label(root, text="Enter song cover URL:", font=("Gabriola", 40), bg = '#1d1d1d', fg = "#ffffff", relief="flat")
        entry_song = tk.Entry(root, font=("Arial", 20), bg="#343434", fg="#ffffff", justify=tk.CENTER, width=25 ,relief="flat")
        # Button to submit song cover URL
        btn_submit = tk.Button(root, text="Submit", font=("Constantia", 25), fg="#FFC90E", bg="#1d1d1d", relief="groove", command= lambda : submit_song(entry_song))
        
        lbl_song.place(x=0.67*screen_width, y=0.44*screen_height, anchor="center")
        entry_song.place(x=0.67*screen_width, y=0.58*screen_height, anchor="center")
        btn_submit.place(x=0.67*screen_width, y=0.72*screen_height, anchor="center")


# def show_conv(root, w1, w2, w3, w4):
        # Clear current widgets
        # screen_width = root.winfo_screenwidth()
        # screen_height = root.winfo_screenheight()
        # destroyall(w1, w2, w3, w4)
        #
        # # Label and Entry for conversation text
        # lbl_conv = tk.Label(root, text="Enter conversation text:", font=("Gabriola", 40), bg = '#1d1d1d', fg = "#ffffff", relief="flat")
        # entry_conv = tk.Entry(root, font=("Arial", 20), bg="#343434", fg="#ffffff", justify=tk.CENTER, width=25 ,relief="flat")
        # # Button to submit conversation text
        # btn_submit = tk.Button(root, text="Submit", font=("Constantia", 25), fg="#FFC90E", bg="#1d1d1d", relief="groove", command= lambda : submit_conv(entry_conv))
        #
        # lbl_conv.place(x=0.67*screen_width, y=0.44*screen_height, anchor="center")
        # entry_conv.place(x=0.67*screen_width, y=0.58*screen_height, anchor="center")
        # btn_submit.place(x=0.67*screen_width, y=0.72*screen_height, anchor="center")


def submit_tts(entry_tts):
        # Get TTS text from entry
        tts_text = entry_tts.get()
        main.textto(tts_text,"preprocessed.wav")
        print(tts_text)

def submit_song(entry_song):
        # Get song cover URL from entry
        song_url = entry_song.get()
        main.song(song_url)
        main.data_for_cover()
        main.song_cover()
        main.final()
        print(song_url)

# def submit_conv(entry_conv):
#         # Get conversation text from entry
#         conv_text = entry_conv.get()
#         print(conv_text)
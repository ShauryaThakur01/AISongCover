import tkinter as tk
from speech2 import AfterArtist
from PIL import ImageTk, Image
import main
def quitter(e):
	root.quit()

def submit_artist(root, artist_label, artist_entry, submit_button):
    # Get artist name from entry
    artist_name = artist_entry.get()
    print(artist_name)
    if(artist_name!="skip"):
        main.yt(artist_name)
        main.vocal()
        main.combine()
        diarization,speakers = main.speakerdiarization()
        i = main.clean(diarization,speakers)
        s = main.preprocess(i)
    artist_label.destroy()
    artist_entry.destroy()
    submit_button.destroy()
    AfterArtist(root)

def MainApp():
    global root
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.overrideredirect(True)
    bg = (Image.open("AiSONG.png"))
    resized_image= bg.resize((screen_width,screen_height), Image.LANCZOS)
    bg = ImageTk.PhotoImage(resized_image)
    BackGround = tk.Label(root, image = bg)
    BackGround.place(x = -2, y = -2)
    root.state('zoomed')

    #close button
    close_label = tk.Label(root, text="×", font=('Helvetica', 30, 'bold'), bg="#1d1d1d", fg="#fff", relief="sunken", bd=0)
    close_label.place( x = 0.99*screen_width, y=0, anchor='ne')
    close_label.bind("<Button-1>", quitter)

    artist_label = tk.Label(root, text="Enter Artist Name", font=("Gabriola", 40), bg = '#1d1d1d', fg = "#ffffff", relief="flat")
    artist_label.place(x=0.67*screen_width, y=0.44*screen_height, anchor="center")
    artist_entry = tk.Entry(root,font=("Arial", 20), bg="#343434", fg="#ffffff", justify=tk.CENTER, width=25 ,relief="flat")
    artist_entry.place(x=0.67*screen_width, y=0.58*screen_height, anchor="center")
    submit_button = tk.Button(root, text="Submit", command= lambda : submit_artist(root, artist_label, artist_entry, submit_button), font=("Constantia", 25), fg="#FFC90E", bg="#1d1d1d", relief="groove")
    submit_button.place(x=0.67*screen_width, y=0.72*screen_height, anchor="center")

    root.mainloop()
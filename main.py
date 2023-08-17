from pydub import AudioSegment, utils
from pydub.playback import play
import speech_recognition as sr
import IPython
from youtubesearchpython import VideosSearch
from youtube_search import YoutubeSearch
from pytube import YouTube
from pydub import AudioSegment


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
    audio = AudioSegment.from_wav("output.wav")
    play(audio)

def song_cover():
    import os
    os.system("cd C:/Users/AKSHITH/Documents/ai song cover")
    # os.system("svc pre-resample")
    # os.system("svc pre-config")
    # os.system("svc pre-hubert")
    # os.system("svc train -t")
    os.system(f"svc infer songwav/song/vocals.wav -m logs/44k/drake.pth -s result")

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


# yt("drake") Shreyash
# vocal() akshith
# combine()  shreyash
# diarization,speakers = speakerdiarization()  shaurya
# i = clean(diarization,speakers) shriyash
# s = preprocess(i)  shriyash
# textto("sun is down freezing cold,you already know","preprocessed.wav") shriyash
# song("https://www.youtube.com/watch?v=mzB1VGEGcSU")  akshith
# data_for_cover() shaurya
# song_cover()   akshith
final()
#gui shreyash
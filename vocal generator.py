import os
# try:
#     os.makedirs("dataset_raw/result")
# except:
#     pass
os.system("cd C:/Users/AKSHITH/Documents/ai song cover")
# os.system("svc pre-resample")
# os.system("svc pre-config")
# os.system("svc pre-hubert")
# os.system("svc train")
os.system("svc infer songwav/song/vocals.wav -m logs/44k/drake.pth -s result")

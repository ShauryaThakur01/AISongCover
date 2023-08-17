from TTS.api import TTS
from pydub import AudioSegment,utils
model_name = TTS.list_models()
i=model_name[6]
tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24", progress_bar=True, gpu=False)
# audio_file = AudioSegment.from_file('songwav/song/vocals.wav')
# chunk_length_ms = 10000
# q=0
# chunks = utils.make_chunks(audio_file, chunk_length_ms)
# for i, chunk in enumerate(chunks):
#     chunk.export(f'test/clip{q}.wav', format='wav')
#     q+=1
for i in range(0,21):
    #tts.voice_conversion(source_wav=f"test/clip{i}.wav", target_wav="preprocessed.wav")
    tts.voice_conversion_to_file(source_wav=f"test/clip{i}.wav", target_wav="preprocessed.wav",file_path=f"test/q{i}.wav")
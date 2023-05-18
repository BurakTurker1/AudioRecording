import sounddevice as sd
import soundfile as sf

duration = int(input("Lütfen kayıt süresini yazınız (saniye): "))
fs = 44100

myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()

filename = input("Lütfen dosya adını giriniz: ")  # Kaydedilecek dosyanın adını alın
filename += ".wav"  # Uzantıyı ekleyin

sf.write(filename, myrecording, fs)  # Ses dosyasını kaydet

print("Kaydedilen ses dosyası:", filename)

from pytube import YouTube

url = input('Qual a URL do vídeo: ')
video = YouTube(url)
nome_video = video.title
pegar_somente_audio = video.streams.filter(only_audio=True).first()
pegar_somente_audio.download(filename=nome_video)
from pytube import YouTube

# Список доступных разрешений видео:
def get_resolution_list(link):
    yt = YouTube(link)
    stream = yt.streams
    stream_list = list(stream.filter(file_extension='mp4', progressive='true').order_by('resolution'))
    stream_list = list(map(str, stream_list))
    stream_list = [stream_list[i].split() for i in range(len(stream_list))]

    resolution_list = [(stream_list[i][1][6:-1], stream_list[i][3][5:-1]) for i in range(len(stream_list))]

    res_str = ''
    for i in range(len(resolution_list)):
        res_str += '\n' + resolution_list[i][1]
        
    return 'Доступные разрешения видео: ' + res_str

# Список доступного качества аудио:
def get_bitrate_list(link):
    yt = YouTube(link)
    stream = yt.streams
    stream_list = list(stream.filter(only_audio=True).order_by('abr'))

    stream_list = list(map(str, stream_list))
    stream_list = [stream_list[i].split() for i in range(len(stream_list))]

    bitrate_list = [(stream_list[i][1][6:-1], stream_list[i][3][5:-1]) for i in range(len(stream_list))]
    print(bitrate_list)

    res_str = ''
    for i in range(len(bitrate_list)):
        res_str += '\n' + bitrate_list[i][1]
    return 'Доступное качество аудио: ' + res_str  

# Скачивание видеофайла по выбранному разрешению:
def download_video(link, save_path, resolution):
    yt = YouTube(link)
    stream = yt.streams
    stream_list = list(stream.filter(file_extension='mp4', progressive='true').order_by('resolution'))
    stream_list = list(map(str, stream_list))
    stream_list = [stream_list[i].split() for i in range(len(stream_list))]

    resolution_list = [(stream_list[i][1][6:-1], stream_list[i][3][5:-1]) for i in range(len(stream_list))]

    for i in range(len(resolution_list)):
        if resolution == resolution_list[i][1]:
            user_res = resolution_list[i][0]

    stream = yt.streams.get_by_itag(user_res)    
    stream.download(save_path)

# Скачивание аудио по выбранному битрейту:
def download_audio(link,  save_path, bitrate):
    yt = YouTube(link)
    stream = yt.streams
    stream_list = list(stream.filter(only_audio=True).order_by('abr'))

    stream_list = list(map(str, stream_list))
    stream_list = [stream_list[i].split() for i in range(len(stream_list))]

    bitrate_list = [(stream_list[i][1][6:-1], stream_list[i][3][5:-1]) for i in range(len(stream_list))]

    for i in range(len(bitrate_list)):
        if bitrate == bitrate_list[i][1]:
            user_bitrate = bitrate_list[i][0]

    stream = yt.streams.get_by_itag(user_bitrate)
    stream.download(save_path)
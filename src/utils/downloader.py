from pytube import YouTube

def get_video_info(url):
    yt = YouTube(url)
    video_streams = yt.streams.filter(progressive=True)
    audio_streams = yt.streams.filter(only_audio=True)
    return {
        'title': yt.title,
        'video_streams': list(video_streams),
        'audio_streams': list(audio_streams)
    }

def download_stream(stream, output_path, progress_callback):
    stream.download(output_path=output_path)

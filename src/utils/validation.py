import re

# source: https://stackoverflow.com/questions/4705996/python-regex-convert-youtube-url-to-youtube-video
def is_valid_youtube_url(url):
    youtube_regex = re.compile(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    return youtube_regex.match(url)

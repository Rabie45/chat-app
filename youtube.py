import pafy
import vlc
import urllib.request
import re
a=0
def URL(url):
    # creating pafy object of the video
    video = pafy.new(url)

    # getting best stream
    best = video.getbest()

    # creating vlc media player object
    media = vlc.MediaPlayer(best.url)
    media.audio_set_volume(50)
    media.video_set_scale(2)
    # start playing video
    media.play()
    return media


def takeSong(sound):
    print(sound)
    html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + sound)
    vido_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print('https://www.youtube.com/watch?v=' + vido_ids[0])
    return 'https://www.youtube.com/watch?v=' + vido_ids[0]


def volumeUp(media,volume):
    media.audio_set_volume(volume+20)

def volumeDown(media, volume):
        media.audio_set_volume(volume - 20)

def mute(media):
    media.audio_set_volume(a)
def stopMu(media):
    media.stop()

def play(media):
    media.play()

def pause(media):
        media.pause()



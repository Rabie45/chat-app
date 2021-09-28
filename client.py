import threading
import socket
import vlc
import youtube_test


name = input('whats ur name? : ')  #THE NAME OF THE USER
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))#to communicate withe server
mediaOBJ = vlc.MediaPlayer() # media object


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8') # always recive message

            if message == "start":  # if communication start send the name to the server
                client.send(name.encode('utf-8'))
            elif '-play' in message:   # play command
                song_URL = message.replace('-play ', '') # delete -play from the command
                url = youtube_test.takeSong(song_URL) # get the url of the song
                client.send(url.encode('utf-8'))
                mediaOBJ = youtube_test.URL(url)
                print(type(mediaOBJ))
            elif '-stop' in message: #stop the music
                youtube_test.stopMu(mediaOBJ)
                mediaOBJ.stop()
            elif '-pause' in message: #pause
                youtube_test.pause(mediaOBJ)
            elif '-con' in message: # contine
                youtube_test.play(mediaOBJ)


            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        data = f':{input("")}' #take the data
        message = name + data
        client.send(message.encode('utf-8'))
        if '-vu' in data: #volume up
            youtube_test.volumeUp(mediaOBJ, 100)
            a = mediaOBJ.audio_get_volume()
            print('up '+str(a))
        elif '-vd' in data: #volume down
            youtube_test.volumeDown(mediaOBJ, 20)
            a = mediaOBJ.audio_get_volume()
            print('down ' + str(a))
        elif '-mute' in data: #mute
            youtube_test.mute(mediaOBJ)
        elif '-con' in data:
            youtube_test.play(mediaOBJ)



receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()

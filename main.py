from pytube import YouTube
import requests

def yt_download():
    url = input('Enter Yt Link'  '      \n' )
    # path_name1 = input('what you wanna save ur file as ' +  '      \n') 
    def progress(stream,file):
        print(file)
    video = YouTube(url   , on_complete_callback=progress )

    print('enter (h) for hightest ,  (l) for lowest , (a) for audio only , (c) to cancel ' )
    inp = str(input('enter format'  +'      \n'))

    video_dl = 0
    if(inp == 'h'):
        video_dl = video.streams.get_highest_resolution()
    if(inp == 'l'):
        video_dl = video.streams.get_lowest_resolution()()
    if(inp == 'a'):
        video_dl = video.streams.get_audio_only()
    if(inp == 'c'):
        return print('exited')
    


    video_dl.download()

yt_download()
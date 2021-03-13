import os, sys, pytube, pyautogui
#Credit me hehe!

def menu():
    url = pyautogui.prompt('Youtube Link : ')
    url = url.replace('https', '')
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    print('Title : ',video.title)
    print('Press enter to download.')
    input('')
    video.download()
    print('Video Downloaded. \n press enter to go back')
    os.system('cls')
    menu()
menu()
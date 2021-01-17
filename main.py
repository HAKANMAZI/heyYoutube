import pytube
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_video_mp4(url, download_path):
    
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download(download_path)
    print(video)

def get_playlist_mp4(playlist_url, download_path):
    wd = webdriver.Chrome(ChromeDriverManager().install())
    wd.get(playlist_url)

    lists = []
    #video linklerini getir
    for a in wd.find_elements_by_xpath('.//a'):
        lists.append(a.get_attribute('href'))

    #video linklerinden gerçekten video olanları diziye aktardık
    matching = [s for s in lists if "watch?v" in str(s) ]
    #video ları eşşizleştirdik
    essis_list = list(set(matching))


    for x in essis_list:
        try:
            youtube = pytube.YouTube(x)
            video = youtube.streams.get_highest_resolution()
            video.download(download_path)
        except:
            print("Error "+ str(x))

def get_playlist_mp3(playlist_url, download_path):
    wd = webdriver.Chrome(ChromeDriverManager().install())
    wd.get(playlist_url)

    lists = []
    #video linklerini getir
    for a in wd.find_elements_by_xpath('.//a'):
        lists.append(a.get_attribute('href'))

    #video linklerinden gerçekten video olanları diziye aktardık
    matching = [s for s in lists if "watch?v" in str(s) ]
    #video ları eşşizleştirdik
    essis_list = list(set(matching))


    for x in essis_list:
        try:
            youtube = pytube.YouTube(x)
            ses = youtube.streams.filter(only_audio=True)
            out_file = ses[0].download(download_path)

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)


        except:
            print("Error "+ str(x))

def get_video_mp3(url, download_path):
    youtube = pytube.YouTube(url)
    ses = youtube.streams.filter(only_audio=True)
    out_file = ses[0].download(download_path)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


#get_playlist_mp3('https://www.youtube.com/watch?v=LiB1wj8_DQE&list=RDLiB1wj8_DQE&start_radio=1','videomp3')
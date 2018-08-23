from os import path
from os import system
import sys
from pytube import YouTube
from colorama import Fore,Back,Style

completed = []
errored = []

input_color = Fore.CYAN + Style.BRIGHT
info_color = Fore.WHITE + Style.BRIGHT
error_color = Fore.RED + Style.BRIGHT
reset = Style.RESET_ALL


def get_file_loc():
    while True:
        try:
            file_loc = input(reset + input_color + "Provide the file path : " + reset + info_color)
            if not path.exists(file_loc):
                raise ValueError
        except ValueError:
            print(reset + error_color + "Not a valid Path... Try Again" + reset,end="\n")
            continue
        except KeyboardInterrupt:
            print(reset + error_color + "Exiting..." + reset)
            sys.exit()
        else:
            break
    return file_loc


def get_download_type():
    while True:
        try:
            type = input(reset + input_color + "Press v and ENTER to download video, else press a and ENTER to download audio only : " + reset + info_color)
            if type not in ('v','V','a','A'):
                raise ValueError
        except ValueError:
            print(reset + error_color + "Not a valid Input (a or v)" + reset,end="\n")
            continue
        except KeyboardInterrupt:
            print(reset + error_color + "Exiting..." + reset)
            sys.exit()
        else:
            break
    return type    


def download(url,type,loc):
    try:
        yt = YouTube(url)
        print(reset + input_color + "Downloading " + reset + info_color +  yt.title + reset)
        if type == 'a':
            yt.streams.filter(only_audio=True, file_extension='mp4').order_by('resolution').desc().first().download(loc)
        else:
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(loc)
    except:
        return (1,yt.title)
    else:
        return (0,yt.title)


def get_download_loc():
    while True:
        try:
            down_loc = input(reset + input_color + "Provide the target path : " + reset + info_color)
            if not path.exists(down_loc):
                raise ValueError
        except ValueError:
            print(reset + error_color + "Not a valid Path... Try Again" + reset,end="\n")
            continue
        except KeyboardInterrupt:
            print(reset + error_color + "Exiting..." + reset)
            sys.exit()
        else:
            break
    return down_loc


if __name__ == '__main__':
    print(info_color + "Welcome to the Youtube Downloader... " + reset ,end="\n")
    while True:
        try:
            method = input(reset + input_color + "Press f and ENTER if links are in a file, else press u and enter to manually provide the urls: " + reset + info_color)
            if method not in ('f','F','u','U'):
                raise ValueError
        except ValueError:
            print(reset + error_color + "Provide a valid input (f or u)" +reset)
            continue
        except KeyboardInterrupt:
            print(reset + error_color + "Exiting..." + reset)
            sys.exit()
        else:
            break

    if method in ('f','F'):
        file = get_file_loc()
        type = get_download_type()
        down_loc = get_download_loc()
        urls = list(open(file))
        system('clear')
        for url in urls:
            return_val = download(url,type,down_loc)
            if return_val[0] == 0:
                completed.append(url)
                print(reset + input_color + "COMPLETE : " + reset + info_color + url + reset)
            else:
                errored.append(url)
                print(reset + error_color + "ERROR : " + reset + info_color + url + reset)
    else:
        url = input(reset + input_color + "Enter the Youtube video url : " + reset + info_color)
        type = get_download_type()
        down_loc = get_download_loc()
        system('clear')
        return_val = download(url,type.lower(),down_loc)
        if return_val[0] == 0:
            completed.append(url)
            print(reset + input_color + "COMPLETE : " + reset + info_color + url + reset)
        else:
            errored.append(url)
            print(reset + error_color + "ERROR : " + reset + info_color + url + reset)
    
    print("total complete : " + str(len(completed)))
    print("total errored : " + str(len(errored)))
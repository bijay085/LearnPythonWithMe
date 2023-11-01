# import a pytube library to download the video
import pytube

# Ask for the url of video
url = input("Enter the url of yt video :")

# specify the storage path of video
path = "D:"

# magic line to download the video
pytube.YouTube(url).streams.get_highest_resolution().download(path)

# cl-coding.com

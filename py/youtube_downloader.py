from pytube import Playlist, YouTube
import time
import os
ending = None #PURELY COSMETIC, VERY USELESS
link = input("What's the video or playlist link?= ")#ask for link
past_time = time.time() #counts elapsed time after asking for link

#define stuff
def download_video():
    """Only downloads a single video."""
    v = YouTube(link)
    v.streams.get_highest_resolution().download(v.title)#downloads video in highest res

def download_playlist():
    """Downloads all items in a playlist"""
    p = Playlist(link) #asks for playlist link and creates Playlist obj
    print(f"You are now downloading {p.title}")
    for v in p:
        try:
            v_obj = YouTube(v)
            print(p.video_urls.index(v) + 1, "of" , len(p.video_urls) , "Downloading: ", v_obj.title, "\n")
            v_obj.streams.get_highest_resolution().download(output_path = p.title) #output folder is created auto
        except:
            print(p.video_urls.index(v_obj)  + 1, "of" , len(p.video_urls) , "This video is skipped because I can't access it. It's probably private or deleted?") #skips priv or del vid

#if the link looks like a playlist link, download_playlist()
#if it looks like a video link, download_video()
#if it doesnt look like anything else, question
if "playlist?list=" in link:
    try:
        download_playlist()
        ending = ". Now you have to tidy them up..."
    except NotADirectoryError:
        print("This playlist doesn't exist...")
        ending = ", sad."
    except:
        print("Something went wrong with your playlist or my code, but I can't put my finger on it...")
        
elif ("watch?v=" in link)  or (link.startswith("www.youtu.be/")):
    try:
        download_video()
        ending = ". The video is in the folder."
    except NotADirectoryError:
        print("This video doesn't exist...")
        ending = ("lol")
    except:
        print("Something went wrong with your video or my code...")

else:
    print("This isn't a video link...")
    ending = ", even though you didn't do anything."
    
#downloading finished, the end
print("You're done! Time elapsed: ", round(time.time() - past_time, 2), "seconds", ending)
input("Press enter to end the program...")


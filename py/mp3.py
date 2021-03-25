import os
import time
import ffmpeg

start = time.time()
list =[f for f in os.listdir(os.getcwd()) if f.endswith(".mp4")]
        
try:
    os.mkdir("audio")
    #makes a folder to put songs
except FileExistsError:
    os.rmdir("audio")
    os.mkdir("audio")

if len(list) <= 0:
    print("There's nothing to convert?")
    
for v in list:
    print(f"Converting {list.index(v) + 1} of {len(list)}: {v}")
    #Converting 6 of 6: The Origami King
    vid = ffmpeg.input(v)
    print(vid)
    aud = vid.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
    print(aud)
    out = ffmpeg.output(aud ,f"{v}.mp3")
    

print("You're done! Time elapsed: ", round(time.time() - start, 2), "seconds")#counts time used
input("Press enter to end...")

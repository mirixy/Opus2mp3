import os
eingabe = ""
eingabe = input("Please type in your Fileformat: ")
fileformat = eingabe
convert2mp3 ='for a in ~/Music/*.' + eingabe + '; do  ffmpeg -i "$a" -qscale:a 0 "${a[@]/%' + eingabe + '/mp3}"; done'

script_out = open("conver2mp3.txt", 'w')
script_out.write(convert2mp3)
script_out.close()
convert = "cp conver2mp3.txt convert2mp3.sh && sudo chmod +x convert2mp3.sh && ./convert2mp3.sh"
os.system(convert)

#! -*- coding: utf-8 -*-
import os


eingabe = ""
eingabe = input("Please type in your Fileformat: ")
print("\n" + ("-" * 50) + "\n")

fileformat = eingabe
convert2mp3 ='#!/bin/bash\n\nfor a in ~/Music/*.' + eingabe + ';\ndo  ffmpeg -hide_banner -i "$a" -qscale:a 0 "${a[@]/%' + eingabe + '/mp3}";\ndone'

script_out = open("conver2mp3.txt", 'w')
script_out.write(convert2mp3)
script_out.close()

convert = "cp conver2mp3.txt convert2mp3.sh && sudo chmod +x convert2mp3.sh && ./convert2mp3.sh"

os.system(convert)

import os
while True:
    os.system("amixer sset Master 0%")
    os.system("amixer sset Master mute")
    os.system("amixer sset Headphone 0%")
    os.system("amixer sset Headphone mute")

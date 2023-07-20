import os
import random
import subprocess

path_wallpaper = "" # path to wallpaper /home/{USER}/path/to/wallpaper
path_file = "" # path to hyprpaper /home/{USER}/path/to/hyprpaper


def wallpaper():
    os.system("pkill hyprpaper")
    random_file = random.choice([f for f in os.listdir(path_wallpaper)])
    with open(path_file, "w") as f:
        f.write(f"preload = {path_wallpaper}{random_file}\nwallpaper = VGA-1,{path_wallpaper}{random_file}")
    subprocess.Popen(["hyprpaper"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     stdin=subprocess.PIPE)


wallpaper()

import os
import random
import subprocess

path_wallpaper = "/home/arcx/wallpaper/"
# path to wallpaper /home/{USER}/path/to/wallpaper
path_file = "/home/arcx/.config/hypr/hyprpaper.conf"
# path to hyprpaper /home/{USER}/path/to/hyprpaper


def wallpaper_next():
    os.system("pkill hyprpaper")

    with open(path_file, "r") as f:
        last_wallpaper = f.readline().strip().split("/")
    list_dir = [i for i in os.listdir(path_wallpaper)]
    last_index_wallpaper = list_dir.index(last_wallpaper[-1])

    if last_index_wallpaper == len(list_dir):
        last_index_wallpaper = 0
    else:
        last_index_wallpaper += 1

    with open(path_file, "w") as f:
        f.write(f"preload = {path_wallpaper}{list_dir[last_index_wallpaper]} \nwallpaper = VGA-1,{path_wallpaper}{list_dir[last_index_wallpaper]}")
    subprocess.Popen(["hyprpaper"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     stdin=subprocess.PIPE)


def wallpaper_random():
    os.system("pkill hyprpaper")
    random_file = random.choice([f for f in os.listdir(path_wallpaper)])
    with open(path_file, "w") as f:
        f.write(f"preload = {path_wallpaper}{random_file} \nwallpaper = VGA-1,{path_wallpaper}{random_file}")
    subprocess.Popen(["hyprpaper"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     stdin=subprocess.PIPE)


wallpaper_next()

import os
import random
import subprocess
import sys

path_wallpaper = "/home/arcx/wallpaper/"
# path to wallpaper /home/{USER}/path/to/wallpaper
path_file = "/home/arcx/.config/hypr/hyprpaper.conf"
# path to hyprpaper /home/{USER}/path/to/hyprpaper


def wallpaper_next(reverse=False):
    os.system("pkill hyprpaper")

    with open(path_file, "r") as f:
        last_wallpaper = f.readline().strip().split("/")
    list_dir = [i for i in os.listdir(path_wallpaper)]
    try:
        last_index_wallpaper = list_dir.index(last_wallpaper[-1])
    except ValueError:
        last_index_wallpaper = random.randint(1, len(os.listdir(path_file)))

    if last_index_wallpaper == len(list_dir):
        last_index_wallpaper = 0
    else:
        if reverse:
            last_index_wallpaper -= 1
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


if __name__ == "__main__":
    if len(sys.argv) == 1:
        wallpaper_next()
    elif 'random' in sys.argv:
        wallpaper_random()
    elif 'true' in sys.argv:
        wallpaper_next(True)
    elif 'help' in sys.argv:
        print("""
random - wallpaper will be randomly selected from the folder
true - wallpaper will be selected back
no argument - wallpaper will be selected forward

""")

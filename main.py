import os
import random
import subprocess
import sys

path_wallpaper = "/home/arcx/wallpaper/"
# path to wallpaper /home/{USER}/path/to/wallpaper
path_file = "/home/arcx/.config/hypr/hyprpaper.conf"
# path to hyprpaper /home/{USER}/path/to/hyprpaper


def write_config(file):
    with open(path_file, "w") as f:
        f.write(f"preload = {path_wallpaper}{file} \nwallpaper = VGA-1,{path_wallpaper}{file}")
    subprocess.Popen(["hyprpaper"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                     stdin=subprocess.PIPE)


def wallpaper_next(file=None):
    os.system("pkill hyprpaper")
    if file:
        image = file.strip().split("/")
        write_config(image[-1])
    else:
        with open(path_file, "r") as f:
            last_wallpaper = f.readline().strip().split("/")
        list_dir = [i for i in os.listdir(path_wallpaper)]
        try:
            last_index_wallpaper = list_dir.index(last_wallpaper[-1])
        except ValueError:
            last_index_wallpaper = 0
        if last_index_wallpaper == len(list_dir):
            last_index_wallpaper = 0
        else:
            last_index_wallpaper += 1
        file = list_dir[last_index_wallpaper]
        write_config(file)


def wallpaper_random():
    os.system("pkill hyprpaper")

    random_file = random.choice([f for f in os.listdir(path_wallpaper)])
    with open(path_file, "r") as f:
        last_wallpaper = f.readline().strip().split("/")
    while random_file == last_wallpaper[-1]:
        random_file = random.choice([f for f in os.listdir(path_wallpaper)])
    write_config(random_file)


def main():
    if len(sys.argv) == 1:
        wallpaper_next()
    elif 'random' in sys.argv:
        wallpaper_random()
    elif 'help' in sys.argv:
        print("""
random - wallpaper will be randomly selected from the folder
""")
    else:
        wallpaper_next(sys.argv[1])


if __name__ == "__main__":
    main()

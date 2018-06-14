import matplotlib
import re
import os
import sys
import shutil

# get config file path

config_file = matplotlib.matplotlib_fname()

# move wenquanyi open source TTF font file in 


if sys.platform == 'win32':
    ttf_font_path = config_file.replace('\\matplotlibrc', '\\fonts\\ttf')
else:
    ttf_font_path = config_file.replace('/matplotlibrc', '/fonts/ttf')

shutil.copy2("wenquanyi-micro-hei.ttf", ttf_font_path)


# clear fontlist

import glob

try:

    dot_matplotlib_path = os.path.expanduser("~/.matplotlib")

    fontlist_files = glob.glob(dot_matplotlib_path+"/fontList*")

    for file in fontlist_files:
        os.remove(file)

    print("Please restart the kernel in Jupyter Notebook and rerun plot command. Enjoy Chinese Display!")

except:

    print('Can not delete font list files in ~/.matplotlib')

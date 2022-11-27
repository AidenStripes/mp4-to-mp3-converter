import os
from moviepy.editor import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="input filename")
parser.add_argument("--output", help="output filename")
args = parser.parse_args()

print('inputfile:', args.input)
print('outputfile:', args.output)

video = VideoFileClip(args.input)
video.audio.write_audiofile(args.output)

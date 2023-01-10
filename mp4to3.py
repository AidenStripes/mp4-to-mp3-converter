from moviepy.editor import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="input filename path", metavar="input")
parser.add_argument("-o", help="output filename path", metavar="output")
args = parser.parse_args()

print('inputfile:', args.i)
print('outputfile:', args.o)

video = VideoFileClip(args.i)
video.audio.write_audiofile(args.o)

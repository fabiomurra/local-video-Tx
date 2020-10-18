'''
	this script will go and look through all video files in a given path and convert them using FFMPEG to a common mezzanine format that is most compatible with all of the entertainment systems in the house
'''

# some variables
videoPathIn = "\\\pippo3\\video\\Kids"							# the path where I'm looking to convert videos --- THIS WILL BE A PARAMETER PASSED AT RUN TIME ---
videoPathOut = videoPathIn & "\\converted"                      # output path. It's a subdir created in the folder where the videos are kept. Be careful, this path will have to be created (if not existent) and excluded from the path search not to get into a recursive situation where output files are converted again. Should it be a unique identifier?
videoExtensionsSupported = [".ts", ".mp4", ".mkv", ".mov"]		# the videos extensions supported
videosInPath = []												# this will be the list of videos I found in path

# libraries and classes to include
from pathlib import Path
import os

# list the content of the current directory
# and extract onto a list the supported videos (i.e. the ones with an extension in the list above)
for videoFile in Path(videoPathIn).iterdir():
	#	print(videoFile.suffix)
	if videoFile.suffix in videoExtensionsSupported:
		print(videoFile.suffix)
		videosInPath.append(videoFile)

print("I found ", len(videosInPath), " supported videos")
print(videosInPath)

# eliminate videoPathOut if present in the list
# if not present create the directory


### << CODE TO BE INSERTED HERE>> ###




# returns the content of the current directory in a list
# as elements WindowsPath
# https://docs.python.org/3/library/pathlib.html
contents = list(Path(videoPathIn).iterdir())



    
# Get the list of all files in directory tree at given path
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(videoPathIn):
	listOfFiles += [os.path.join(dirpath, file) for file in filenames]

# Print the files    
for elem in listOfFiles:
	print(elem)    
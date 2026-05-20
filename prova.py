import pyaudio
from pydub import AudioSegment, playback
from pydub.utils import make_chunks
from io import BytesIO
import wave
import numpy as np
import sys
import os
import threading

class	TonyPythony(threading, Thread):
	def __init__(self, dir = "Tony"):
		super(TonyPythony, self).__init__()
		self.loop = False
		self.mainloop = False
		sound = AudioSegment.from_file(os.path.abspath(dir+"12-si.mp3"), "mp3")
		self.player = pyaudio.pyAudio()

	def run(self):
		print("LESGOO")
		while (self.mainloop):
			try:
				self.going = True
				self.loop = True
				start = 0;
				




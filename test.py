import functools
import tempfile

import threading
import pyaudio
from pydub import AudioSegment, playback
from pydub.utils import make_chunks
from io import BytesIO
import requests
import json
import subprocess
import random
import wave
import numpy as np
import functools
import asyncio
import sys
import os
import glob
# ~ import vlc
import time
import datetime

class input_t(threading.Thread):
	"""
	A simple class based on PyAudio and pydub to play in a loop in the backgound
	"""

	def __init__(self):
		"""
		Initialize `PlayerLoop` class.
		PARAM:
			-- filepath (String) : File Path to wave file.
			-- loop (boolean)    : True if you want loop playback.
								False otherwise.
		"""
		super(input_t, self).__init__()
		self.init = True
		self.timerconta = 0

	def run(self):
		print("input_t started")
		while (True):
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>input_t:")

			time.sleep(1)


class output_t(threading.Thread):
	"""
	A simple class based on PyAudio and pydub to play in a loop in the backgound
	"""

	def __init__(self):
		"""
		Initialize `PlayerLoop` class.
		PARAM:
			-- filepath (String) : File Path to wave file.
			-- loop (boolean)    : True if you want loop playback.
								False otherwise.
		"""
		super(output_t, self).__init__()
		self.init = True
		self.timerconta = 0

	def run(self):
		print("output_t started")
		while (True):
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>output_t:")

			time.sleep(0.1)


print("START EVENTSSSS")


input_thread = input_t()
input_thread.start()
output_thread = output_t()
output_thread.start()

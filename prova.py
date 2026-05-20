import os
import threading
import time

import pyaudio
from pydub import AudioSegment
from pydub.utils import make_chunks

class output_t(threading.Thread):

	def __init__(self, dir = "Tony", loop = True):

		super(output_t, self).__init__()
		self.init = True
		self.timerconta = 0
		self._stop_event = threading.Event()

	def run(self):
		print("output_t started")
		while (not self._stop_event.is_set()):
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>output_t:")

			time.sleep(0.1)

	def stop(self):
		self._stop_event.set()


class TonyPythony(threading.Thread):

	def __init__(self, dir = "Tony"):
		super(TonyPythony, self).__init__()
		self.loop = False
		self.mainloop = False
		self.going = False
		self.goingnow = False
		self.end = False
		self.time = 0
		self.dir = dir
		self.sound = AudioSegment.from_file(
			os.path.abspath(os.path.join(dir, "12-si.mp3")), "mp3")
		self.player = pyaudio.PyAudio()
		self._stop_event = threading.Event()

	def play(self):
		self.loop = True
		self.mainloop = True
		if not self.is_alive():
			self.start()

	def stop(self):
		self.loop = False
		self.mainloop = False
		self._stop_event.set()

	def run(self):
		print("LESGOO")
		while (not self._stop_event.is_set()):
			if not self.mainloop:
				time.sleep(0.05)
				continue
			try:
				self.going = True
				self.loop = True
				start = 0
				sound = self.sound
				length = sound.duration_seconds
				volume = 100.0
				playchunk = sound[start*1000.0:(start+length)
                                  * 1000.0] - (60 - (60 * (volume/100.0)))
				millisecondchunk = 5000 / 1000.0
				stream = self.player.open(
					format=self.player.get_format_from_width(sound.sample_width),
					channels=sound.channels,
					rate=sound.frame_rate,
					frames_per_buffer=8000,
					output=True,
				)
				try:
					while self.loop and not self._stop_event.is_set():
						self.time = start
						for chunks in make_chunks(playchunk, int(millisecondchunk * 1000)):
							if not self.loop or self._stop_event.is_set():
								break
							self.goingnow = True
							self.time += millisecondchunk
							stream.write(chunks._data)
							if (self.time >= start + length):
								if self.end:
									self.loop = False
								break
				finally:
					stream.stop_stream()
					stream.close()
					self.going = False
					self.goingnow = False
					self.mainloop = False
					break
			except Exception as exc:
				print("stream error:", exc)
				self.going = False
				self.goingnow = False
				self.mainloop = False
				break




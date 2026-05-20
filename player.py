class PlayerLoopTones(threading.Thread):
	"""
	A simple class based on PyAudio and pydub to play in a loop in the backgound
	"""

	def __init__(self, fast=0, localp="sonini", occupato="sonini/occupato.mp3"):
		"""
		Initialize `PlayerLoop` class.
		PARAM:
			-- filepath (String) : File Path to wave file.
			-- loop (boolean)    : True if you want loop playback.
								False otherwise.
		"""
		super(PlayerLoopTones, self).__init__()
		self.loop = False
		self.end = False
		self.mainloop = False
		self.occupato_path = occupato
		self.playerind = 0
		self.fast = fast
		sound0 = AudioSegment.from_file(os.path.abspath(localp+"/d0.mp3"), "mp3")
		sound1 = AudioSegment.from_file(os.path.abspath(localp+"/d1.mp3"), "mp3")
		sound2 = AudioSegment.from_file(os.path.abspath(localp+"/d2.mp3"), "mp3")
		sound3 = AudioSegment.from_file(os.path.abspath(localp+"/d3.mp3"), "mp3")
		sound4 = AudioSegment.from_file(os.path.abspath(localp+"/d4.mp3"), "mp3")
		sound5 = AudioSegment.from_file(os.path.abspath(localp+"/d5.mp3"), "mp3")
		# ~ sound6 = AudioSegment.from_file(os.path.abspath(localp+"/d6.mp3"), "mp3")
		# ~ sound7 = AudioSegment.from_file(os.path.abspath(localp+"/d7.mp3"), "mp3")
		# ~ sound8 = AudioSegment.from_file(os.path.abspath(localp+"/d8.mp3"), "mp3")
		# ~ sound9 = AudioSegment.from_file(os.path.abspath(localp+"/d9.mp3"), "mp3")
		# ~ sound10 = AudioSegment.from_file(os.path.abspath(localp+"/d10.mp3"), "mp3")
		# ~ sound11 = AudioSegment.from_file(os.path.abspath(localp+"/d11.mp3"), "mp3")
		# ~ sound12 = AudioSegment.from_file(os.path.abspath(localp+"/d12.mp3"), "mp3")
		# ~ sound13 = AudioSegment.from_file(os.path.abspath(localp+"/d13.mp3"), "mp3")
		if (not (self.fast)):
			sound14 = AudioSegment.from_file(os.path.abspath(localp+"/n0.mp3"), "mp3")
			sound15 = AudioSegment.from_file(os.path.abspath(localp+"/n1.mp3"), "mp3")
			sound16 = AudioSegment.from_file(os.path.abspath(localp+"/n2.mp3"), "mp3")
			sound17 = AudioSegment.from_file(os.path.abspath(localp+"/n3.mp3"), "mp3")
			sound18 = AudioSegment.from_file(os.path.abspath(localp+"/n4.mp3"), "mp3")
			sound19 = AudioSegment.from_file(os.path.abspath(localp+"/n5.mp3"), "mp3")
			sound20 = AudioSegment.from_file(os.path.abspath(localp+"/n6.mp3"), "mp3")
			sound21 = AudioSegment.from_file(os.path.abspath(localp+"/n7.mp3"), "mp3")
			sound22 = AudioSegment.from_file(os.path.abspath(localp+"/n8.mp3"), "mp3")
			sound23 = AudioSegment.from_file(os.path.abspath(localp+"/n9.mp3"), "mp3")
			sound24 = AudioSegment.from_file(os.path.abspath(localp+"/n10.mp3"), "mp3")
			sound25 = AudioSegment.from_file(os.path.abspath(localp+"/n11.mp3"), "mp3")
		sound26 = AudioSegment.from_file(
			os.path.abspath(localp+"/libero.mp3"), "mp3")
		sound27 = AudioSegment.from_file(os.path.abspath(localp+"/ring.mp3"), "mp3")
		sound28 = AudioSegment.from_file(
			os.path.abspath(localp+"/occupato.mp3"), "mp3")

		if (not (self.fast)):
		self.sounds = [sound0, sound1, sound2, sound3, sound4, sound5, sound26, sound28, sound27,
                 sound14, sound15, sound16, sound17, sound18, sound19,
                 sound20, sound21, sound22, sound23, sound24, sound25]
		else:

		self.sounds = [sound0, sound1, sound2, sound3,
                 sound4, sound5, sound26, sound28, sound27]
		self.player = pyaudio.PyAudio()

	def run(self):
		fau_print("xxxxxxxxxxxxxxxxxxxSTREMMXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxx")
		while (True):
			if (self.mainloop):
				fau_print("self.playerind"+str(self.playerind))
				sound = self.sounds[self.playerind]
				try:

					# ~ fau_print("xxxpyaudio:"+str(self.playerind))
					# ~ fau_print("xxZxopen:")
					# ~ fau_print(player.get_default_input_device_info())
					# ~ fau_print("xxZxopenLISA_TAAA:")
					# ~ for i in range(player.get_device_count()):
					# ~ fau_print(player.get_device_info_by_index(i))
					# ~ fau_print("xxxsound:"+str(sound))

					# ~ fau_print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAan:")
					self.going = True

					self.loop = True
					# PLAYBACK LOOP
					start = 0
					# ~ fau_print("xxxduration e chunk:")

					length = sound.duration_seconds
					volume = 100.0
					playchunk = sound[start*1000.0:(start+length)
                                            * 1000.0] - (60 - (60 * (volume/100.0)))
					millisecondchunk = 5000 / 1000.0
					# ~ fau_print("xxxstream loop : GO")
					# ~ fau_print(str(length))
					# ~ fau_print(str(self.end))
					# ~ fau_print(str(self.loop))
					try:
					stream = self.player.open(format=self.player.get_format_from_width(sound.sample_width),
                                            channels=sound.channels,
                                            rate=sound.frame_rate,
                                            frames_per_buffer=8000,
                                            output=True)
					except Exception as e:
						self.player.terminate()
						time.sleep(1)
						self.player = pyaudio.PyAudio()
						stream = self.player.open(format=self.player.get_format_from_width(sound.sample_width),
                                                    channels=sound.channels,
                                                    rate=sound.frame_rate,
                                                    frames_per_buffer=8000,
                                                    output=True)
					try:

						while self.loop:
							self.time = start

							for chunks in make_chunks(playchunk, millisecondchunk*1000):
								self.goingnow = True
								self.time += millisecondchunk
								stream.write(chunks._data)
								if not self.loop:
									break
								if (self.time >= start+length):
									if (self.end):
										self.loop = False
									break
							# ~ if(self.end):
									# ~ self.loop=False
					except Exception as e:
						fau_print("xxxstreamERROR:"+str(e))
					stream.close()
				except Exception as e:
					fau_print("xxxstreamERROR:"+str(e))

				self.going = False

				fau_print("xxxstream close : stopped")
				# ~ player.terminate()
				self.mainloop = False

	def play(self, fp):
		fau_print("xxxplay:"+str(fp))
		if (fp > len(self.sounds)-1):
			fau_print("WARNING NON SUONO : INDICE TROPPO ALTO!!")
			return
		# ~ self.filepath = os.path.abspath(fp)
		self.end = False
		if (fp > 6):
			self.end = True
		self.loop = False
		self.mainloop = True
		self.playerind = fp

	def stop(self):
		"""
		Stop playback.
		"""
		self.loop = False

	def terminate_player(self):
		self.player.terminate()

	def init_new_player(self):
		self.player = pyaudio.PyAudio()


class PlayerLoop(threading.Thread):
	"""
	A simple class based on PyAudio and pydub to play in a loop in the backgound
	"""

	# ~ def __init__(self, path="sonini/n9.mp3", loop=True, occupato="sonini/occupato.mp3"):
	def __init__(self, path="sonini/dopoilbip.mp3", loop=True, occupato="sonini/occupato.mp3"):
		"""
		Initialize `PlayerLoop` class.

		PARAM:
			-- filepath (String) : File Path to wave file.
			-- loop (boolean)    : True if you want loop playback.
								False otherwise.
		"""
		super(PlayerLoop, self).__init__()
		self.loop = loop
		self.iddevice = 1
		self.going = True
		self.goingnow = False
		self.islocal = False
		self.occupato_path = occupato
		self.url = ""
		self.code = ""
		self.dnum = ""
		# ~ path="sonini/d6.mp3"
		# ~ self.soundd = AudioSegment.from_file(path, "mp3")

	def run(self):
		if (self.recmode == 0):
			try:
				player = pyaudio.PyAudio()
				fau_print("play::"+getremote_mainfolder()+"/"+self.url)
				if (not (self.islocal)):
					try:
						res = requests.get(getremote_mainfolder()+"/"+self.url)
						fau_print("play online:"+self.url)
						sound = AudioSegment.from_file(BytesIO(res.content), "mp3")
						set_no_internet(False)
					except Exception as e:
						set_no_internet(True)
						time.sleep(0.5)
						self.end = False
						sound = AudioSegment.from_file(self.occupato_path, "mp3")
						fau_print("play occupato:"+self.occupato_path)

				else:
					# ~ time.sleep(0.5)
					try:
						if (len(self.code) > 0):
							if (len(self.url.split("risp")) > 1):
								fau_print("URL IN LOCALE CON RISP")
							else:
								dirv = self.url.split("/")
								self.url = dirv[0]+"/"+self.code+".mp3"
						fau_print(" play local:"+self.url)
						sound = AudioSegment.from_file(self.url, "mp3")
					except Exception as e:
						try:
							fau_print("is local BUT try play online:"+self.url)
							set_no_internet(False)
							res = requests.get(getremote_mainfolder()+"/"+self.url)
							sound = AudioSegment.from_file(BytesIO(res.content), "mp3")
						except Exception as e:
							fau_print("play occupato2:"+self.occupato_path)
							set_no_internet(True)
							self.end = False
							time.sleep(0.5)
							sound = AudioSegment.from_file(self.occupato_path, "mp3")

						# ~ sound = AudioSegment.from_file(self.filepath, "mp3")
						# ~ fau_print("play local:"+self.url)
				# ~ sound = self.soundd
				# ~ player = self.player;
				# ~ for i in range(player.get_device_count()):
					# ~ fau_print(str(i))
					# ~ fau_print(player.get_device_info_by_index(i))
				try:

					# PLAYBACK LOOP
					start = 0
					length = sound.duration_seconds
					volume = 100.0
					playchunk = sound[start*1000.0:(start+length)
                                            * 1000.0] - (60 - (60 * (volume/100.0)))
					millisecondchunk = 5000 / 1000.0
					self.goingnow = False
					makechuchu = make_chunks(playchunk, millisecondchunk*1000)
					stream = player.open(format=player.get_format_from_width(sound.sample_width),
                                            channels=sound.channels,
                                            rate=sound.frame_rate,
                                            output=True,
                                            start=False)
					fau_print(str(len(makechuchu))
					          + "-______millisecondchunk:"+str(millisecondchunk))
					stream.start_stream()
					fau_print(str(self.end))
					while self.loop:
						self.time = start
						for chunks in makechuchu:
							self.goingnow = True
							stream.write(chunks._data)
							self.time += millisecondchunk
							if (not (self.loop)):
								self.goingnow = False
								break
							if (self.time >= start+length):
								if (self.end):
									self.loop = False
									self.going = False
									self.goingnow = False
								break
					fau_print("stream close : stopped, self.going false")
					self.going = False
					self.loop = True
					stream.close()
					player.terminate()
				except Exception as e:
					set_no_internet(True)
					self.end = False
					time.sleep(0.5)
					sound = AudioSegment.from_file(self.occupato_path, "mp3")
					fau_print("play occupato3:"+self.occupato_path)
			except Exception as e:
				fau_print("play occupato3:"+str(e))

		elif (self.recmode == 1):
			LED_ACCENDI(0)
			LED_VELOCITI(0, 2)
			fau_print("self.dnum")
			fau_print(self.dnum)

			cartella = "records"
			if (len(self.dnum) > 0 and ("s" in self.dnum) and not ("risp" in self.dnum)):
				cartella = "secret"
			fau_print("....cartella")
			fau_print(cartella)

			timestr = "tmpwav_"+time.strftime("%Y%m%d-%H%M%S")
			timestrwav = timestr+".wav"

			RESPEAKER_RATE = 48000
			RESPEAKER_CHANNELS = 1
			RESPEAKER_WIDTH = 2
			# run getDeviceInfo.py to get index
			RESPEAKER_INDEX = 2  # refer to input device id
			CHUNK = 2048
			WAVE_OUTPUT_FILENAME = timestrwav

			p = pyaudio.PyAudio()
			self.iddevice = 1
			try:
				for i in range(p.get_device_count()):
				 # ~ fau_print(p.get_device_info_by_index(i))
					dev = p.get_device_info_by_index(i)
					fau_print("------------>"+dev["name"])
					if ("AB13X USB Audio" in dev["name"]):
						self.iddevice = dev["index"]
						fau_print("ID DEVICE CORRETTO------------>"+str(self.iddevice))
			except Exception as e:
				fau_print("-------errorrrr----->")
			stream = p.open(
						rate=RESPEAKER_RATE,
						format=p.get_format_from_width(RESPEAKER_WIDTH),
						channels=RESPEAKER_CHANNELS,
						input=True,
						input_device_index=self.iddevice)

			set_registra(True)
			fau_print("**** recording")

			frames = []
			x = 0
			try:
				while (get_registra()):
					data = stream.read(CHUNK, exception_on_overflow=False)

					# extract channel 0 data from 2 channels, if you want to extract channel 1, please change to [1::2]
					a = np.frombuffer(data, dtype=np.int16)[0::2]
					frames.append(a.tobytes())
					# registra=premuto();
				# frames=audio_datalist_set_volume(frames, 0.1)

				fau_print("*++++ done recording")
				stream.stop_stream()
				stream.close()
				LED_VELOCITI(0, 0)
			except Exception as e:
				fau_print("---- error recording:"+str(e))
				LED_VELOCITI(0, 4)

			time.sleep(1.5)
			# ~ LED_SPENGI(0)
			# ~ LED_SPENGI(0)
			try:
				wf = wave.open(cartella+"/"+WAVE_OUTPUT_FILENAME, 'wb')
				wf.setnchannels(1)
				wf.setsampwidth(p.get_sample_size(
					p.get_format_from_width(RESPEAKER_WIDTH)))
				wf.setframerate(RESPEAKER_RATE/2)
				wf.writeframes(b''.join(frames))
				wf.close()
				if (len(self.dnum) > 0):
					newname = self.dnum
				else:
					newname = new_for_elenco("")
				os.system("ffmpeg -i "+cartella+"/"+timestrwav
                                    + " -vn -ar 44100 -ac 2 -b:a 192k "+cartella+"/"+newname+".mp3")
				os.system('rm -f '+cartella+'/tmpwav_*.wav')
				p.terminate()

				fau_print("finito di comprimere REC FILE")
				salva_nome_ultimaregistrata(newname)
				# ~ fil=get_not_uploaded("records")
				# ~ fau_print("UPLOAD "+fil)
				LED_SPENGI(0)
			except Exception as e:
				LED_VELOCITI(0, 4)

			# ~ ~ LED_SPENGI(0)
				# ~ LED_ACCENDI(0)
				# ~ LED_VELOCITI(0,3)
			put_on_elenco_local(newname, cartella)
			go_transfert_thread()
			# ~ upload_if_internet(fil)

	def getname_and_play(self, url, code, end=False, islocal=False):
		LED_ACCENDI(3)
		LED_SPENGI(2)
		os.system("amixer sset Master 100%")
		os.system("amixer sset Capture 30%")

		fau_print("get name and play url:"+url)
		self.url = url
		self.code = code
		self.islocal = islocal
		self.end = end
		self.recmode = 0
		self.loop = True
		self.start()

	def play(self, fp, end=False):
		"""
		Just another name for self.start()
		"""
		# ~ ~ LED_SPENGI(0)
		# ~ LED_ACCENDI(0)
		# ~ LED_VELOCITI(0,3)

		# ~ self.url = os.path.abspath(fp)
		self.url = fp
		self.end = end
		self.recmode = 0
		self.loop = True
		self.going = True
		self.islocal = True
		self.code = ""

		self.start()
		self.goingnow = False

	def rec(self, dnum=""):
		"""
		Just another name for self.start()
		"""
		self.recmode = 1
		self.start()
		self.dnum = dnum

	def stop(self):
		"""
		Stop playback.
		"""
		self.loop = False

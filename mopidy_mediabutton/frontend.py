import pykka
from threading import Thread
import logging
import traceback
from button_watcher import ButtonWatcher

from mopidy import core
logger = logging.getLogger(__name__)

class MediaButtonFrontend(pykka.ThreadingActor, core.CoreListener):
	def __init__(self, config, core):
		super(MediaButtonFrontend, self).__init__()
		logger.info('MediaButton Frontend init.')
		self.core = core
		self.config = config
		self.running = False

	def start_thread(self):
		self._button_watcher = ButtonWatcher("BT005",self.config, self.core)
		while self.running:
			self._button_watcher.watch_buttons()

	def on_start(self):
		try:
			logger.info('Start MediaButton Frontend')
			self.running = True
			thread = Thread(target=self.start_thread)
			thread.start()
		except:
			traceback.print_exc()

	def on_stop(self):
		logger.info('Stopping MediaButton Frontend')
		self.running = False

	def track_playback_started(self, tl_track):
		try:
			logger.info('Track playback started')
		except:
			traceback.print_exc()

	def volume_changed(self, volume):
		logger.info('Volume changed')

	def playback_state_changed(self, old_state, new_state):
		logger.info('Track playback state changed')

	def tracklist_changed(self):
		try:
			logger.info('Tracklist changed')
		except:
			traceback.print_exc()

	def track_playback_ended(self, tl_track, time_position):
		logger.info('Track playback ended')

	def options_changed(self):
		try:
			logger.info('Options changed')
		except:
			traceback.print_exc()

	def playlists_loaded(self):
		logger.info('Playlists loaded')
		if self._button_watcher:
			self._button_watcher.playlists_loaded()
		#self.screen_manager.playlists_loaded()

	def stream_title_changed(self, title):
		logger.info('Stream title changed')
		if self._button_watcher:
			self._button_watcher.stream_title_changed(title)
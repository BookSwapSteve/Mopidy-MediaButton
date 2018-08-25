import sys
import os
import evdev

import logging

logger = logging.getLogger(__name__)
from mopidy import backend, exceptions

from mopidy.core import PlaybackState

watched_keys = {"KEY_PLAYPAUSE": "playpause",
                "KEY_NEXTSONG": "next",
                "KEY_PREVIOUSSONG": "previous",
                "KEY_VOLUMEUP": "volume/+2",
                "KEY_VOLUMEDOWN": "volume/-2"}

class ButtonWatcher:
	def __init__(self, button_name, config, core):
		self.config = config
		self.core = core
		self._button_name = button_name  # "BT005"

	def watch_buttons(self):
		# We well repeatedly enter watch_buttons if the button/keyboard has disconnected
		# as happens after x minutes with the bluetooth button.
		logger.info('Mediabutton waiting for button press. Button: {}'.format(self._button_name))

		try:
			# Get all the input devices
			devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

			# Itterate the devices until we find the one we want.
			# Note: It's possible to have multiple devices with the same name so
			# we may need a better differentiator.
			for device in devices:
				# print(device.path, device.name, device.phys)
				if device.name == self._button_name:
					logger.info("Button found: {}".format(device.name))

					# Grab the device and keep reading on a loop for events.
					# not really needed as we don't need to be the only receipient.
					# device.grab()

					# See: https://python-evdev.readthedocs.io/en/latest/tutorial.html
					# read_loop or just read (useful for multiple devices)
					for event in device.read_loop():
						if event.type == evdev.ecodes.EV_KEY:
							data = evdev.categorize(event)  # Save the event temporarily to introspect it

							if data.keystate == 1:  # Down events only
								self.handle_button_press(data)


		except Exception, e:
			logger.warn("Lost keyboard connection. Restarting search")
			pass

	def handle_button_press(self, data):
		try:
			if data.keycode == "KEY_VOLUMEUP":
				logger.info("Volume Up")
				volume = self.core.mixer.get_volume().get()
				if volume == None:
					return

				volume = volume + 1
				if volume > 100:
					volume = 100
				self.core.mixer.set_volume(volume)

			elif data.keycode == "KEY_VOLUMEDOWN":
				logger.info("Volume Down")
				volume = self.core.mixer.get_volume().get()
				logger.info("Current volume: {}".format(volume))

				if volume == None:
					return

				volume = volume - 1
				if volume < 0:
					volume = 0
				self.core.mixer.set_volume(volume)

			elif data.keycode == "KEY_PLAYPAUSE":
				logger.info("Play/Payse")

				state = self.core.playback.get_state().get()

				if state ==  PlaybackState.PLAYING:
					self.core.playback.pause()
				elif state ==  PlaybackState.PAUSED:
					self.core.playback.resume()
				elif state == PlaybackState.STOPPED:
					logger.info("TODO: Start playing")
				else:
					logger.warn("Unknown playback state: {0}".format(state))

			else:
				logger.info("Unhandled Keycode: {}".format(data.keycode))
		# PlaybackController.next()
		# PlaybackController.previous()

		# if data.keycode in watched_keys:
		#	logger.info("Button pressed: {}".format(data.keycode))
		except Exception, e:
			logger.warn(e)
			logger.exception("Error handling key press")


	def playlists_loaded(self):
		logger.info('Playlists loaded')

	def stream_title_changed(self, title):
		logger.info('stream title changed')
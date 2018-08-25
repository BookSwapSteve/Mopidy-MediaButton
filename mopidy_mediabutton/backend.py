from __future__ import unicode_literals

import logging
from mopidy import backend, exceptions

import pykka

logger = logging.getLogger(__name__)

class MediaButtonBackend (
        pykka.ThreadingActor, backend.Backend):

    def __init__(self, config, audio):
        super(MediaButtonBackend, self).__init__()

        self.config = config

        self._default_playlist = config['mediabutton']['default_playlist']
        self._button_name = config['mediabutton']['button_name']

        self.uri_schemes = ['mediabutton']

    def on_start(self):
        # Create the button watcher.
        logger.info('Start MediaButton Backend')

    def on_stop(self):
        logger.info('Stopping MediaButton Backend')
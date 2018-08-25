from __future__ import unicode_literals

import os

from mopidy import config, ext

__version__ = '0.1.0'

class MediaButtonExtension(ext.Extension):

    dist_name = 'Mopidy-MediaButton'
    ext_name = 'mediabutton'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(MediaButtonExtension, self).get_config_schema()

        schema['default_playlist'] = config.String()
        schema['button_name'] = config.String()


        return schema

    def setup(self, registry):
        from .backend import MediaButtonBackend
        registry.add('backend', MediaButtonBackend)
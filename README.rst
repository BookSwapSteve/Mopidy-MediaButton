******************
Mopidy-MediaButton
******************

Dependencies
============

You must have a media button (BT005)

- Bluetooth must be enabled on your device

- The media button needs to be paired with the device.


Installation
============

Install the Mopidy-MediaButton extension by running::

    pip install mopidy-mediabutton


Configuration
=============

If no music is paused/playing, pressing play on the media button will play the default_playlist defined in the configuraiton

    [mediabutton]
    default_playlist = PressPlayOnMediaButton
    button_name = BT005



Usage
=====

The extension is enabled by default if all dependencies are
available. 



Project resources
=================

- `Source code <https://github.com/BookSwapSteve/Mopidy-MediaButton>`_
- `Issue tracker <https://github.com/BookSwapSteve/Mopidy-MediaButton/issues>`_


Credits
=======

- Original author: `Stephen Harrison <https://github.com/BookSwapSteve>`_
- Current maintainer: `Stephen Harrison <https://github.com/BookSwapSteve>`_
- `Contributors <https://github.com/BookSwapSteve/Mopidy-MediaButton/graphs/contributors>`_


Changelog
=========

v0.1 (2018-08-25)
-----------------

- Initial release
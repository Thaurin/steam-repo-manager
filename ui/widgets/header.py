import os
from pathlib import Path
from gi.repository import Gtk
from utils import clear_installed_videos
from utils import movies_path, startup_file
from ui.widgets.playback_interface import PlaybackInterface

class Header(Gtk.Box):
    def clear_videos(self, _=None):
        clear_installed_videos()
        self.play_installed_button.set_sensitive(False)
        dialog = Gtk.MessageDialog(
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Success ! Reboot your device, default boot video should be back.",
        )
        dialog.run()
        dialog.destroy()

    @staticmethod
    def play_installed_video(_, installed_video_path):
        PlaybackInterface("file://" + installed_video_path)

    def enable_play_installed_button(self, is_enabled):
        print('enable_play_installed_button() was called')
        self.play_installed_button.set_sensitive(is_enabled)

    def __init__(self):
        super(Header, self).__init__()
        self.original_label = "Clear installed videos"

        self.clear_button = Gtk.Button(label=self.original_label)
        self.clear_button.connect("clicked", self.clear_videos)
        self.clear_button.set_margin_left(20)
        self.add(self.clear_button)

        installed_video_path = os.path.join(Path(movies_path), startup_file)
        self.play_installed_button = Gtk.Button(label="Play installed video")
        self.play_installed_button.connect('clicked', self.play_installed_video, installed_video_path)
        self.play_installed_button.set_margin_left(6)

        if not os.path.exists(installed_video_path):
            self.enable_play_installed_button(False)

        self.add(self.play_installed_button)

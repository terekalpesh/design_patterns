from abc import ABC, abstractmethod

# Old interface that we need to adapt
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type: str, file_name: str):
        pass

# The new interface that needs to be adapted
class AdvancedMediaPlayer(ABC):
    @abstractmethod
    def play_vlc(self, file_name: str):
        pass

    @abstractmethod
    def play_mp4(self, file_name: str):
        pass

# Concrete implementation of the old MediaPlayer
class AudioPlayer(MediaPlayer):
    def play(self, audio_type: str, file_name: str):
        if audio_type == "mp3":
            print(f"Playing mp3 file: {file_name}")
        else:
            print(f"Invalid audio type: {audio_type}")

# Concrete implementation of the new AdvancedMediaPlayer (can play VLC and MP4)
class MediaAdapter(AdvancedMediaPlayer):
    def __init__(self, media_type: str):
        if media_type == "vlc":
            self.advanced_music_player = VlcPlayer()
        elif media_type == "mp4":
            self.advanced_music_player = Mp4Player()

    def play_vlc(self, file_name: str):
        self.advanced_music_player.play_vlc(file_name)

    def play_mp4(self, file_name: str):
        self.advanced_music_player.play_mp4(file_name)

# Implement the actual VLC and MP4 players
class VlcPlayer(AdvancedMediaPlayer):
    def play_vlc(self, file_name: str):
        print(f"Playing VLC file: {file_name}")

    def play_mp4(self, file_name: str):
        pass

class Mp4Player(AdvancedMediaPlayer):
    def play_vlc(self, file_name: str):
        pass

    def play_mp4(self, file_name: str):
        print(f"Playing MP4 file: {file_name}")

# Using the Adapter Pattern
class AudioPlayerWithAdapter(MediaPlayer):
    def __init__(self):
        self.adapter = None

    def play(self, audio_type: str, file_name: str):
        if audio_type == "mp3":
            print(f"Playing mp3 file: {file_name}")
        elif audio_type in ["vlc", "mp4"]:
            self.adapter = MediaAdapter(audio_type)
            if audio_type == "vlc":
                self.adapter.play_vlc(file_name)
            elif audio_type == "mp4":
                self.adapter.play_mp4(file_name)
        else:
            print(f"Invalid audio type: {audio_type}")

# Example usage:
player = AudioPlayerWithAdapter()
player.play("mp3", "song.mp3")
player.play("vlc", "movie.vlc")
player.play("mp4", "video.mp4")
player.play("avi", "file.avi")

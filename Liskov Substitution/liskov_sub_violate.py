class MediaPlayer:
    def play(self):
        pass

class AudioPlayer(MediaPlayer):
    def play(self):
        print("Playing audio")

class VideoPlayer(MediaPlayer):
    def play(self):
        print("Playing video")

class MediaClient:
    def play_media(self, player):
        player.play()

# Usage
client = MediaClient()
audio_player = AudioPlayer()
video_player = VideoPlayer()
client.play_media(audio_player)  # Output: Playing audio
client.play_media(video_player)  # Output: Playing video

# Now, let's say we want to add a new player type called StreamPlayer. We can create a new class StreamPlayer and inherit from MediaPlayer.

# Adding a new player that violates LSP. we can not use the subclass PhotoViewer as it does not implement the play method.
class PhotoViewer(MediaPlayer):
    def play(self):
        raise NotImplementedError("Cannot play photos")


photo_viewer = PhotoViewer()
client.play_media(photo_viewer)  # Raises NotImplementedError

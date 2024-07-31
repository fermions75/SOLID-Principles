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

# Creating a separate hierarchy for PhotoViewer to adhere to LSP
class Viewer:
    def view(self):
        pass

class PhotoViewer(Viewer):
    def view(self):
        print("Viewing photo")

class ViewerClient:
    def view_media(self, viewer):
        viewer.view()

# Usage
viewer_client = ViewerClient()
photo_viewer = PhotoViewer()
viewer_client.view_media(photo_viewer)  # Output: Viewing photo
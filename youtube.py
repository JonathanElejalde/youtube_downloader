import os

from pytube import YouTube, Playlist, exceptions
from pydub import AudioSegment
from pathlib import Path


class Downloader:
    """
    Class to download python videos and playlist.
    It uses pytube library
    """

    def __init__(self, link, video=None, audio=None, playlist=None, quality='highest', convert=True):
        self.video = video
        self.audio = audio
        self.playlist = playlist
        self.quality = quality
        self.youtube = Playlist(link) if playlist else YouTube(link)
        self.download_path = './downloads/'
        self.convert = convert

    def _download_video(self, video):
        if self.quality == 'highest':
            
            download = video.streams.filter(progressive=True).get_highest_resolution()
            print('Downloading highest resolution')
        
        else:
            download = video.streams.filter(progressive=True, res=self.quality, subtype='mp4')
            if len(download) == 0:
                print('Quality specified is not present, downloading highest resolution available')
                download = video.streams.filter(progressive=True).get_highest_resolution()
            else:
                print('Quality specified was found, downloading')
                download = download.first()

        download.download(output_path=self.download_path)

    def _download_audio(self, video, convert):
        audio = video.streams.filter(only_audio=True, subtype='mp4').first()
        print('Downloading audio file')
        if convert:
            path = audio.download()
            path = Path(path)
            audio_path = path.name
            filename = path.stem
            audiomp3 = AudioSegment.from_file(audio_path)
            audiomp3.export(self.download_path + filename + '.mp3', format='mp3')
            os.remove(audio_path)
        else:
            audio.download(output_path=self.download_path, filename_prefix='only_audio')

    def _download_playlist(self):
        for video in self.youtube.videos:
            try:
                if self.audio:
                    self._download_audio(video, self.convert)
                if self.video:
                    self._download_video(video)
            except exceptions.VideoUnavailable:
                print(f'Video {url} is unavailable, skipping')

    def download(self):
        if self.playlist:
            self._download_playlist()
        else:
            video = self.youtube
            if self.audio:
                self._download_audio(video, self.convert)
            if self.video:
                self._download_video(video)

    def get_resolutions(self):
        streams = self.youtube.streams.filter(progressive=True)
        resolutions = [stream.resolution for stream in streams]
        return resolutions

if __name__ == "__main__":
    pass
# Youtube Downloader

### Description

Download videos or entire playlists from youtube.    
You can specify if you want only audio, the video or both in separated files.

## Getting Started

It uses a simple UI created with streamlit, where you can follow the steps pretty easily.

- Choose between downloading a video or a playlist
- Add the link
- Choose a download type. You could download the normal youtube vide, only the audio or both.
- Choose a quality for the video
- Hit the "Download" button
- Wait 

#### Note:  
- If you are downloading a playlist, these options apply to every link
- If the resolution is not available, it will download the highest


### Install
```console
git clone https://github.com/JonathanElejalde/youtube-downloader.git
pip install -r requirements.txt
```

#### Important

Because the app converts the mp4 audio to mp3 using pydub, you also are going to  
need the download of **ffmpeg**

### Usage

Once we have installed everything, we can just run this command
```console
streamlit run app.py
```

## License

This project is licensed under the [MIT License](https://github.com/this/project/blob/master/LICENSE)

## Motivation

I wanted to download some coding tutorials to be able to watch them offline. Also, it is a good way to practice my python skills and use *streamlit* which is a new tool that I trying to learn
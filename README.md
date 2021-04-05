# Youtube Downloader

### Description

Download videos or entire playlists from youtube.    
You can specify if you want only audio, the video or both in separated files.

## Getting Started

It uses a simple UI created with streamlit, where you can follow the steps pretty easily.

- Choose between downloading a video or a playlist
- Add the link
- Choose a download type. You could download the normal youtube video, only the audio or both.
- Choose a quality for the video
- Hit the "Download" button
- Wait 

#### Note:  
- If you are downloading a playlist, these options apply to every link
- If the resolution is not available, it will download the highest

### Install with docker
```console
git clone https://github.com/JonathanElejalde/youtube_downloader.git
cd youtube_downloader
docker build -t youtube:1.0 .
docker run --name youtube_downloader -p 8501:8501 -v $(pwd)/downloads:/home/youtube_downloader/downloads/ youtube:1.0
```

### Usage with docker

Now you can access the app on `http://localhost:8501/`.

The next time that you need to start the app, you can use the following command:     
`docker start -i youtube_downloader`, then we can access the app on `http://localhost:8501/`.


### Install without docker
```console
git clone https://github.com/JonathanElejalde/youtube_downloader.git
cd youtube_downloader
pip install -r requirements.txt
```
#### Important

Because the app converts the mp4 audio to mp3 using pydub, you're going to  
need **ffmpeg**. However, you can decide not to convert to mp3  
and avoid this download. For this, you just need to pass `convert=False` when  
instantiating the Downloader object.

You change this code in `app.py` line `59`

```python
# Change this
downloader = Downloader(link, video=video, audio=audio, playlist=playlist, quality=quality)
# For this
downloader = Downloader(link, video=video, audio=audio, playlist=playlist, quality=quality, convert=False)
```

### Usage

Once you have installed everything, you can just run this command
```console
streamlit run app.py
```

## License

This project is licensed under the [MIT License](https://github.com/this/project/blob/master/LICENSE)

## Motivation

I wanted to download some coding tutorials to be able to watch them offline. Also, it is a good way to practice my python skills and use *streamlit* which is a new tool that I trying to learn
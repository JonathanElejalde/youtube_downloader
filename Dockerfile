FROM python:3.8-buster

# streamlit-specific commands
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

# exposing default port for streamlit
EXPOSE 8501

ADD . /home/youtube_downloader/

WORKDIR /home/youtube_downloader/

RUN apt update -y && apt install ffmpeg -y

RUN pip install -r requirements.txt

CMD [ "streamlit", "run", "app.py" ]

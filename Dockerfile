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

WORKDIR /home/youtube_downloader/

COPY ./requirements.txt ./

RUN pip install -r requirements.txt && rm requirements.txt

RUN apt update -y && apt install ffmpeg -y

ADD . .

CMD [ "streamlit", "run", "app.py" ]

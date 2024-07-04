import streamlit as st
from pytube import YouTube

st.title('YouTube Video Download')


video_url = st.text_input('Insira o link do vídeo do YouTube')


def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        return True, f'Download do video: {stream.title} feito com sucesso!'
    except Exception as e:
        return False, f'Erro no  download do video: {str(e)}'


if st.button('Download Video'):
    success, message = download_video(video_url)
    if success:
        st.success(message)
    else:
        st.error(message)

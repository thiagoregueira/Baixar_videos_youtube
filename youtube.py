import os  # noqa: I001, F401
from io import BytesIO

import streamlit as st
from pytube import YouTube


def get_video_streams(url):
    yt = YouTube(url)
    streams = yt.streams.get_highest_resolution()
    return streams


def download_video(stream):
    buffer = BytesIO()
    stream.stream_to_buffer(buffer)
    buffer.seek(0)
    return buffer


st.title('YouTube Download Videos')

# Input URL
url = st.text_input('Digite o endereço do vídeo:')

if url:
    try:
        streams = get_video_streams(url)

        if st.button('Download Buffer'):
            with st.spinner('Downloading...'):
                video_buffer = download_video(streams)
                st.download_button(
                    label='Download Video',
                    data=video_buffer,
                    file_name=f'{streams.title}.mp4',
                    mime='video/mp4',
                )
                st.success(
                    'Download pronto! Clique no botão acima para baixar o vídeo.'  # noqa: E501
                )
    except Exception as e:
        st.error(f'Error: {e}')

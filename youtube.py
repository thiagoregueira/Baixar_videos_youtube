import os

import streamlit as st
from pytube import YouTube


def get_video_streams(url):
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, file_extension='mp4').all()
    return streams


def download_video(stream, output_path):
    stream.download(output_path)


def get_download_path():
    if os.name == 'nt':  # Windows
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    else:  # Linux and other Unix-like systems
        return os.path.join(os.path.expanduser('~'), 'Downloads')


st.title('YouTube Video Downloader')

# Input URL
url = st.text_input('Enter YouTube URL:')

if url:
    try:
        streams = get_video_streams(url)
        quality_options = [
            f'{stream.resolution} - {stream.fps}fps' for stream in streams
        ]

        # Select quality
        quality = st.selectbox('Select Quality:', quality_options)

        # Find the selected stream
        selected_stream = next(
            stream
            for stream in streams
            if f'{stream.resolution} - {stream.fps}fps' == quality
        )

        if st.button('Download'):
            with st.spinner('Downloading...'):
                download_path = get_download_path()
                download_video(selected_stream, download_path)
                st.success(
                    f'Download completed! File saved to {download_path}'
                )
    except Exception as e:
        st.error(f'Error: {e}')

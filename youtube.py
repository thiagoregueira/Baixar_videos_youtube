import os  # noqa: I001, F401
from io import BytesIO

import streamlit as st
from pytube import YouTube


def get_video_streams(url):
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, file_extension='mp4').all()
    return streams


def download_video(stream):
    buffer = BytesIO()
    stream.stream_to_buffer(buffer)
    buffer.seek(0)
    return buffer


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
                video_buffer = download_video(selected_stream)
                st.download_button(
                    label='Download Video',
                    data=video_buffer,
                    file_name=f'{selected_stream.title}.mp4',
                    mime='video/mp4',
                )
                st.success(
                    'Download ready! Click the button above to download the video.'  # noqa: E501
                )
    except Exception as e:
        st.error(f'Error: {e}')

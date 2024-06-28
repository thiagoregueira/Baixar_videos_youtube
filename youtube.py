import streamlit as st
from pytube import YouTube


def get_video_streams(url):
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, file_extension='mp4').all()
    return streams


def download_video(stream, output_path='downloads'):
    stream.download(output_path)


st.title('YouTube Video Downloader')


url = st.text_input('Enter YouTube URL:')

if url:
    try:
        streams = get_video_streams(url)
        quality_options = [
            f'{stream.resolution} - {stream.fps}fps' for stream in streams
        ]

        quality = st.selectbox('Select Quality:', quality_options)

        selected_stream = next(
            stream
            for stream in streams
            if f'{stream.resolution} - {stream.fps}fps' == quality
        )

        if st.button('Download'):
            with st.spinner('Downloading...'):
                download_video(selected_stream)
                st.success('Download completed!')
    except Exception as e:
        st.error(f'Error: {e}')

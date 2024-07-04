import io

import streamlit as st
from pytube import YouTube

st.title('YouTube Video Download')

video_url = st.text_input('Insira o link do vídeo do YouTube:')


def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        # Baixa o vídeo para um buffer em memória
        buffer = io.BytesIO()
        stream.stream_to_buffer(buffer)
        buffer.seek(0)

        return True, buffer, stream.title
    except Exception as e:
        return False, None, f'Erro no download do video: {str(e)}'


if st.button('Download Video'):
    success, buffer, message = download_video(video_url)
    if success:
        st.download_button(
            label='Baixar Vídeo',
            data=buffer,
            file_name=f'{message}.mp4',
            mime='video/mp4',
        )
        st.success(f'Download do video: {message} feito com sucesso!')
    else:
        st.error(message)

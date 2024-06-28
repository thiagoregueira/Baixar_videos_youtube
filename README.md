# YouTube Video Downloader

Este é um aplicativo web simples desenvolvido com Python e Streamlit que permite aos usuários baixar vídeos do YouTube em diferentes qualidades. O aplicativo está atualmente em produção e pode ser acessado através do seguinte endereço: [https://videosyoutube.streamlit.app/](https://videosyoutube.streamlit.app/)

## Funcionalidades

- **Entrada de URL do YouTube**: Os usuários podem inserir a URL do vídeo do YouTube que desejam baixar.
- **Seleção de Qualidade**: O aplicativo lista todas as qualidades disponíveis para o vídeo e permite que o usuário selecione a qualidade desejada.
- **Download do Vídeo**: Após selecionar a qualidade, o usuário pode clicar no botão de download para baixar o vídeo.
- **Download Direto**: O vídeo é baixado diretamente para o dispositivo do usuário.

## Como Usar

1. **Acesse o Aplicativo**: Vá para [https://videosyoutube.streamlit.app/](https://videosyoutube.streamlit.app/).
2. **Insira a URL do YouTube**: No campo de entrada, cole a URL do vídeo do YouTube que você deseja baixar.
3. **Selecione a Qualidade**: Escolha a qualidade do vídeo na lista de opções disponíveis.
4. **Baixe o Vídeo**: Clique no botão "Download" para bufferizar o video e depois clique em Downloado do Video.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas: `streamlit`, `pytube`

## Instalação
```bash
1. Clone o repositório:
2. Crie um ambiente virtual e ative-o:
    
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    

3. Instale as dependências:
    
    pip install -r requirements.txt


4. Execute o aplicativo:
    
    streamlit run youtube.py


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a Licença MIT.


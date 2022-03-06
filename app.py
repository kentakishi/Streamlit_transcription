from google.cloud import speech
import io
import streamlit as st

import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='secret.json'


def transcribe_file(content,lang='Japanese'):
    lang_code={
        "English":"en-US",
        "Japanese":"ja-JP",
        "Korean":"kr-KR",
        "French":"fr-FR",
        "Portuguese":"pt-PT"}
    client = speech.SpeechClient()

#    with io.open(speech_file,'rb') as f:
#        content=f.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        language_code=lang_code[lang],
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        st.write(result.alternatives[0].transcript)
#        print("Transcript: {}".format(result.alternatives[0].transcript))

st.title('Speech to Text App')
st.header('Summary')
st.text('This is the app to create transcribe from the audio source. Below is the link')
st.markdown('<a href="https://cloud.google.com/speech-to-text/docs/">Cloud Speech-To-Text</a>', unsafe_allow_html=True)

upload_file = st.file_uploader("Upload File", type=['mp3','wav'])
if upload_file is not None:
    content = upload_file.read()
    st.subheader('File information')
    file_details = {
        'FileName':upload_file.name,'FileType':uload_file.type,'FileSize':upload_file.size}
    st.write(file_details)
    st.subheader('Play music')
    st.audio(content)
    
    st.subheader('Select Language')
    option = st.selectbox('Select source language', ('English','French','Portuguese','Japanese','Korean'))
    st.write('Selected Language',option)
    st.write('Transcription')
    if st.button('Start'):
        comment= st.empty()
        comment.write('Start transcription')
        transcribe_file(content,lang=option)
        comment.write('Finished')
        
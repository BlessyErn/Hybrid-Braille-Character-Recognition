import streamlit as st
import cv2
import numpy as np
from gtts import gTTS
import tempfile
import os
from PIL import Image
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Braille mapping dictionary (not used in this version)
BRAILLE_MAP = {
    '100000': 'a', '110000': 'b', '100100': 'c', '100110': 'd', '100010': 'e',
    '110100': 'f', '110110': 'g', '110010': 'h', '010100': 'i', '010110': 'j',
    '101000': 'k', '111000': 'l', '101100': 'm', '101110': 'n', '101010': 'o',
    '111100': 'p', '111110': 'q', '111010': 'r', '011100': 's', '011110': 't',
    '101001': 'u', '111001': 'v', '010111': 'w', '101101': 'x', '101111': 'y',
    '101011': 'z', '000000': ' ', '001111': '.', '000011': ',', '000101': '?'
}

def text_to_speech(text, lang='en'):
    """Convert text to speech and return audio file path"""
    if not text.strip():
        return None
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        tts.save(audio_file.name)
        return audio_file.name
    except Exception as e:
        logger.error(f"Text-to-speech failed: {str(e)}")
        return None

# Streamlit UI
st.title("Braille Recognition Plartform")
st.markdown("Upload your document to start conversion")

uploaded_file = st.file_uploader("Choose a document image:", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    # Immediately display feedback message
    feedback_message = "Hello, your document needs work. But the model is a success. What a triumph. Congradulations University of Zimbabwe Student!"
    st.warning(feedback_message)
    
    # Convert feedback message to speech
    feedback_audio_path = text_to_speech(feedback_message)
    if feedback_audio_path:
        st.audio(feedback_audio_path, format='audio/mp3')
        try:
            os.unlink(feedback_audio_path)
        except:
            pass
    
    # Display the uploaded image (optional)
    st.image(uploaded_file, caption="Your uploaded document", use_column_width=True)

# Add instructions
st.sidebar.markdown("**Instructions:**")
st.sidebar.write("- Upload any document image")
st.sidebar.write("- You'll receive immediate feedback")
st.sidebar.write("- No image processing is performed")

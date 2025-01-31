import streamlit as st
import requests

# Streamlit UI setup
st.title("Speech-to-Text Transcription")
st.write("Upload an audio file and get the transcribed text using the Whisper API.")

# Input fields for the API endpoint and API key
api_url = st.secrets["api_url"]
api_key = st.secrets["api_key"]
# Upload audio file
uploaded_file = st.file_uploader("Upload an audio file (e.g., .mp3, .wav, .m4a)", type=["mp3", "wav", "m4a"])

if uploaded_file and api_key and api_url:
    st.audio(uploaded_file, format="audio/wav")
    
    # Sending file to API
    with st.spinner("Transcribing audio..."):
        # API headers
        headers = {
            "Authorization": f"Bearer {api_key}",
            "api-key": api_key,
        }
        
        # Uploading the file to the API as a form-data POST request
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}

        response = requests.post(api_url, headers=headers, files=files)

        # Display result
        if response.status_code == 200:
            result = response.json()
            st.success("Transcription completed successfully!")
            st.write("### Transcribed Text:")
            st.text_area("Transcription", result.get("text", "No transcription available"), height=200)
        else:
            st.error(f"Failed to transcribe. Status Code: {response.status_code}")
            st.write(response.text)

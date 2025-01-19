import streamlit as st
import numpy as np
import io
import wave
import os
from groq import Groq
from gtts import gTTS
import tempfile
import time
from pydub import AudioSegment
from pydub.playback import play

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def record_audio(duration=10):
    """Simulate recording audio with a placeholder silent audio segment."""
    st.write("🎤 Listening...")
    
    # Create a progress bar for recording duration
    progress_bar = st.progress(0)
    
    # Simulate recording by creating a silent audio segment
    audio = AudioSegment.silent(duration=duration * 1000)  # Duration in milliseconds
    
    # Update progress bar
    for i in range(duration):
        time.sleep(1)  # Simulate recording time
        progress_bar.progress((i + 1) / duration)
    
    progress_bar.empty()
    
    # Save to temporary WAV file
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    audio.export(temp_wav.name, format="wav")
    
    return temp_wav.name

def get_ai_response(text, context=""):
    """Get conversational response from LLaMA model."""
    try:
        # Create a more conversational prompt
        prompt = f"""Previous context: {context}
        User said: {text}
        Please respond in a friendly, conversational way. Keep responses brief but natural.
        """
        
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            max_tokens=50  # Keep responses shorter
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Sorry, I couldn't process that. {str(e)}"

def text_to_speech(text):
    """Convert text to speech with optimized settings."""
    try:
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        tts = gTTS(text, lang='en', slow=False)
        tts.save(temp_audio.name)
        return temp_audio.name
    except Exception as e:
        return f"Error with speech: {str(e)}"

def voice_assistant_page():
    st.title("💬 Voice Chat Assistant")
    
    # Initialize session state for conversation
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
    
    # Simple chat interface
    chat_container = st.container()
    
    # Voice recording button with status
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("🎤 Start Chat", key="chat_button"):
            # Record audio and get temporary file path
            temp_wav_path = record_audio(5)  # 5 seconds recording
            
            try:
                # Process speech to text
                with st.spinner("Processing..."):
                    with open(temp_wav_path, 'rb') as audio_file:
                        transcription = client.audio.transcriptions.create(
                            file=audio_file,
                            model="whisper-large-v3-turbo"
                        ).text
                    
                    # Get recent context (last 2 exchanges)
                    recent_context = " ".join([
                        f"{msg['role']}: {msg['content']}" 
                        for msg in st.session_state.conversation[-4:]
                    ])
                    
                    # Get AI response
                    response = get_ai_response(transcription, recent_context)
                    
                    # Convert to speech quickly
                    audio_file_path = text_to_speech(response)
                    
                    # Update conversation
                    st.session_state.conversation.extend([
                        {"role": "user", "content": transcription},
                        {"role": "assistant", "content": response}
                    ])
                    
                    # Play response
                    st.audio(audio_file_path)
                    
                    # Clean up temporary files
                    os.unlink(temp_wav_path)
                    os.unlink(audio_file_path)
                    
            except Exception as e:
                st.error(f"Error processing audio: {str(e)}")
                if os.path.exists(temp_wav_path):
                    os.unlink(temp_wav_path)
    
    with col2:
        # Quick phrases for testing
        st.markdown("### Quick Phrases")
        quick_phrases = [
            "How are you?",
            "What's the weather like?",
            "Tell me a joke",
            "What time is it?",
            "Goodbye"
        ]
        
        selected_phrase = st.selectbox("Try a phrase:", quick_phrases)
        if st.button("Send"):
            with st.spinner("Getting response..."):
                response = get_ai_response(selected_phrase)
                audio_file_path = text_to_speech(response)
                
                st.session_state.conversation.extend([
                    {"role": "user", "content": selected_phrase},
                    {"role": "assistant", "content": response}
                ])
                
                st.audio(audio_file_path)
                os.unlink(audio_file_path)
    
    # Display conversation in chat-like format
    with chat_container:
        st.markdown("### Conversation")
        for message in st.session_state.conversation[-6:]:  # Show last 3 exchanges
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            else:
                st.markdown(f"**Assistant:** {message['content']}")
            st.markdown("---")

if __name__ == "__main__":
    voice_assistant_page()

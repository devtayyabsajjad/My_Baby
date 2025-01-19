# utils/ai_utils.py
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def get_groq_client():
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(prompt, model="llama-3.3-70b-versatile"):
    client = get_groq_client()
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=model
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def process_voice_input(audio_data, model="whisper-large-v3-turbo"):
    client = get_groq_client()
    try:
        # Process audio data using Whisper model
        response = client.audio.transcriptions.create(
            file=audio_data,
            model=model
        )
        return response.text
    except Exception as e:
        return f"Error processing audio: {str(e)}"

# utils/constants.py
PREGNANCY_WEEKS = {
    1: "Your baby is the size of a poppy seed",
    4: "Your baby is the size of a sweetpea",
    8: "Your baby is the size of a raspberry",
    12: "Your baby is the size of a lime",
    # ... Add more weeks
}

NUTRITION_TIPS = {
    "first_trimester": [
        "Focus on folate-rich foods",
        "Increase protein intake",
        "Stay hydrated",
    ],
    "second_trimester": [
        "Add calcium-rich foods",
        "Include iron-rich foods",
        "Eat plenty of fruits",
    ],
    "third_trimester": [
        "Increase caloric intake",
        "Focus on omega-3 fatty acids",
        "Eat frequent small meals",
    ]
}

EXERCISE_RECOMMENDATIONS = {
    "first_trimester": [
        "Walking",
        "Swimming",
        "Prenatal yoga",
    ],
    "second_trimester": [
        "Low-impact aerobics",
        "Stationary cycling",
        "Modified strength training",
    ],
    "third_trimester": [
        "Gentle stretching",
        "Walking",
        "Pelvic floor exercises",
    ]
}
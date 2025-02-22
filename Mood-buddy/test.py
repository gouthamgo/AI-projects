import streamlit as st 
from transformers import pipeline 
from openai import OpenAI
from dotenv import load_dotenv
import os 


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with st.spinner("Initializing AI models..."):
    mood_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    emotion_pipeline = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")
    crisis_pipeline = pipeline("text-classification", model="roberta-base")


    resources = {
    'crisis': ['https://www.lifeline.org.au/', 'https://www.beyondblue.org.au/get-support'],
    'sadness': ['https://www.blackdoginstitute.org.au/resources-support/'],
    'anxiety': ['https://www.anxiety.org.au/'],
    'general': ['https://www.healthdirect.gov.au/mental-health']
}
    
    def analyze_text(text):
        
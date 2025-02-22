import streamlit as st
from transformers import pipeline
from openai import OpenAI
from dotenv import load_dotenv
import os
import random

# Load Environment Variables and Initialize OpenAI Client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize Models
@st.cache_resource
def load_models():
    return {
        'mood': pipeline("sentiment-analysis", model="roberta-large"),
        'emotion': pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion"),
        'crisis': pipeline("text-classification", model="roberta-base")
    }

# Initialize models with loading indicator
with st.spinner("Loading AI models..."):
    models = load_models()

# Comprehensive Resource Database
resources = {
    'crisis': [
        'https://www.lifeline.org.au/', 
        'https://www.beyondblue.org.au/get-support', 
        'https://www.sane.org/helpline', 
        'https://www.health.gov.au/mental-health-services'
    ],
    'sadness': [
        'https://www.blackdoginstitute.org.au/resources-support/', 
        'https://www.psychcentral.com/depression', 
        'https://www.helpguide.org/articles/depression/helping-a-depressed-person.htm', 
        'https://www.mayoclinic.org/diseases-conditions/depression/in-depth/depression/art-20047725'
    ],
    'anxiety': [
        'https://www.anxiety.org.au/', 
        'https://www.nimh.nih.gov/health/topics/anxiety-disorders', 
        'https://adaa.org/understanding-anxiety', 
        'https://www.verywellmind.com/anxiety-disorders-overview-4171929'
    ],
    'general': [
        'https://www.healthdirect.gov.au/mental-health', 
        'https://www.mind.org.au/', 
        'https://www.mentalhealth.org.uk/', 
        'https://www.who.int/mental_health/en/'
    ],
    'stress': [
        'https://www.webmd.com/balance/stress-management/stress-management', 
        'https://www.helpguide.org/articles/stress/stress-management.htm', 
        'https://www.calm.com/stress', 
        'https://www.apa.org/topics/stress'
    ],
    'joy': [
        'https://www.psychologytoday.com/us/basics/happiness', 
        'https://greatergood.berkeley.edu/article/item/ten_ways_to_become_more_grateful1', 
        'https://www.happify.com/hd/how-to-be-happy/', 
        'https://www.positivityblog.com/how-to-be-happy/'
    ]
}

# Parallel Processing Function
def analyze_input(text):
    analysis = {}
    
    # Mood Analysis
    mood_result = models['mood'](text)[0]
    analysis['sentiment'] = mood_result['label']
    analysis['sentiment_score'] = mood_result['score']
    
    # Emotion Analysis
    emotion_result = models['emotion'](text)[0]
    analysis['emotion'] = emotion_result['label']
    analysis['emotion_score'] = emotion_result['score']
    
    # Crisis Detection
    crisis_result = models['crisis'](text)[0]
    analysis['crisis'] = crisis_result['score'] > 0.7
    
    return analysis

# Comprehensive Suggestion Generation
def generate_suggestions(analysis):
    suggestions = {}
    if analysis['crisis']:
        suggestions['therapy'] = "Please seek help immediately. Here's what you can do right now:"
        crisis_activities = [
            "Focus on slow, deep breathing to calm yourself.",
            "Sit in a quiet, safe place and count to 10 slowly.",
            "Call a trusted friend or family member for support.",
            "Remember you're not alone - help is available.",
            "Stay in a safe environment with someone you trust."
        ]
        suggestions['activity'] = random.choice(crisis_activities)
        suggestions['resources'] = resources['crisis']
    
    elif analysis['emotion'] == 'sadness':
        suggestions['therapy'] = "Try writing down your thoughts or a quick mindfulness exercise."
        sadness_activities = [
            "Consider a short walk in nature to lift your spirits.",
            "Listen to calming music or your favorite happy song.",
            "Draw or color something fun to cheer you up.",
            "Reach out to a friend for a chat.",
            "Practice gentle self-care activities."
        ]
        suggestions['activity'] = random.choice(sadness_activities)
        suggestions['resources'] = resources['sadness']
    
    elif analysis['emotion'] == 'fear' or analysis['emotion'] == 'anxiety':
        suggestions['therapy'] = "Take a moment to breathe deeply or practice grounding techniques."
        anxiety_activities = [
            "Try the 5-4-3-2-1 grounding exercise.",
            "Practice deep breathing for 5 minutes.",
            "Listen to soothing nature sounds.",
            "Hold something comforting and focus on its texture.",
            "Write down your worries to release them."
        ]
        suggestions['activity'] = random.choice(anxiety_activities)
        suggestions['resources'] = resources['anxiety']
    
    elif analysis['emotion'] == 'anger':
        suggestions['therapy'] = "Write down what's making you upset or try a calming exercise."
        anger_activities = [
            "Take a brisk walk to release tension.",
            "Practice progressive muscle relaxation.",
            "Count backwards from 100 by 7s.",
            "Squeeze and release a stress ball.",
            "Write a letter expressing your feelings (without sending it)."
        ]
        suggestions['activity'] = random.choice(anger_activities)
        suggestions['resources'] = resources['stress']
    
    elif analysis['emotion'] == 'joy':
        suggestions['therapy'] = "You're doing great—keep nurturing your positivity!"
        joy_activities = [
            "Share your happiness with someone you care about.",
            "Write down three things you're grateful for.",
            "Plan something fun for tomorrow.",
            "Take a photo of something that makes you smile.",
            "Dance to your favorite upbeat song."
        ]
        suggestions['activity'] = random.choice(joy_activities)
        suggestions['resources'] = resources['joy']
    
    else:
        suggestions['therapy'] = "You're doing well—keep up the good vibes!"
        general_activities = [
            "Try a new hobby or revisit an old one.",
            "Connect with a friend or family member.",
            "Take a moment for mindful breathing.",
            "Go for a short walk outside.",
            "Write down your thoughts in a journal."
        ]
        suggestions['activity'] = random.choice(general_activities)
        suggestions['resources'] = resources['general']
    
    return suggestions

# Enhanced Response Generation
def generate_response(user_input, analysis, suggestions):
    prompt = f"""
    User input: {user_input}
    Analysis: Sentiment is {analysis['sentiment']} (score: {analysis['sentiment_score']}), 
             Emotion is {analysis['emotion']} (score: {analysis['emotion_score']}), 
             Crisis: {analysis['crisis']}.
    Suggestions: Therapy - {suggestions['therapy']}, 
                Activity - {suggestions['activity']}.
    Resources: {', '.join(suggestions['resources'])}.
    
    Create an empathetic response that:
    1. Acknowledges their feelings
    2. Offers the suggestions naturally
    3. Encourages reaching out for support if needed
    4. Maintains a warm, supportive tone
    End with 'Feel free to share more anytime.'
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a compassionate Mood Buddy focused on providing support and understanding."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content, suggestions['resources']
    except Exception as e:
        return f"I'm here to listen and support you. However, I'm having trouble formulating my response right now. Please try sharing again.", suggestions['resources']

# Enhanced UI
def main():
    # Custom CSS
    st.markdown("""
        <style>
        .main {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .stTextArea > div > div > textarea {
            border: 2px solid #3498db;
            border-radius: 10px;
            padding: 15px;
            font-size: 16px;
        }
        .stButton > button {
            background-color: #3498db;
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            border: none;
            width: 100%;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #2980b9;
            transform: translateY(-2px);
        }
        .response-box {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stButton {
            margin-bottom: 0;
        }
        .stSpinner {
            margin-bottom: 0;
            margin-top: 5px;
        }
        .response-box h4 {
            margin-top: 15px;
            margin-bottom: 10px;
        }
        .stInfo {
            margin-bottom: 15px;
        }
        .emotion-metric {
            text-align: center;
            padding: 10px;
            background-color: #f0f0f0;
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.title("💚 Mood Buddy")
    st.write("Share your thoughts in a safe, private space. No data is stored.")

    # User Input
    user_input = st.text_area(
        "How are you feeling today?",
        height=150,
        placeholder="Type your thoughts here..."
    )

    # Process Input
    if st.button("Share", use_container_width=True):
        if user_input:
            # Analyze input with minimal spacing
            analysis = analyze_input(user_input)
            suggestions = generate_suggestions(analysis)
            response, links = generate_response(user_input, analysis, suggestions)
            
            # Display response in a compact layout
            # st.markdown('<div class="response-box">', unsafe_allow_html=True)
            st.write(response)
                
                # Display suggestions with minimal spacing
            st.markdown("#### Try This")
            st.info(suggestions['activity'])
                
                # Display resources immediately after suggestions
            if links:
                    st.markdown("#### Helpful Resources")
                    for link in links:
                        st.markdown(f"- [{link}]({link})")
            st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
        ---
        <p style='text-align: center; color: #666;'>
        This is not a substitute for professional mental health care.<br>
        If you're in crisis, please reach out to emergency services or crisis helplines.
        </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
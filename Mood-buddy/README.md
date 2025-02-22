# Mood Buddy: An AI-Powered Mental Health Companion

## 🌟 What is Mood Buddy?
Mood Buddy is a fun, friendly AI chatbot I created to support mental health and wellbeing, inspired by Australia’s R U OK? campaign. It’s like having a cheerful buddy who asks, “Are you OK?” and helps you feel better by understanding your feelings, offering supportive suggestions, and sharing helpful resources—all in a safe, private space. No data is stored, ensuring your privacy!

## 💡 Inspiration
I built Mood Buddy to reflect the spirit of R U OK?, which encourages people to check in on each other’s mental health. It’s my way of contributing to mental health awareness in Australia and beyond, providing a tool for people to express their emotions and find support.

## 🚀 Features
- **Mood Detection:** Uses AI to understand if you’re happy, sad, anxious, or stressed.
- **Emotion Support:** Offers random, fun activities like walks, breathing exercises, or drawing to lift your spirits.
- **Crisis Help:** Identifies potential crises and suggests urgent resources.
- **Helpful Resources:** Shares links to trusted mental health websites for further support.
- **Privacy-First:** Operates statelessly—your inputs aren’t saved, keeping everything private and secure.
- **Interactive UI:** A simple, colorful Streamlit website where you can chat with your buddy.

## 🛠 Tech Stack
- **Streamlit:** Creates the easy-to-use, playful website.
- **OpenAI (gpt-4):** Powers empathetic, natural responses from a smart AI robot.
- **Hugging Face Models:** Uses roberta-large, distilbert-base-uncased-emotion, and roberta-base to detect moods, emotions, and crises through parallel processing.
- **Python Libraries:** Includes transformers, torch, python-dotenv for secure API key management, and random for varied suggestions.

## 📸 Live Demo
Check out Mood Buddy in action! [Watch the Demo Video](https://yourapp.streamlit.app) (replace with your actual Streamlit Cloud URL after deployment). See how it responds to inputs like “I’m feeling really anxious today” with supportive replies, activity suggestions, and resources.

## 🚀 Getting Started (Local Setup)
Want to play with Mood Buddy locally? Here’s how (for fun and learning—code not included here for privacy):

1. **Clone or Download:** Get this repo to your computer (ask a grown-up or teacher for help).
2. **Install Python:** Make sure you have Python 3.8+ (download from python.org if needed).
3. **Set Up Virtual Environment:**
   - Open a terminal, go to your folder, and type:
     ```bash
     python -m venv venv
     source venv/bin/activate  # Windows: venv\Scripts\activate
     ```
4. **Install Dependencies:**
   - In the terminal, type:
     ```bash
     pip install streamlit transformers torch openai python-dotenv
     ```
5. **Add API Key:**
   - Create a `.env` file in your folder with:
     ```
     OPENAI_API_KEY=your-openai-api-key-here
     ```
   - Get your OpenAI key from [platform.openai.com](https://platform.openai.com).
6. **Run the App:**
   - Type:
     ```bash
     streamlit run app.py
     ```
   - Open your browser to `http://localhost:8501` and chat with Mood Buddy!

## 🌍 Deployment
not yet deployed 

## 🎉 Why I Built This
I wanted to learn about AI, mental health, and how technology can help people. Playing with Streamlit, OpenAI, and Hugging Face taught me parallel processing, natural language understanding, and building empathetic AI agents. It’s my way of supporting the R U OK? mission and creating something fun and helpful!

## ❤️ Acknowledgements
- Inspired by the R U OK? campaign (ruok.org.au) for mental health awareness.
- Built using open-source tools from Streamlit, OpenAI, and Hugging Face—thanks to these amazing communities!

## 🚀 Contribute or Learn
Feel free to reach out if you want to learn more about AI, mental health, or Streamlit apps. I’d love to hear your ideas on how Mood Buddy can grow! #AI #MentalHealth #RUOKDay #TechForGood

---


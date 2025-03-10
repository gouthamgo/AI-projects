from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import re

# Download required NLTK data (run once or ensure it's available)
nltk.download("vader_lexicon")
nltk.download("punkt")
nltk.download("stopwords")

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust based on frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-feedback/")
async def upload_feedback(file: UploadFile = File(...), column_name: str = Form(...)):
    # Read uploaded file
    contents = await file.read()
    try:
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid CSV file format.")

    # Validate column existence
    if column_name not in df.columns:
        raise HTTPException(status_code=400, detail=f"Column '{column_name}' not found in file.")

    feedback_texts = df[column_name].dropna().tolist()
    if not feedback_texts:
        raise HTTPException(status_code=400, detail="No valid feedback data found in the specified column.")

    # Initialize sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    stop_words = set(stopwords.words("english"))

    # Enhanced Insights
    insights = {
        "sentiment_distribution": Counter(),  # Positive, Negative, Neutral counts
        "detailed_categories": Counter(),    # More granular categories
        "top_words": Counter(),              # Most frequent words
        "average_length": 0,                 # Average feedback length
    }

    # Process each feedback
    total_length = 0
    for text in feedback_texts:
        text = str(text).strip()
        total_length += len(text)

        # 1. Sentiment Analysis (VADER)
        sentiment_scores = sia.polarity_scores(text)
        compound_score = sentiment_scores["compound"]
        if compound_score >= 0.05:
            insights["sentiment_distribution"]["positive"] += 1
        elif compound_score <= -0.05:
            insights["sentiment_distribution"]["negative"] += 1
        else:
            insights["sentiment_distribution"]["neutral"] += 1

        # 2. Detailed Categories (Keyword-based + Sentiment)
        text_lower = text.lower()
        if "excellent" in text_lower or "great" in text_lower or "love" in text_lower:
            insights["detailed_categories"]["highly_positive"] += 1
        elif "good" in text_lower or "nice" in text_lower:
            insights["detailed_categories"]["positive"] += 1
        elif "bad" in text_lower or "poor" in text_lower:
            insights["detailed_categories"]["negative"] += 1
        elif "terrible" in text_lower or "awful" in text_lower or "hate" in text_lower:
            insights["detailed_categories"]["highly_negative"] += 1
        else:
            insights["detailed_categories"]["neutral"] += 1

        # 3. Word Frequency (excluding stopwords)
        words = word_tokenize(text_lower)
        cleaned_words = [word for word in words if word.isalnum() and word not in stop_words]
        insights["top_words"].update(cleaned_words)

    # 4. Average Feedback Length
    insights["average_length"] = round(total_length / len(feedback_texts), 2) if feedback_texts else 0

    # Format Response
    response = {
        "insights": {
            "sentiment_distribution": [
                {"category": k, "count": v} for k, v in insights["sentiment_distribution"].items()
            ],
            "detailed_categories": [
                {"category": k, "count": v} for k, v in insights["detailed_categories"].items()
            ],
            "top_words": [
                {"word": k, "count": v} for k, v in insights["top_words"].most_common(5)
            ],
            "average_length": insights["average_length"],
        }
    }

    return response

# Health check endpoint (optional)
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io
from collections import Counter

app = FastAPI()

# Enable CORS to allow frontend to call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-feedback/")
async def upload_feedback(file: UploadFile = File(...), column_name: str = Form(...)):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

    # Ensure column exists
    if column_name not in df.columns:
        return {"error": f"Column '{column_name}' not found in file."}

    feedback_texts = df[column_name].dropna().tolist()

    # Simple keyword-based categorization
    categories = ["positive", "negative", "neutral"]
    category_counts = Counter()
    for text in feedback_texts:
        if "good" in text.lower() or "excellent" in text.lower():
            category_counts["positive"] += 1
        elif "bad" in text.lower() or "poor" in text.lower():
            category_counts["negative"] += 1
        else:
            category_counts["neutral"] += 1

    insights = [{"category": cat, "count": category_counts[cat]} for cat in categories]

    return {"insights": insights}

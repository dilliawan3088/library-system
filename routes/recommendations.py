import os
from dotenv import load_dotenv
import openai
from fastapi import APIRouter
from models.schemas import BookRecommendationRequest


openai.api_key = "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"

router = APIRouter()

@router.post("/recommendations/")
def recommend_books(request: BookRecommendationRequest):
    prompt = f"Suggest books based on the following preference: {request.preference}"

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful book recommender."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )

    return {"recommendations": response.choices[0].message.content.strip()}


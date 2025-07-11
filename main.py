import openai
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from routes import books, users, borrow, recommendations
from fastapi.middleware.cors import CORSMiddleware



from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://library-system-frontend-bice.vercel.app",  # ✅ no trailing slash
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers for different functionalities
app.include_router(books.router)
app.include_router(users.router)
app.include_router(borrow.router)
app.include_router(recommendations.router)
# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.get("/")
def read_root():
    return {"message": "📚 Smart Library AI Backend is running!"}

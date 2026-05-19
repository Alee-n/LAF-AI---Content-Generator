import os


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "laf_ai_secret")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

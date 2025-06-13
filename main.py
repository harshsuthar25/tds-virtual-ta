from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# ✅ Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
def get_answer(q: Query):
    return {
        "answer": "Thanks for your question! (This is a placeholder.)",
        "links": []
    }

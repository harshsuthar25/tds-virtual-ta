from fastapi import FastAPI, UploadFile, File
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
def get_answer(q: Query):
    return {
        "answer": "Thanks for your question! (This is a placeholder.)",
        "links": []
    }

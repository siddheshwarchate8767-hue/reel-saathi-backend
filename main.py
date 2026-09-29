
import os
import subprocess
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class RenderRequest(BaseModel):
    audio_url: str
    image_urls: List[str]
    output_filename: str = "output.mp4"

@app.get("/")
def home():
    return {"status": "Reel Saathi FFmpeg Backend Running!"}

@app.post("/render")
def render_video(req: RenderRequest):
    try:
        cmd = f'ffmpeg -loop 1 -i {req.image_urls[0]} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {req.output_filename}'
        subprocess.run(cmd, shell=True, check=True)
        return {"status": "success", "message": "Video rendered successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

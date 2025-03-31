import threading
import tkinter as tk
from fastapi import FastAPI
import uvicorn
from typing import List, Optional
from pydantic import BaseModel

root = tk.Tk()
root.title("Tkinter Canvas Drawing")
canvas = tk.Canvas(root, width=450, height=450, bg='white')
canvas.pack()

class DrawRequest(BaseModel):
    coordinates: List[int] = [0,0]
    fill: Optional[str] = None
    text: Optional[str] = None
    
    
app = FastAPI()


@app.post("/clear")
async def clear_canvas() -> str:
    canvas.delete("all")
    return "Canvas cleared"

@app.post("/draw/line")
async def draw_line(DrawRequest: DrawRequest) -> str:
    canvas.create_line(*DrawRequest.coordinates, fill=DrawRequest.fill)
    return "line drawn"


@app.post("/draw/rectangle")
async def draw_rectangle(DrawRequest: DrawRequest) -> str:
    canvas.create_rectangle(*DrawRequest.coordinates, fill=DrawRequest.fill)
    return "Rectangle drawn"

@app.post("/draw/oval")
async def draw_oval(DrawRequest: DrawRequest) -> str:
    canvas.create_oval(*DrawRequest.coordinates, fill=DrawRequest.fill)
    return "oval drawn"

@app.post("/draw/text")
async def draw_text(DrawRequest: DrawRequest) -> str:
    canvas.create_text(*DrawRequest.coordinates, fill=DrawRequest.fill, text=DrawRequest.text)
    return "Text drawn"

def run_fastapi():
    uvicorn.run(app, host="127.0.0.1", port=8000)

    # Main function
if __name__ == "__main__":
    # Start FastAPI in a separate thread
    api_thread = threading.Thread(target=run_fastapi, daemon=True)
    api_thread.start()
    
    root.mainloop()
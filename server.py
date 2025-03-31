from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP


# Initialize FastMCP server
mcp = FastMCP("draw", 
              description="basic drawing tools in a canvas of 400 by 400 pixels. 0,0 is the upper left corner")

port="8000"

@mcp.tool()
async def draw_lines(coordinates: list[int], fill: str = "black") -> str:
    """
    Draw one or more connected lines on the canvas.
    Args:
        coordinates: list of x,y coordinates. e.g. [10,10,100,100] for one line, [10,10,100,100,200,100] for two connected lines
        fill (str): The color of the line. e.g. blue, green, black, etc.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"http://localhost:{port}/draw/line", json={
                "coordinates": coordinates,
                "fill": fill
            })
            response.raise_for_status()
        except Exception as exc:
            return f"error: {exc}"
        return "line drawn"
    

@mcp.tool()
async def draw_rectangle(x1: int, y1: int, x2: int, y2: int, fill: str = "black") -> str:
    """
    Draw a rectangle on the canvas.
    Args:
        x1 (int): The x-coordinate of the top-left corner of the rectangle.
        y1 (int): The y-coordinate of the top-left corner of the rectangle.
        x2 (int): The x-coordinate of the bottom-right corner of the rectangle.
        y2 (int): The y-coordinate of the bottom-right corner of the rectangle.        
        fill (str): The fill color. e.g. blue, green, black, etc.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"http://localhost:{port}/draw/rectangle", json={
                "coordinates": [x1, y1, x2, y2],
                "fill": fill
                })            
            response.raise_for_status()
        except Exception as exc:
            return f"error: {exc}"
    return "rectangle drawn"

@mcp.tool()
async def draw_oval(x1: int, y1: int, x2: int, y2: int, fill: str = "black") -> str:
    """
    Draw an oval or circle on the canvas.
    Args:
        x1 (int): The x-coordinate of the top-left corner of the oval boucnding box.
        y1 (int): The y-coordinate of the top-left corner of the oval boucnding box.
        x2 (int): The x-coordinate of the bottom-right corner of the oval boucnding box.
        y2 (int): The y-coordinate of the bottom-right corner of the oval boucnding box.
        fill (str): The fill color. e.g. blue, green, black, etc.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"http://localhost:{port}/draw/oval",json={
                "coordinates": [x1, y1, x2, y2],
                "fill": fill
                })            
            response.raise_for_status()
        except Exception as exc:
            return f"error: {exc}"
    return "rectangle drawn"

@mcp.tool(
        name="draw_text",
        description="Draw text on the canvas, given its center coordinates and text"
)
async def draw_text(x: int, y: int, text: str, fill: str = "black") -> str:
    """
    Draw text on the canvas.
    Args:
        x (int): The x-coordinate of the middle of the text
        y (int): The y-coordinate of the middle of the text
        fill (str): The color of the text. e.g. blue, green, black, etc.
        text (str): The text to draw
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"http://localhost:{port}/draw/text", json= {
                "coordinates": [x, y],
                "fill": fill,
                "text": text
            })
            response.raise_for_status()
        except Exception as exc:
            return f"error {exc}"
    return "text drawn"
        
@mcp.tool(name="clear_canvas",
          description="Clear the canvas")
async def clear_canvas() -> str:
    """
    Clear the canvas.
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"http://localhost:{port}/clear")
            response.raise_for_status
        except Exception as exc:
            return f"error: {exc}"
    return "canvas cleared"
    

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
    
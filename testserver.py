import asyncio

from server import draw_rectangle, draw_text, draw_lines, draw_oval, clear_canvas



async def main():
    await clear_canvas()
    await draw_rectangle(10, 10, 100, 150)    
    await draw_text(50, 50, "hellowolrd", "white")
    await draw_lines([10, 10, 100, 150], "blue")
    await draw_oval(100, 100, 200, 250, "yellow")    


if __name__ == "__main__":
    asyncio.run(main())

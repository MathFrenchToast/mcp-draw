# MCP DRAW Project

Demonstration of a MCP server talking to a drawing app.
The app has a HTTP rest interface (see http://localhost:8000/docs) to draw to a tkinter canvas.


## launch

`uv run draw.py`

test everythin is ok, with the requests in /test/requests.http

## link to claude desktop


Add it to your claude config
```json
"mcpServers": {
    ...

    "draw": {
        "command": "uv",
        "args": [
            "--directory",
            "C:\\dev\\projets\\frenchtoast\\mcp-draw",                
            "run",
            "draw.py"
        ]
    }
    ...
}
```

## test it with LangGraph

create a .env file with an entry for `OPENAI_API_KEY=****`
cd langgraph  
python client.py  


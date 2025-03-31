import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from langchain_openai import ChatOpenAI

import os
from dotenv import dotenv_values

config = dotenv_values("./.env")
os.environ["OPENAI_API_KEY"] = config.get("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-4o-mini")

async def main():
    
    async with MultiServerMCPClient(
        {
            "draw": {
                "command": "uv",
                "args": [
                    "--directory",
                    "C:\\dev\\projets\\frenchtoast\\mcp-draw",                
                    "run",
                    "server.py"
                ],  
                "transport": "stdio",
            }
        }
    ) as client:
        agent = create_react_agent(model, client.get_tools())
        ag_response = await agent.ainvoke({"messages": 
                                             """using draw tool, create an illustration for this headline: 
                                             'les émissions pré-estimées pour l'année 2024 continuent leur réduction pour atteindre 366 millions de tonnes de CO2 équivalent (Mt CO2e), soit –1,8 % par rapport à 2023'
                                             think step by step, and plan your drawing first.
                                             After drawing, you'll explain what you have drawn.
                                             """})
        print(ag_response.get("output"))

if __name__ == "__main__":
    asyncio.run(main())

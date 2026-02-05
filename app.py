import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, trace

load_dotenv(override=True)

system_instructions = """You are a professional chatbot that speaks on behalf of a professional Python developer."""

agent = Agent(name="professional_python_developer", instructions=system_instructions, model="gpt-4")

async def main(input):
    with trace("HireMe Chatbot"):
        result = await Runner.run(agent, input)
        print(result.final_output)

if __name__ == "__main__":
    while True:
        asyncio.run(main(input("Your message:")))


from dotenv import load_dotenv
from openai import OpenAI
import json
import gradio as gr

load_dotenv(override=True)
cv_path= "knowledge_base/profile.json"

def extract_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return json.dumps(data, indent=2)

async def chatbot(user_input, history):
    client = OpenAI()
    system_instructions = f"""
    You are a chatbot representing a junior Python developer.
    Use ONLY the information below.
    If something is not mentioned, say you don't know.
    
    {extract_json(cv_path)}
"""

    response = client.responses.create(
        model="gpt-4",
        input=user_input,
        instructions=system_instructions,
        max_output_tokens=300
    )

    return response.output_text


if __name__ == "__main__":
    chat_interface = gr.ChatInterface(fn=chatbot, title="Junior Python Developer Chatbot",
    description="Popovídej si se mnou a nabídni mi topovej job!🔥")
    chat_interface.launch()



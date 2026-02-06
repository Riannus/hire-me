from dotenv import load_dotenv
from openai import OpenAI
import json
import gradio as gr
import config

load_dotenv(override=True)
cv_path = "knowledge_base/profile.json"


def extract_json(file_path: str) -> str:
    with open(file_path, "r") as file:
        data = json.load(file)
        return json.dumps(data, indent=2)


async def chatbot(user_input: str, history: list) -> str:
    client = OpenAI()

    response = client.responses.create(
        model=config.MODEL,
        input=user_input,
        instructions=config.SYSTEM_INSTRUCTIONS + extract_json(config.CV_PATH),
        max_output_tokens=config.MAX_OUTPUT_TOKENS,
    )

    return response.output_text


if __name__ == "__main__":
    chat_interface = gr.ChatInterface(
        fn=chatbot,
        title="Junior Python Developer Chatbot",
        description="Popovídej si se mnou a nabídni mi topovej job!🔥",
    )
    chat_interface.launch()

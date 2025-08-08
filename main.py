import os
import requests
from dotenv import find_dotenv, load_dotenv
from langchain import PromptTemplate, LLMChain, OpenAI
from huggingface_hub import InferenceClient
import streamlit

load_dotenv(find_dotenv())
api_key = os.getenv("APY_TOKEN")

client = InferenceClient(
    provider="fal-ai",
    api_key = os.getenv("APY_TOKEN"),
)

def create_image(prompt):

    # output is a PIL.Image object
    image = client.text_to_image(
        prompt,
        model="Qwen/Qwen-Image",
    )
    print(f"Creating a {prompt} image.")
    image.show()

    image.save('LangChain/new_image.jpg') 

def main():

    streamlit.set_page_config(page_title="Hyprog", page_icon="🐆")

    streamlit.header("Welcome to Hyena Programming, what can I help you with?")
    
    # Add a text input for the prompt
    prompt = streamlit.text_input("Enter your desired prompt for image creation:", 
                          placeholder="A cute cat wearing sunglasses")

    # Add a button to trigger image generation
    if streamlit.button("Generate Image"):
        if prompt:  # Only proceed if there's a prompt
            with streamlit.spinner("Generating your image..."):
                try:
                    image = create_image(prompt)
                    streamlit.image(image, caption=f"Generated image: {prompt}", use_column_width=True)
                except Exception as e:
                    streamlit.error(f"Error generating image: {e}")
        else:
            streamlit.warning("Please enter a prompt first")

if __name__ == "__main__":
    main()
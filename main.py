# Importing necessary modules and classes
from openai import OpenAI  # Importing the OpenAI class for API interaction
from fastapi import FastAPI, Form  # Importing FastAPI and Form for creating a web application
from typing import Annotated  # Importing Annotated for type hints

# Initializing OpenAI with the provided API key
openai = OpenAI(
    api_key="MyKey"
)

# Creating a FastAPI application instance
app = FastAPI()

# Initializing an empty list to store chat history
chat_log = []

# Defining a FastAPI route to handle POST requests
@app.post("/")
async def chat(user_input: Annotated[str, Form()]):
    """
    Handle incoming POST requests to the root endpoint.
    This function processes user input, generates a response using OpenAI GPT-3.5-turbo,
    and returns the bot's response.

    Parameters:
        user_input (str): The user's input received from a form.

    Returns:
        str: The bot's response.
    """

    # Appending user input to the chat log
    chat_log.append({'role': 'user', 'content': user_input})

    # Generating a response from the OpenAI GPT-3.5-turbo model
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=chat_log,
        temperature=0.6  # Controlling the randomness of the model's output
    )

    # Extracting the bot's response from the OpenAI API response
    bot_response = response.choices[0].message.content

    # Appending bot's response to the chat log
    chat_log.append({'role': 'assistant', 'content': bot_response})

    # Returning the bot's response as the API response
    return bot_response

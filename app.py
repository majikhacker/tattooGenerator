# import openai
# import streamlit as st

# openai.api_key = st.secrets["OPENAI_API_KEY"]

# if "messages" not in st.session_state:
#     st.session_state.messages = [
#     {"role": "system", 
# "content":"you are a tatoo generator,you will generate black and white tatoo images"},
# ]

# def generate_and_append_image(user_message):
#     st.session_state.messages.append({"role": "user", "content": user_message})  

# response = openai.images.generate(
#   model = "dall-e-3",
#   prompt = "user_message",
#   size = "1024x1024",
#   n = 1,
# )

# image_url = response.data[0].url

# st.image(image_url, caption="Generated Image")

# st.session_state.messages.append({"role": "assistant", "content": image_url})

# user_message = st.text_input("Enter your tattoo idea: ", key="user_message")

# # Condition to generate image on user input
# if user_message and st.button("Generate"):
#      generate_and_append_image(user_message)
    


# import openai

# openai.api_key = ["OPENAI_API_KEY"]

# messages = [
#     {"role": "system", 
# "content":"you are a tatoo generator,you will generate black and white tatoo images"},
# ]

  
# user_message = input("User: ")
# if user_message:
#   messages.append(
#     {"role": "user", "content": user_message},
#   )
# response = openai.images.generate(
#   model = "dall-e-3",
#   prompt = user_message,
#   size = "1024x1024",
#   n = 1,
# )
    
# image_url = response.data[0].url
# print(f'Tattoo Generator: {image_url}')
from openai import OpenAI
import streamlit as st

client = OpenAI.api_key=st.secrets["OPENAI_API_KEY"]


# Assuming your OpenAI API key is stored in Streamlit's secrets or an environment variable

# Initialize messages if not already in the session state
if "messages" not in st.session_state:
st.session_state.messages = [
        {"role": "system", "content": ""},
    ]
tattoo_prompt = "as a black and white stencil-style that i can turn into a tattoo"
def generate_and_append_image(user_text):
    # Append user message
st.session_state.messages.append({"role": "user", "content": user_text})

    # Call OpenAI API to get image
response = client.images.generate(model="dall-e-3",
    prompt=user_text + tattoo_prompt,
    size="1024x1024",
    quality="standard",
    style="natural",
    n=1)

    # Assuming the response structure has the image URL at response['data'][0]['url']
image_url = response.data[0].url  # Adjust according to the actual response structure

    # Display the image
st.image(image_url, caption="Generated Image")

    # Append the assistant's message with the image URL
st.session_state.messages.append({"role": "assistant", "content": image_url})

# User input
user_text = st.text_input("Enter your tattoo idea: ", key="user_input")

# Condition to generate image on user input
if user_text and st.button("Generate"):
    generate_and_append_image(user_text)





import openai
import streamlit as st

# Initialize the OpenAI client with API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Title Text
title_text = "Tattoo? Yes Please!"

# Apply HTML/CSS attributes
st.markdown(f"<h1 style='text-align: center;'>{title_text}</h1>", unsafe_allow_html=True)

# Define options for user to select
color_options = ["B/W", "Color"]
style_options = ["Japanese", "Tribal", "Traditional/Old School", "Realistic", "Basic"]
technique_options = ["Blackwork(No hard lines)", "Outlined"]

# Collect user input for the tattoo options
selected_color = st.selectbox("Would you like your tattoo in black and white or in color?", color_options)
selected_style = st.selectbox("Choose the style for your tattoo:", style_options)
selected_technique = st.selectbox("Choose the technique for your tattoo:", technique_options)

user_message = st.text_input("Describe the idea you have for your tattoo:")

# Description that will be added to user input to ensure the image looks like a tattoo sketch
tattoo_prompt = (
    f"Can you create an image on a blank white canvas that looks like a tattoo sketch of user_message with no backround that has {selected_style} style, with {selected_technique} technique and in {selected_color}"
)



if user_message and st.button("Generate"):
    client = openai.OpenAI()  # Create an instance of the OpenAI client
    response = client.images.generate(
        model="dall-e-3",
        prompt=tattoo_prompt + user_message,  # Use user's message as prompt
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url

    st.image(image_url, caption="Generated Image")

st.write("Tattoo Yes Please is Created and Owned by NovusOrbisTechnology, LLC")



#*****____________*****__________*****______________*****______________*****________________*****______________*****


# from openai import OpenAI
# import streamlit as st

# # Initialize the OpenAI client with your API key
# client = OpenAI.api_key=st.secrets["OPENAI_API_KEY"]

# # Define your title text
# title_text = "T.Y.P."

# # Use st.markdown() to apply CSS for centering
# st.markdown(f"<h1 style='text-align: center;'>{title_text}</h1>", unsafe_allow_html=True)

# # Display business name in small text on the sidebar
# st.write("created by MajikB AI")

# # Define the options for the user to select
# color_options = ["B/W", "Color"]
# style_options = ["Japanese", "Tribal", "Traditional/Old School", "Realistic", "Basic"]
# technique_options = ["Blackwork", "Outlined"]

# # Collect user input for color, style, and technique
# selected_color = st.selectbox("Would you like your tattoo in black and white or in color?", color_options)
# selected_style = st.selectbox("Choose the style for your tattoo:", style_options)
# selected_technique = st.selectbox("Choose the technique for your tattoo:", technique_options)



# # Function to generate and append image
# user_text = st.text_input("Describe the idea you have for your tattoo")
# tattoo_prompt = (
#     f"Can you create a tattoo design that matches the following description:\n"
#     f"- Style: {selected_style}\n"
#     f"- Technique: {selected_technique}\n"
#     f"- Color: {selected_color}\n"
#     "Please ensure that the design looks like it was hand-drawn by a tattoo artist on paper, "
#     "with no background. The image should be displayed on a white surface to simulate a clean canvas."
#         )
#         # Call OpenAI API to get image
# response = client.images.generate(model="dall-e-3",
#         prompt=tattoo_prompt + user_text,
#         size="1024x1024",
#         quality="standard",
#         n=1)
        
#         # Assuming the response structure has the image URL at response['data'][0]['url']
# image_url = response.data[0].url # Adjust according to the actual response structure

#     # Display the image
# st.image(image_url, caption="Generated Image")

#     # Append the assistant's message with the image URL
# st.session_state.messages.append({"role": "assistant", "content": image_url})

# ## User input for the tattoo idea


# # Condition to generate image on user input
# if user_text and st.button("Generate"):
#     (tattoo_prompt)



#*****____________*****__________*****______________*****______________*****________________*****______________*****


# from openai import OpenAI
# import streamlit as st

# # Initialize the OpenAI client with your API key
# client = openai(st.secrets["OPENAI_API_KEY"])

# # Define your title text
# title_text = "T.Y.P."

# # Use st.markdown() to apply CSS for centering
# st.markdown(f"<h1 style='text-align: center;'>{title_text}</h1>", unsafe_allow_html=True)

# # Display business name in small text on the sidebar
# st.write("created by MajikB AI")

# # Define the options for the user to select
# color_options = ["B/W", "Color"]
# style_options = ["Japanese", "Tribal", "Traditional/Old School", "Realistic", "Basic"]
# technique_options = ["Blackwork", "Outlined"]

# # Collect user input for color, style, and technique
# selected_color = st.selectbox("Would you like your tattoo in black and white or in color?", color_options)
# selected_style = st.selectbox("Choose the style for your tattoo:", style_options)
# selected_technique = st.selectbox("Choose the technique for your tattoo:", technique_options)

# # User input for the tattoo idea
# user_input = st.text_input("Describe the idea you have for your tattoo")

# # Function to generate and append image
# def generate_and_append_image(user_text, color, style, technique):
#     try:
#         # Construct the prompt based on user's selections
#         tattoo_prompt = (
#             f"Can you create a tattoo design that matches the following description:\n"
#             f"- Style: {style}\n"
#             f"- Technique: {technique}\n"
#             f"- Color: {color}\n"
#             f"- Description: {user_text}\n"
#             "Please ensure that the design looks like it was hand-drawn by a tattoo artist on paper, "
#             "with no background. The image should be displayed on a white surface to simulate a clean canvas."
#         )
#         # Call OpenAI API to get image
#         response = client.images.generate(model="dall-e-3",
#                                           prompt=tattoo_prompt,
#                                           size="1024x1024",
#                                           quality="standard",
#                                           n=1)
        
#         # Assuming the response structure has the image URL at response['data'][0]['url']
#         image_url = response['data'][0]['url'] # Adjust according to the actual response structure

#         # Display the image
#         st.image(image_url, caption="Generated Image")

#         # Append the assistant's message with the image URL
#         st.session_state.messages.append({"role": "assistant", "content": image_url})

#     except Exception as e:
#         st.error(f"Error: {e}")

# # User input
# user_text = st.text_input("Enter your tattoo idea: ", key="user_input")

# # Condition to generate image on user input
# if user_text and st.button("Generate"):
#     generate_and_append_image(user_text, selected_color, selected_style, selected_technique)


#*****____________*****__________*****______________*****______________*****________________*****______________*****



# import streamlit as st
# from openai import OpenAI, ApiError

# # Initialize the OpenAI client with your API key
# client = OpenAI.api_key=st.secrets["OPENAI_API_KEY"]

# # Define your title text
# title_text = "T.Y.P."

# # Use st.markdown() to apply CSS for centering
# st.markdown(f"<h1 style='text-align: center;'>{title_text}</h1>", unsafe_allow_html=True)

# # Display business name in small text on the sidebar
# st.write("created by MajikB AI")

# # Define the options for the user to select
# color_options = ["B/W", "Color"]
# style_options = ["Japanese", "Tribal", "Traditional/Old School", "Realistic", "Basic"]
# technique_options = ["Blackwork", "Outlined"]

# # Collect user input for color, style, and technique
# selected_color = st.selectbox("Would you like your tattoo in black and white or in color?", color_options)
# selected_style = st.selectbox("Choose the style for your tattoo:", style_options)
# selected_technique = st.selectbox("Choose the technique for your tattoo:", technique_options)

# # User input for the tattoo idea
# user_input = st.text_input("Describe the idea you have for your tattoo")

# # Function to generate and append image
# def generate_and_append_image(user_text, color, style, technique):
#     try:
#         # Construct the prompt based on user's selections
#         tattoo_prompt = (
#             f"Can you create a tattoo design that matches the following description:\n"
#             f"- Style: {style}\n"
#             f"- Technique: {technique}\n"
#             f"- Color: {color}\n"
#             f"- Description: {user_text}\n"
#             "Please ensure that the design looks like it was hand-drawn by a tattoo artist on paper, "
#             "with no background. The image should be displayed on a white surface to simulate a clean canvas."
#         )
#         # Call OpenAI API to get image
#         response = client.images.generate(model="dall-e-3",
#                                           prompt=tattoo_prompt,
#                                           size="1024x1024",
#                                           quality="standard",
#                                           n=1)
        
#         # Assuming the response structure has the image URL at response['data'][0]['url']
#         image_url = response.data[0].url # Adjust according to the actual response structure

#         # Display the image
#         st.image(image_url, caption="Generated Image")

#         # Append the assistant's message with the image URL
#         st.session_state.messages.append({"role": "assistant", "content": image_url})
#     except ApiError as e:
#         st.error(f"Error generating image: {e}")

# # Condition to generate image on user input
# if user_input and st.button("Generate"):
#     generate_and_append_image(user_input, selected_color, selected_style, selected_technique)

# # Initialize messages if not already in the session state
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display messages
# st.write("### Chat Log:")
# for message in st.session_state.messages:
#     st.write(f"{message['role'].capitalize()}: {message['content']}")






# def generate_and_append_image(user_text, color, style, technique):
#     try:
#         # Construct the prompt based on user's selections
#         tattoo_prompt = (
#             f"Can you create a tattoo design that matches the following description:\n"
#             f"- Style: {style}\n"
#             f"- Technique: {technique}\n"
#             f"- Color: {color}\n"
#             f"- Description: {user_text}\n"
#             "Please ensure that the design looks like it was hand-drawn by a tattoo artist on paper, "
#             "with no background. The image should be displayed on a white surface to simulate a clean canvas."
#         )
        
#         # Call OpenAI API to get image
#         response = client.images.generate(
#             model="dall-e-3",
#             prompt=tattoo_prompt,
#             size="1024x1024",
#             quality="standard",
#             n=1
#         )
        
#         # Assuming the response structure has the image URL at response['data'][0]['url']
#         image_url = response.data[0].url # Adjust according to the actual response structure

#         # Display the image
#         st.image(image_url, caption="Generated Image")

#         # Append the assistant's message with the image URL
#         st.session_state.messages.append({"role": "assistant", "content": image_url})
#     except Exception as e:
#         st.error(f"Error generating image: {e}")

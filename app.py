import streamlit as st
from openai import OpenAI

OpenAI.api_key = st.secrets["OPENAI_API_KEY"]

import streamlit as st

# Set the background image for the sidebar
background_image_url = "images/tattooBckImg1.png"
st.markdown(f"""
    <style>
        .main {{
            background-image: url('{background_image_url}');
            background-size: cover;
            background-repeat: no-repeat;
        }}
    </style>
    """, unsafe_allow_html=True)


title_text = "Tattoo? Yes Please!"
st.markdown(f"<h1 style='text-align: center;'>{title_text}</h1>", unsafe_allow_html=True)


# Assuming color_options and technique_options are defined elsewhere in your code
color_options = ["b/w", "color"]
technique_options = ["basic", "traditional/old-school", "tribal", "japanese"]


# Initialize session state if not already set
if 'selected_color' not in st.session_state:
    st.session_state['selected_color'] = color_options[0]
if 'selected_technique' not in st.session_state:
    st.session_state['selected_technique'] = technique_options[0]
if 'user_message' not in st.session_state:
    st.session_state['user_message'] = ''

# Sidebar widgets
st.sidebar.selectbox("Would you like your tattoo in black and white or in color?", color_options, key='selected_color')
st.sidebar.selectbox("Choose the technique for your tattoo:", technique_options, key='selected_technique')
st.sidebar.text_input("Describe the idea you have for your tattoo:", key='user_message')

# Submit button
if st.sidebar.button('Generate'):
    # Check if user_message is not empty
    if st.session_state['user_message']:
        # Initialize OpenAI client
        client = OpenAI()
        
        # Prepare the prompt
        tattoo_prompt = f"{st.session_state['selected_color']} and {st.session_state['selected_technique']} tattoo: "
        
        # Generate the image
        response = client.images.generate(
            model="dall-e-3",
            prompt=tattoo_prompt + st.session_state['user_message'], 
            quality="hd",
            style="vivid",
            n=1,
            size="1024x1024"
        )
        
        # Get the image URL
        image_url = response.data[0].url
        
        # Display generated image
        st.image(image_url)
    else:
        st.error("Please enter a description for your tattoo.")




# Assuming you have a function to generate your image
def generate_image():
    # Your image generation logic here
    # This is just a placeholder for your actual image generation function
    return "https://example.com/path/to/your/generated/image.png"

# Generate the image
generated_image_url = generate_image()

# Overlay the generated image on top of the background image
st.markdown(f"""
    <div style="position: relative; width: 100%; height: 100%;">
        <img src="{generated_image_url}" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
    </div>
    """, unsafe_allow_html=True)

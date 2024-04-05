from openai import OpenAI
import streamlit as st

# Initialize the OpenAI client with API key
OpenAI.api_key = st.secrets["OPENAI_API_KEY"]

title_text = "Tattoo? Yes Please!"

import streamlit as st

# Set the background image
st.markdown(
    """
    <style>
    .reportview-container {
        background: url('/images/tattooBckImg1.png') no-repeat center center fixed; 
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Your Streamlit app code goes here


# Apply HTML/CSS attributes
st.markdown(f"<h1 style='text-align: center;'>{title_text}</h1>", unsafe_allow_html=True)

# Business name and information
st.write("Tattoo? Yes, Please! Because when someone asks if you want a tattoo, it's more than a simple yes or no. We take"\
"the complications out of the equation and create something you can take in and get tattooed. Have you ever wanted a tattoo,"\
"but struggled to articulate what you want? We'll conjure a sketch that's as unique as your fingerprint as personal as your"\
"story. Let's make your tattoo dreams a reality. Let's create something that's not just ink on skin but a piece of your soul"\
"etched in time. Manifest your ideas into reality with Tattoo Yes Please.")




# Define options for user to select
color_options = ["b/w", "color"]
technique_options = ["basic", "traditional/old-school", "tribal", "japanese"]


    # Collect user input for the tattoo options
with st.form(key="user_input_form"):
    selected_color = st.selectbox("Would you like your tattoo in black and white or in color?", color_options)
    selected_technique = st.selectbox("Choose the technique for your tattoo:", technique_options)
    user_message = st.text_input("Describe the idea you have for your tattoo:")
    submitted = st.form_submit_button(label="Generate")

    # Custom prompt that will be added with 'user prompt' to get desired 'tattoo sketch effect'
   
tattoo_prompt = (
    
    f"Generate a sketched image that should depict {user_message} using the {selected_technique} technique and in {selected_color}." 
    f"Ensure the image is complete, on a white canvas with a blank background." 
    f"The image should accurately reflect the user's selections without adding unexpected elements or colors." 
    f"Avoid including tattoos on any objects in the image."

)

        # Generate the image
if submitted and user_message:  
    client = OpenAI()
    response = client.images.generate(
        model="dall-e-3",
        prompt=tattoo_prompt + user_message, 
        quality="hd",
        style="vivid",
        n=1,
        size="1024x1024"
    )

        # Get the image URL
    image_url = response.data[0].url

        # Display generated image
    st.image(image_url)    
    st.markdown(f"[Send me this image!](https://your-email-form-page.com)")



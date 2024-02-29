### Documentation for Tattoo Stencil Image Generator

#### Introduction
The Tattoo Stencil Image Generator is an application designed to turn text descriptions into visual black and white tattoo stencil images. Leveraging the power of OpenAI's DALL·E 3 model through a simple and interactive Streamlit interface, users can input their tattoo ideas and receive artistically generated images that match their descriptions. This document serves as a guide to understanding and navigating the application. I had trouble with the module openai, depending on what versions of everything youre running, you may need to use"from openai import OpenAI" instead of importing the whole module. 

#### Setting Up the Environment
To run the Tattoo Stencil Image Generator, you will need Python installed on your system along with the Streamlit and OpenAI libraries. Ensure you have the following prerequisites:
1. Python 3.6 or later.
2. An OpenAI API key to access DALL·E 3.

##### Installation Steps:
1. **Install Streamlit:** Run the command `pip install streamlit` in your terminal or command prompt.
2. **Install OpenAI:** Run `pip install openai` to install the OpenAI library.
3. **API Key Configuration:** The application assumes your OpenAI API key is securely stored. You can use Streamlit's secrets management for local development or set it as an environment variable.
4. **Without Streamlit:***Just take out the streamlit syntax and it should just run in a python interpreter or your ide you use just fine.

##### Message Initialization
Upon application start-up, a default set of messages is initialized in Streamlit's session state. This includes a system message explaining the application's purpose and a placeholder for the assistant's generated content.

##### User Text Input
Via a Streamlit text input field, users can submit their tattoo ideas. This input acts as the "prompt" for the DALL·E 3 model to generate an image.

##### Image Generation and Display
Upon receiving user input, the application calls the `generate_and_append_image` function. This function performs the following operations:
* Appends the user's message to the session state.
* Makes an API call to OpenAI's DALL·E 3 model with the user's text, requesting a 1024x1024 standard quality image.
* Retrieves the URL of the generated image from the API's response.
* Displays the generated image in the Streamlit interface.
* Appends a new message to the session state with the image URL for reference.

##### User Interaction
The application provides a straightforward workflow:
1. **Enter Your Idea:** Users fill in the text input field with their tattoo concept or idea.
2. **Generate:** By pressing the "Generate" button, the application procures a stencil image that corresponds to the provided text description.
3. **View and Iterate:** Users can view the generated image, then modify their input and regenerate images as needed.

#### Security and API Key Management
Securing the OpenAI API key is crucial. The application leverages Streamlit's secrets management for development and suggests environment variables for production environments to keep the API key secure.

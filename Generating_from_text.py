

import torch
from diffusers import StableDiffusionPipeline
import gradio as gr
from PIL import Image
import os

# Determine the device to use: GPU (cuda) if available, otherwise CPU
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the Stable Diffusion model and configure it to run on the appropriate device
text_to_image_model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to(device)

# Create the main history directory
history_dir = "/content/History"
os.makedirs(history_dir, exist_ok=True)

# Function to generate and save an image and prompt from text
def generate_and_save_image(prompt):
    # Calculate the index based on the number of existing directories in Generated_Images
    index = len([name for name in os.listdir(history_dir) if name.startswith("Generated_Images")]) + 1

    # Create a new directory for this prompt and image
    image_dir = os.path.join(history_dir, f"Generated_Images{index}")
    os.makedirs(image_dir, exist_ok=True)

    # Define file paths for saving the image and prompt (without index in file names)
    image_file_path = os.path.join(image_dir, "generated_image.png")
    prompt_file_path = os.path.join(image_dir, "prompt.txt")

    # Save the prompt to a text file
    with open(prompt_file_path, "w") as f:
        f.write(prompt)

    # Generate the image from the prompt
    images = text_to_image_model(prompt).images

    # Display the generated image
    images[0].show()

    # Save the image to the specified file path
    images[0].save(image_file_path)

    return image_file_path

# Function to handle image generation
def handle_generation(prompt):
    # Generate and save the image and prompt
    file_path = generate_and_save_image(prompt)

    # Load the saved image
    image = Image.open(file_path)

    return image

# Gradio UI setup
with gr.Blocks() as demo:
    gr.Markdown("# Generate Image from Text (it works better without living things like people, dogs, etc.)")

    # Input field for the user to describe the image they want to generate
    prompt = gr.Textbox(label="Describe the image you want to generate (Write in English please)")

    # Submit button for image generation
    submit_btn = gr.Button("Submit")

    # Image output
    image_output = gr.Image(label="Generated Image")

    # Handle submit button click
    submit_btn.click(
        fn=handle_generation,
        inputs=[prompt],
        outputs=[image_output]
    )

# Launch the Gradio interface
demo.launch()

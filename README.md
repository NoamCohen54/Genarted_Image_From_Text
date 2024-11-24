# Genarted_Image_From_Text with Stable Diffusion and Gradio
This project generates images from text descriptions using the Stable Diffusion model.

## How It Works
1. **Input a Text Prompt**: Describe the image you want to generate in English.
2. **Generate Image**: The Stable Diffusion model creates an image based on your description.
3. **Save and Display**: Each generated image is saved to a unique folder with the text prompt.

## Features
- **Automatic GPU/CPU Detection**: The program uses a GPU if available; otherwise, it runs on the CPU.
- **Image and Prompt History**: Each generated image is stored in the `/content/History` folder along with the prompt that created it.
- **Gradio Interface**: An easy-to-use interface lets users input text prompts and view generated images.

## Using the Interface
- Enter a description of the image you want.
- Press **Submit** to generate and view the image.

## Directory Structure
- **/content/History/Generated_Images***: A directory is created for each image with the prompt text and image file.

## Requirements
Install the necessary libraries with:
```bash
pip install transformers diffusers gradio pillow

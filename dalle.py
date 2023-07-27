# pip install openai
import openai
import os
from dotenv import load_dotenv

# Load variables from .env file into the environment
load_dotenv()

# Now you can access the variables using the os.environ dictionary
dalle_key = os.environ.get("DALLE_KEY")
# Your OpenAI API key
openai.api_key = dalle_key

# how many images do you want
image_count = 10
i = 0

while (i < image_count):
    i = i + 1

    print(f"Generating image #{i}")
    
    # The text prompt you want to use to generate an image
    prompt = "a high resolution 8bit Jeep top down, with no background"

    # Generate an image
    response = openai.Image.create(
        prompt=prompt,
        model="image-alpha-001",
        size="1024x1024",
        response_format="url"
    )

    # Print the URL of the generated image
    print(response["data"][0]["url"])


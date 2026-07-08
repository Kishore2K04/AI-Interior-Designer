import os
import replicate
from dotenv import load_dotenv

load_dotenv()

client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

def generate_room(image_path, style):

    prompt = (
        f"Redesign this bedroom in {style} interior style. "
        "Keep the room layout exactly the same. "
        "Do not move the bed, wardrobe, windows, doors or furniture. "
        "Only change colors, materials, lighting and decorations."
    )

    with open(image_path, "rb") as img:

        output = client.run(
            "black-forest-labs/flux-kontext-pro",
            input={
                "input_image": img,
                "prompt": prompt,
                "aspect_ratio": "match_input_image",
                "output_format": "jpg",
                "prompt_upsampling": False,
                "safety_tolerance": 2
            }
        )

    return str(output.url)
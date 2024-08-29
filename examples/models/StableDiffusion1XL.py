from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
from krutrim_cloud.lib.utils import convert_base64_to_PIL_img
from krutrim_cloud.lib.utils import convert_base64_to_OpenCV_img

load_dotenv()
client = KrutrimCloud()

try:
    stable_diffusion_response = client.images.generations.diffusion(
        model_name="diffusion1XL", image_height=1024, image_width=1024, prompt="dog with hat on beach"
    )
    print(f"Number of Images created: {stable_diffusion_response.created}")
    print(f"Error: {stable_diffusion_response.error}")

    # Access each generated image
    for index, data in enumerate(stable_diffusion_response.data, start=1):
        OpenCV_img = convert_base64_to_OpenCV_img(data["b64_json"])
        # OR
        PIL_img = convert_base64_to_PIL_img(data["b64_json"])

        # Process the image as per your requirements
    # OR

    # Store generated images in local storage
    stable_diffusion_response.save(output_dirpath="./output")  # Optional: filename="your-output-name.png"
except Exception as exc:
    print(f"Exception: {exc}")

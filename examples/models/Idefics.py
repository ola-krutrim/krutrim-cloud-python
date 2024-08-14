from krutrim_cloud import KrutrimCloud
from PIL import Image
from dotenv import load_dotenv
from krutrim_cloud.lib.utils import convert_PIL_image_to_base64

load_dotenv()

client = KrutrimCloud()

PIL_img_1 = Image.open("../resources/Skyline-Chicago.jpg")
enc_img_1 = convert_PIL_image_to_base64(PIL_img_1, format="JPEG")

images = [[enc_img_1], []]
prompts = ["<image>", "what is the city??"]

try:
    response = client.multimodal.generations.idefics(
        model_name="idefics", prompts=prompts, images=images, max_tokens=50
    )
    # Access generated output
    print(f"Output: {response.generated_texts}")
    # OR

    # Store generated output in local storage
    response.save(output_dirpath="./output")

except Exception as exc:
    print(f"Exception: {exc}")

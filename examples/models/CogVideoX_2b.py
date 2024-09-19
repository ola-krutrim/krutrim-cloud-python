from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
from krutrim_cloud.lib.utils import convert_base64_to_PIL_img, create_video_clip
import os

load_dotenv()

client = KrutrimCloud()

prompt = [
    "A detailed wooden toy ship with intricately carved masts and sails is seen gliding smoothly over a plush, blue carpet that mimics the waves of the sea. The ship's hull is painted a rich brown, with tiny windows. The carpet, soft and textured, provides a perfect backdrop, resembling an oceanic expanse. Surrounding the ship are various other toys and children's items, hinting at a playful environment. The scene captures the innocence and imagination of childhood, with the toy ship's journey symbolizing endless adventures in a whimsical, indoor setting."
]

try:
    response = client.videos.generations.text2video.create(
        model_name="cogvideo",
        prompt=prompt,
        guidance_scale=6,
        num_frames=10,
        num_inference_steps=30,
        num_videos_per_prompt=1,
    )
    # Decode video frames
    video_frames = []
    for res in response.data:
        frame = convert_base64_to_PIL_img(res["b64_json"])
        video_frames.append(frame)
    # Create a video clip from the generated frames
    video = create_video_clip(video_frames=video_frames)
    if not os.path.exists("./output"):
        os.mkdir("./output")
    video.write_videofile(os.path.join("./output", "output.mp4"), fps=8)

    # OR
    # Store the generated video frames as a video
    response.save(output_dirpath="./output", filename="output.mp4", fps=10)

except Exception as exc:
    print(f"Exception: {exc}")

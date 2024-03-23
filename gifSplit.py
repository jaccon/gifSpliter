import os
from PIL import Image
import imageio

def gifToFrames(gif_path, output_folder):
    gif = imageio.mimread(gif_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, frame in enumerate(gif):
        image = Image.fromarray(frame)

        image.save(os.path.join(output_folder, f"frame_{i}.png"))

    print(f"{len(gif)} frames extraídos e salvos em {output_folder}")

gif_path = "assets/cow3.gif" 
output_folder = "spliter" 
gifToFrames(gif_path, output_folder)

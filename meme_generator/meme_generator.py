import os
import random
from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """The class that is responsible to generating the memes."""

    def __init__(self, output_dir):
        """Create the output directory."""
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500):
        """Create a meme using the parameters image, text and author."""
        image = Image.open(img_path)
        outfile = os.path.join(self.output_dir, f"{random.randint(0,9999999999)}.jpg")
        real_width, real_height = image.size

        height = int(real_height * width / real_width)
        image.thumbnail((width, height))

        quote_font = ImageFont.truetype(
            "./_data/Fonts/LilitaOne-Regular.ttf", 22)
        author_font = ImageFont.truetype(
            "./_data/Fonts/LilitaOne-Regular.ttf", 18)
        draw = ImageDraw.Draw(image)
        draw.text((30, 10), text,  font=quote_font, fill='black')
        draw.text((40, 40), f"- {author}", font=author_font, fill='black')

        image.save(outfile, "JPEG")
        return outfile

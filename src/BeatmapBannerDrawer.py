import pathlib

from OsuFileParser import BeatmapFileParser, BeatmapData
from PIL import Image, ImageDraw, ImageFont, ImageColor

from src.TextParser import TextParser


class BeatmapBannerDrawer:
    def __init__(self, file_path: pathlib.Path | str):
        """
        :param file_path: Osu file path or Image path
        """
        if isinstance(file_path, str):
            file_path = pathlib.Path(file_path)

        self.beatmap_data = BeatmapData(BeatmapFileParser.parse_full_osu_file(file_path))
        self.image = Image.open(file_path.parent / pathlib.Path(self.beatmap_data.events.background_filename))

    def draw_border(self, *, thickness, color):
        if thickness == 0:
            return

        draw = ImageDraw.Draw(self.image, "RGBA")
        image_width, image_height = self.image.size

        # Further parsing arguments
        if isinstance(thickness, float):
            thickness = int(min(image_width, image_height) * thickness)

        if isinstance(color, str):
            try:
                color = ImageColor.getrgb(color)
            except ValueError:
                raise ValueError(f"Invalid color name: {color}")
        ##############################

        for i in range(thickness):
            opacity = max(0, int(255 - (i + 1) * 255 / thickness))  # Calculate opacity based on thickness
            border_color = color + (opacity,)  # Add opacity value to RGB color tuple
            left = i
            top = i
            right = image_width - i - 1
            bottom = image_height - i - 1
            try:
                draw.rectangle((left, top, right, bottom), outline=border_color)
            except ValueError:  # Check for bad coordinates
                pass

    def draw_text_centered(self, text, *, font_family, font_size, font_color):
        if font_size == 0:
            return

        draw = ImageDraw.Draw(self.image)
        image_width, image_height = self.image.size

        # Further parsing arguments
        if isinstance(font_size, float):
            font_size = int(min(image_width, image_height) * font_size)

        text = TextParser.parse_text(text, beatmap_data=self.beatmap_data)

        if isinstance(font_color, str):
            try:
                font_color = ImageColor.getrgb(font_color)
            except ValueError:
                raise ValueError(f"Invalid color name: {font_color}")
        ###########################

        font = ImageFont.truetype(str(font_family), font_size)

        bbox = draw.multiline_textbbox((0, 0), text, font=font)
        center_x = image_width // 2
        center_y = image_height // 2
        bbox_center_x = (bbox[0] + bbox[2]) // 2
        bbox_center_y = (bbox[1] + bbox[3]) // 2
        offset_x = center_x - bbox_center_x
        offset_y = center_y - bbox_center_y
        try:
            draw.multiline_text((bbox[0] + offset_x, bbox[1] + offset_y), text, font=font, fill=font_color,
                                align="center")
        except ValueError:  # Check for bad coordinates
            pass

    def crop_image(self, *, crop_vertical_size):
        if crop_vertical_size == 0:
            return

        image_width, image_height = self.image.size

        # Further parsing arguments
        if isinstance(crop_vertical_size, float):
            crop_vertical_size = int(min(image_width, image_height) * crop_vertical_size)

        ###########################

        left = 0
        top = crop_vertical_size
        right = image_width
        bottom = image_height - crop_vertical_size
        try:
            self.image = self.image.crop((left, top, right, bottom))
        except ValueError:  # Check for bad coordinates
            pass

    def save_image(self, output_path):
        self.image.save(output_path)

    def __del__(self):
        # Close the image file
        self.image.close()

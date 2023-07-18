import argparse

import yaml

from src.ArgumentParser import ArgumentParser
from src.BeatmapBannerDrawer import BeatmapBannerDrawer


def exec_main(args):
    # Pre-parsing arguments for BeatmapBannerDrawer class to accept them
    with open(args.style, 'r') as file:
        data = yaml.safe_load(file)
        parameters = data['parameters']
        border_thickness = ArgumentParser.parse_size_value(parameters['border-thickness'])
        border_color = ArgumentParser.parse_color_value(parameters['border-color'])
        font_size = ArgumentParser.parse_size_value(parameters['font-size'])
        font_color = ArgumentParser.parse_color_value(parameters['font-color'])
        font_family = ArgumentParser.parse_font_family_value(parameters['font-family'])
        text = ArgumentParser.parse_text_value(parameters['text'])

    input_file = args.input_file
    output_file_path = args.output

    beatmap_banner_drawer = BeatmapBannerDrawer(input_file)
    beatmap_banner_drawer.draw_border(thickness=border_thickness, color=border_color)
    beatmap_banner_drawer.draw_text_centered(text, font_size=font_size,
                                             font_color=font_color,
                                             font_family=font_family)

    beatmap_banner_drawer.save_image(output_file_path)
    print(f"Saved file to: {output_file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CLI application for generating beatmap banner from the given parameters. "
                    "Just a mini pillow script.")

    parser.add_argument("input_file", help="Path to the '.osu' map file (only for standard mode). "
                                           "Or path to the Image file.")

    parser.add_argument("-o", "--output", required=True, help="Specify the output file path.")
    parser.add_argument("-s", "--style", default="data/styles/default-style.yaml", help="Style '.yaml' file path.")

    args = parser.parse_args()
    exec_main(args)

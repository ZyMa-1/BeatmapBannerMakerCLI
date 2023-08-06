import pathlib

from PIL import ImageColor

from src.PathManager import PathManager


class ArgumentParser:
    @staticmethod
    def parse_px_value(arg: str) -> int:
        if arg[-2:] == 'px':
            val = int(arg[:-2])
            if val >= 0:
                return val
            else:
                raise ValueError("Bad argument.")
        else:
            raise ValueError("Bad argument.")

    @staticmethod
    def parse_size_value(arg: str) -> int | float:
        if arg[-1] == '%':
            val = float(arg[:-1]) / 100
            if 0 <= val <= 1:
                return val
            else:
                raise ValueError("Bad argument.")
        elif arg[-2:] == 'px':
            val = int(arg[:-2])
            if val >= 0:
                return val
            else:
                raise ValueError("Bad argument.")
        else:
            raise ValueError("Bad argument.")

    @staticmethod
    def parse_color_value(arg: str) -> tuple | str:
        if len(arg.split(',')) == 3:
            args = arg.split(',')
            try:
                args = [int(arg) for arg in args]
            except ValueError:
                raise ValueError("Bad argument.")
            if not all(0 <= int(arg) <= 255 for arg in args):
                raise ValueError("Bad argument.")
            return tuple(args)
        elif isinstance(arg, str) and arg[0] == '#' and len(arg) == 7:
            arg = arg[1:]
            r = int(arg[0:2], 16)
            g = int(arg[2:4], 16)
            b = int(arg[4:6], 16)
            if not all(0 <= int(arg) <= 255 for arg in [r, g, b]):
                raise ValueError("Bad argument.")
            return r, g, b
        elif isinstance(arg, str):
            try:
                arg = ImageColor.getrgb(arg)
            except ValueError:
                raise ValueError(f"Invalid color name: {arg}")
            return arg
        else:
            raise ValueError("Bad argument.")

    @staticmethod
    def parse_font_family_value(arg: str) -> pathlib.Path:
        if arg == 'default':
            val = pathlib.Path(PathManager.PROJECT_ROOT / r"data/fonts/SourceCodePro-Regular.ttf")
            return val
        else:
            val = pathlib.Path(arg)
            return val

    @staticmethod
    def parse_text_value(arg: list | str) -> list:
        if isinstance(arg, str) and arg == 'default':
            return ["{artist} - {title}", "Beatmap by {creator}"]
        elif isinstance(arg, list):
            return arg
        else:
            raise ValueError("Bad argument.")

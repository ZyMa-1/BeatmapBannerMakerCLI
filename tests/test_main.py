import argparse
import unittest

from main import exec_main_parameters
from src.PathManager import PathManager
from tests.StyleValuesGenerator import StyleValuesGenerator as SVGen
from tests.TestDataGenerator import TestDataGenerator as TDGen


def generate_args_and_parameters(pre_data):
    for current_test_data in TDGen.generate_test_data_from_dict(pre_data):
        data = {'parameters': current_test_data}

        if len(pre_data) != len(data['parameters']):
            raise ValueError("Invalid test pre-data.")

        # Create the arguments object with the test case values
        args = argparse.Namespace(
            input_file=str(PathManager.PROJECT_ROOT / "tests" / "input" / "Hensonn - Sahara (SMOKELIND) [X].osu"),
            output=str(PathManager.PROJECT_ROOT / "tests" / "res" / "temp-res.png"),
            style=str(PathManager.PROJECT_ROOT / "tests" / "temp-style.yaml"),
        )
        parameters = data['parameters']

        yield args, parameters


class TestApp(unittest.TestCase):
    def test_main_valid(self):
        pre_data = {
            'border-thickness': SVGen.generate_size_valid_values(),
            'border-color': SVGen.generate_color_valid_values(),
            'font-size': SVGen.generate_size_valid_values(),
            'bg-crop-vertical-size': SVGen.generate_size_valid_values(),
            'font-color': SVGen.generate_color_valid_values(),
            'font-family': SVGen.generate_font_family_valid_values(),
            'text': SVGen.generate_text_valid_values(),
            'text-outline-thickness': SVGen.generate_px_valid_values(),
            'text-outline-color': SVGen.generate_color_valid_values(),
            'bg-blur-radius': SVGen.generate_px_valid_values()
        }

        for args, parameters in generate_args_and_parameters(pre_data):
            exec_main_parameters(args=args, parameters=parameters, save_image=False)

    def test_main_invalid(self):
        pre_data = {
            'border-thickness': SVGen.generate_size_bad_values(),
            'border-color': SVGen.generate_color_bad_values(),
            'font-size': SVGen.generate_size_bad_values(),
            'crop-vertical-size': SVGen.generate_size_bad_values(),
            'font-color': SVGen.generate_color_bad_values(),
            'font-family': SVGen.generate_font_family_bad_values(),
            'text': SVGen.generate_text_bad_values()
        }

        for args, parameters in generate_args_and_parameters(pre_data):
            self.assertRaises((OSError, ValueError),
                              lambda: exec_main_parameters(args=args, parameters=parameters, save_image=False))


if __name__ == "__main__":
    unittest.main()

import argparse
import unittest

from main import exec_main_parameters
from src.PathManager import PathManager
from tests.StyleValuesGenerator import StyleValuesGenerator as SVGen
from tests.TestDataGenerator import TestDataGenerator as TDGen


def generate_args_and_parameters(pre_data):
    for current_test_data in TDGen.generate_test_data(pre_data):
        data = {
            'parameters': {
                'border-thickness': current_test_data[0],
                'border-color': current_test_data[1],
                'font-size': current_test_data[2],
                'font-color': current_test_data[3],
                'font-family': current_test_data[4],
                'text': current_test_data[5]
            }
        }

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
        pre_data = [SVGen.generate_size_valid_values(),
                    SVGen.generate_color_valid_values(),
                    SVGen.generate_size_valid_values(),
                    SVGen.generate_color_valid_values(),
                    SVGen.generate_font_family_valid_values(),
                    SVGen.generate_text_valid_values()]

        for args, parameters in generate_args_and_parameters(pre_data):
            exec_main_parameters(args=args, parameters=parameters, save_image=False)

    def test_main_bad(self):
        pre_data = [SVGen.generate_size_bad_values(),
                    SVGen.generate_color_bad_values(),
                    SVGen.generate_size_bad_values(),
                    SVGen.generate_color_bad_values(),
                    SVGen.generate_font_family_bad_values(),
                    SVGen.generate_text_bad_values()]

        for args, parameters in generate_args_and_parameters(pre_data):
            self.assertRaises((OSError, ValueError),
                              lambda: exec_main_parameters(args=args, parameters=parameters, save_image=False))


if __name__ == "__main__":
    unittest.main()

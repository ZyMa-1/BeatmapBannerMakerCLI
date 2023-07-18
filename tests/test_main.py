import argparse
import unittest

import yaml

from main import exec_main
from src.PathManager import PathManager
from tests.StyleValuesGenerator import StyleValuesGenerator as SVGen
from tests.TestDataGenerator import TestDataGenerator as TDGen


def generate_args(pre_data):
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

        with open('temp-style.yaml', 'w') as file:
            yaml.dump(data, file)

        # Create the arguments object with the test case values
        args = argparse.Namespace(
            input_file=str(PathManager.PROJECT_ROOT / "tests" / "input" / "Hensonn - Sahara (SMOKELIND) [X].osu"),
            output=str(PathManager.PROJECT_ROOT / "tests" / "res" / "temp-res.png"),
            style=str(PathManager.PROJECT_ROOT / "tests" / "temp-style.yaml"),
        )

        yield args


class TestApp(unittest.TestCase):
    def test_main_valid(self):
        pre_data = [SVGen.generate_size_valid_values(),
                    SVGen.generate_color_valid_values(),
                    SVGen.generate_size_valid_values(),
                    SVGen.generate_color_valid_values(),
                    SVGen.generate_font_family_valid_values(),
                    SVGen.generate_text_valid_values()]

        for args in generate_args(pre_data):
            exec_main(args)

    def test_main_bad(self):
        pre_data = [SVGen.generate_size_bad_values(),
                    SVGen.generate_color_bad_values(),
                    SVGen.generate_size_bad_values(),
                    SVGen.generate_color_bad_values(),
                    SVGen.generate_font_family_bad_values(),
                    SVGen.generate_text_bad_values()]

        for args in generate_args(pre_data):
            self.assertRaises((OSError, ValueError), lambda: exec_main(args))


if __name__ == "__main__":
    unittest.main()

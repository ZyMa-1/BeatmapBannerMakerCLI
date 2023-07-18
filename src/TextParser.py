import re

from OsuFileParser import BeatmapData


def _extract_variables_from_fstring(fstring):
    variable_pattern = r"{(.*?)}"
    variables = re.findall(variable_pattern, fstring)
    return variables


def _add_prefix_to_fstring_variables(fstring, prefix):
    variable_pattern = r"{(.*?)}"
    prefixed_fstring = re.sub(variable_pattern, lambda match: "{" + prefix + match.group(1) + "}", fstring)
    return prefixed_fstring


class TextParser:
    supported_variables = {'title', 'title_unicode', 'artist', 'artist_unicode', 'creator', 'source', 'beatmap_id',
                           'beatmap_set_id'}

    @classmethod
    def parse_text(cls, text: list, *, beatmap_data: BeatmapData) -> str:
        prefix = "beatmap_data.metadata."

        res = ""
        for line in text:
            extracted_variables = set(_extract_variables_from_fstring(line))

            if not extracted_variables.issubset(cls.supported_variables):
                raise ValueError("Bad argument. Template variables are not supported.")

            # Add prefix to all variables
            formatted_string = _add_prefix_to_fstring_variables(line, prefix)
            fstring_string = formatted_string.format(**locals())

            res += fstring_string
            res += "\n"

        return res

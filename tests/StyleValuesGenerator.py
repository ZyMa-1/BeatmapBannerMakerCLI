class StyleValuesGenerator:
    @staticmethod
    def generate_px_valid_values():
        return ["0px", "10px", "50px", "1000px"]

    @staticmethod
    def generate_px_bad_values():
        return ["-1px", "-2px", "-2.0px"]

    @staticmethod
    def generate_size_valid_values():
        return ["0%", "10%", "50.5%", "99%", "100%", "0px", "10px", "50px", "1000px"]

    @staticmethod
    def generate_size_bad_values():
        return ["-1%", "101%", "-1px", "-2px", "-2.0px"]

    @staticmethod
    def generate_color_valid_values():
        return ['white', 'black', 'red', 'blue', "0,0,0", "255,255,255", "255,0,0", "255, 125, 125",
                "#a4eb34", "#ffffff", "#000000"]

    @staticmethod
    def generate_color_bad_values():
        return ["color_name_that_does_not_exists", "-1,0,0", "#gggggg", "#-1-1-1-1", "#0123gf", "#0000000"]

    @staticmethod
    def generate_font_family_valid_values():
        return ["default"]

    @staticmethod
    def generate_font_family_bad_values():
        return ["other"]

    @staticmethod
    def generate_text_valid_values():
        non_f_string = ["Amogus123", "Python nerd", "Osu virgin"]
        f_string = ["{artist}{title}{title_unicode}{artist_unicode}", "{creator}{source}{beatmap_id}",
                    "{beatmap_set_id}"]
        concat_string = non_f_string + f_string
        return [non_f_string, f_string, concat_string]

    @staticmethod
    def generate_text_bad_values():
        non_f_string = ["Amogus123", "Python nerd", "Osu virgin"]
        f_string = ["{amogus}{bad}{123}{artist_unicode}"]
        concat_string = non_f_string + f_string

        return [f_string, concat_string]

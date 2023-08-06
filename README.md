# BeatmapBannerMakerCLI
[![GitHub release](https://img.shields.io/github/release/ZyMa-1/BeatmapBannerMakerCLI.svg?style=for-the-badge&logo=github)](https://github.com/ZyMa-1/BeatmapBannerMakerCLI/releases/latest) 
<br>
<br>
[![Python Version](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![Licence MIT](https://img.shields.io/badge/License-MIT-purple.svg)](/LICENCE)
![Test Status](https://github.com/ZyMa-1/BeatmapBannerMakerCLI/actions/workflows/tests.yml/badge.svg?branch=main)


CLI script dedicated to manipulating image using `Pillow` library.
Generate beatmap banner by enhancing background file with a border and a text.

## CLI '--help' thingy
 
```
usage: main.py [-h] -o OUTPUT [-s STYLE] input_file 

CLI application for generating beatmap banner from the given parameters. Just a mini pillow script.

positional arguments:
  input_file            Path to the '.osu' map file (only for standard mode). Or path to the Image file.

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Specify the output file path.
  -s STYLE, --style STYLE
                        Style '.yaml' file path.
```


## Simple Usage of the '.py' file

```bash
python main.py "path_to_your_osu!_folder\Songs\1965625 Azari - Black Out\Azari - Black Out (Ryuusei Aika) [----].osu" --output res/result2.png
```

## Simple Usage of the '.exe' file

```bash
 .\beatmap_banner_maker_v1.2.exe "path_to_your_osu!_folder\Songs\Hensonn - Sahara (SMOKELIND) [X].osu" -o res/test.png
```

## Further explanation

Resulted image would look like that:

![Result](readme_images/result2.png)

It is not the best quality cause I'm not a designer of any sort.

Under curtains, my script loads `default-style.yaml` file which looks like that:

```yaml
####################
#
# border-thickness: {int number}px              |  Thickness in pixels
# border-thickness: {float number}%             |  Border thickness in pixels relative to min(width, height)
#
# border-color: {string}                        |  Name of the color: "black", "white", etc.
# border-color: {HEX string}                    |  Hex string of the color. For example #4287f5, #ffffff, etc.
# border-color: {0-255},{0-255},{0-255}         |  RGB color
#
# font-size: {int number}px                     |  Font size in pixels
# font-size: {float number}%                    |  Font size in pixels relative to min(width, height)
#
# bg-crop-vertical-size: {int number}px         |  Crop image from the top and the bottom by a given amount of pixels
# bg-crop-vertical-size: {float number}%        |  Crop image from the top and the bottom by a given amount of pixels
#                                               |                                       relative to min(width, height)
#
# font-color: {string}                          |  Name of the color: "black", "white", etc.
# font-color: {HEX string}                      |  Hex string of the color. For example #4287f5, #ffffff, etc.
# font-color: {0-255},{0-255},{0-255}           |  RGB color
#
# font-family: {string}                         |  Path to the 'ttf' font file
# font-family: default                          |  'data/fonts/SourceCodePro-Regular.ttf'
#
# text: YAML list of python f-strings           |
# text: default                                 |  ["{artist} - {title}", "Beatmap by {creator}"]
#
# Available f-strings: ('title', 'title_unicode', 'artist', 'artist_unicode',
#                       'creator', 'source', 'beatmap_id', 'beatmap_set_id')
#                      I.e.  Some metadata
#
#
# text-outline-thickness: {int}px               |  Thickness radius, recommended to specify it in px
#
# text-outline-color: {string}                  |  Name of the color: "black", "white", etc.
# text-outline-color: {HEX string}              |  Hex string of the color. For example #4287f5, #ffffff, etc.
# text-outline-color: {0-255},{0-255},{0-255}   |  RGB color
#
# bg-blur-radius: {int}px                       |  Gaussian blur specified in px
#
###################
parameters:
  border-thickness: 5%
  border-color: white
  font-size: 60px
  bg-crop-vertical-size: 15%
  font-color: white
  font-family: default
  text: default
  text-outline-thickness: 2px
  text-outline-color: black
  bg-blur-radius: 10px
```

You can specify some parameters there and further pass `your_style.yaml` path to the script using `--style` or `-s` parameter.  
  
Also as you may notice in the default `yaml` file is some sort of documentation, you can refer to it when changing parameters.


P.S

One more example:

![Result](readme_images/result1.png)

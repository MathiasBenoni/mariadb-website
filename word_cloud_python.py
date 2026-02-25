from os import read

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

size_x = 400
size_y = 400

separator = ' '

def make_cloud(x):
    if x:
        words = [
            adj.capitalize()
            for i in range(0, len(x), 2)
            for adj in [x[i]] * x[i + 1]
        ]

        
        text = separator.join(words)
        #text = open("text.txt", 'r').read()

        # Load and resize FIRST
        mask_image = Image.open("images/github.png")
        mask_image = mask_image.resize((size_x, size_y))

        # Convert to numpy array
        python_mask = np.array(mask_image)

        # Create color generator from the numpy array
        colourmap = ImageColorGenerator(python_mask)

        # Dark version
        wc = WordCloud(mask=python_mask,
                    background_color="black",
                    max_words=2000,
                    width=size_x,
                    height=size_y,
                    min_font_size=2).generate(text)

        wc.recolor(color_func=colourmap)
        wc.to_file("static/images/cloud_dark.png")

        # Light version
        wc = WordCloud(mask=python_mask,
                    background_color="white",
                    max_words=2000,
                    width=size_x,
                    height=size_y,
                    min_font_size=2).generate(text)

        wc.recolor(color_func=colourmap)
        wc.to_file("static/images/cloud_light.png")
    else:
        return "NOPE"

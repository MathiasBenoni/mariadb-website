import matplotlib
matplotlib.use('Agg')
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

size_x = 400
size_y = 400

def make_cloud(adjectives: dict):
    if not adjectives:
        return "NOPE"

    else:
        # Capitalize keys for display
        frequencies = {adj.capitalize(): count for adj, count in adjectives.items()}

        mask_image = Image.open("images/github_green.png").resize((size_x, size_y))
        python_mask = np.array(mask_image)
        colourmap = ImageColorGenerator(python_mask)

        shared_config = dict(
            mask=python_mask,
            max_words=2000,
            width=size_x,
            height=size_y,
            min_font_size=2,
            stopwords=set(),
        )

        # Dark version
        wc = WordCloud(**shared_config, background_color="#1a1a1a")
        wc.generate_from_frequencies(frequencies)
        wc.recolor(color_func=colourmap)
        wc.to_file("static/images/cloud_dark.png")

        mask_image = Image.open("images/github_red.png").resize((size_x, size_y))
        python_mask = np.array(mask_image)
        colourmap = ImageColorGenerator(python_mask)

        shared_config = dict(
            mask=python_mask,
            max_words=2000,
            width=size_x,
            height=size_y,
            min_font_size=2,
            stopwords=set(),  
        )

        # Light version
        wc = WordCloud(**shared_config, background_color="#f5f0eb")
        wc.generate_from_frequencies(frequencies)
        wc.recolor(color_func=colourmap)
        wc.to_file("static/images/cloud_light.png")
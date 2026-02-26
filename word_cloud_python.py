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

    # Capitalize keys for display
    frequencies = {adj.capitalize(): count for adj, count in adjectives.items()}

    mask_image = Image.open("images/github.png").resize((size_x, size_y))
    python_mask = np.array(mask_image)
    colourmap = ImageColorGenerator(python_mask)

    shared_config = dict(
        mask=python_mask,
        max_words=2000,
        width=size_x,
        height=size_y,
        min_font_size=2,
        stopwords=set(),  # Disable built-in stopwords so "no" etc. appear
    )

    # Dark version
    wc = WordCloud(**shared_config, background_color="black")
    wc.generate_from_frequencies(frequencies)
    wc.recolor(color_func=colourmap)
    wc.to_file("static/images/cloud_dark.png")

    # Light version
    wc = WordCloud(**shared_config, background_color="white")
    wc.generate_from_frequencies(frequencies)
    wc.recolor(color_func=colourmap)
    wc.to_file("static/images/cloud_light.png")
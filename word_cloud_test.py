import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

separator = ' '

def make_cloud(x):
    # x is [adjective_1, counter_1, adjective_2, counter_2, ...]
    words = []
    for i in range(0, len(x), 2):  # Step by 2 to get pairs
        adjective = x[i]           # Get adjective (string)
        counter = x[i + 1]         # Get counter (int)
        words.extend([adjective] * counter)  # Repeat adjective 'counter' times
    
    text = separator.join(words)
    
    # Load and resize FIRST
    mask_image = Image.open("images/python.jpeg")
    mask_image = mask_image.resize((500, 500))

    # Convert to numpy array
    python_mask = np.array(mask_image)

    # Create color generator from the numpy array
    colourmap = ImageColorGenerator(python_mask)

    # Dark version
    wc = WordCloud(mask=python_mask,
                background_color="black",
                max_words=2000,
                min_font_size=2).generate(text)

    wc.recolor(color_func=colourmap)
    wc.to_file("static/images/output_wordcloud_dark.png")

    # Light version
    wc = WordCloud(mask=python_mask,
                background_color="white",
                max_words=2000,
                min_font_size=2).generate(text)

    wc.recolor(color_func=colourmap)
    wc.to_file("static/images/output_wordcloud_light.png")
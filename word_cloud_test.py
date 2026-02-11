from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

text = open("text.txt", 'r').read()

# Load and resize FIRST
mask_image = Image.open("images/python.jpeg")
mask_image = mask_image.resize((500, 500))  # Resize before converting to array

# Convert to numpy array
python_mask = np.array(mask_image)

# Create color generator from the numpy array
colourmap = ImageColorGenerator(python_mask)

wc = WordCloud(mask=python_mask,
               background_color="black",
               max_words=2000,
               min_font_size=2).generate(text)

# Recolor using the image colors
wc.recolor(color_func = colourmap)

# Save the wordcloud
wc.to_file("static/images/output_wordcloud_dark.png")


wc = WordCloud(mask=python_mask,
               background_color="white",
               max_words=2000,
               min_font_size=2).generate(text)

wc.recolor(color_func = colourmap)

wc.to_file("static/images/output_wordcloud_light.png")

plt.imshow(wc, interpolation='bilinear')

from wordcloud import STOPWORDS, WordCloud
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

text = open("text.txt", 'r').read()


mask_image = Image.open("images/joker.png")

python_mask = np.array(mask_image)

wc = WordCloud(stopwords=STOPWORDS, 
               mask = python_mask, 
               background_color = "white",
               max_words = 2000,
               relative_scaling = 0.5).generate(text)

# Save the wordcloud as an image

mask_image = mask_image.resize((800, 800))
wc.to_file("images/output_wordcloud.png")

from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

text = open("text.txt", 'r').read()


python_mask = np.array(PIL.Image.open("images/python_logo.png"))


wc = WordCloud(mask = python_mask, 
               background_color = "white").generate(text)

plt.imshow(wc)
plt.grid("off")
plt.axis("off")
plt.show()
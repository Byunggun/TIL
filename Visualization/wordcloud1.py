#wordcloud(워드 클라우드)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
#%matplotlib inline

text = "coffee phone phone phone phone phone phone phone phone phone cat dog dog"

# Generate a word cloud image
wordcloud = WordCloud(max_font_size=100).generate(text)

# Display the generated image:
# the matplotlib way:

fig = plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
# plt.savefig('../../assets/images/markdown_img/wordcloud_ex1.svg')
plt.savefig('MyGitHub\NLP/wordcloud_ex1.svg')
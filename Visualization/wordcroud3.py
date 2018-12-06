#워드 클라우드에서 한글 지원을 안하므로, 설정을 따로 해주셔야 합니다
#아래와 같은 형식으로 변경해보세요

#답변
from wordcloud import WordCloud

font_path = "c:/Windows/Fonts/malgun.ttf"
# font_path = 'YOUR_FONT_DIR/truetype/nanum/NanumBarunGothic.ttf'

krwordrank_cloud = WordCloud(
font_path = font_path,
width = 800,
height = 800,
background_color="white"
)

krwordrank_cloud = krwordrank_cloud.generate_from_frequencies(passwords)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 10))
plt.imshow(krwordrank_cloud, interpolation="bilinear")
plt.show()

#질문
# import matplotlib
# from tensorflow.contrib.distributions.python.ops.bijectors import inline
# from konlpy.tag import Okt
#
# from wordcloud import WordCloud
#
# import matplotlib as mpl
# #한글 깨지는 문제 해결
# mpl.rcParams['axes.unicode_minus']=False
# from matplotlib import font_manager, rc
# import matplotlib.pyplot as plt
# from math import sqrt
# font_name=font_manager.FontProperties(
#     fname='c:/Windows/Fonts/malgun.ttf').get_name()
# rc('font',family=font_name)
#
# text = "커피 빵 카스테라 강아지 루피 보리 phone phone cat dog dog"
#
# # Generate a word cloud image
# wordcloud = WordCloud(max_font_size=100).generate(text)
#
# # Display the generated image:
# # the matplotlib way:
#
# fig = plt.figure()
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.savefig('wordcloud_ex1.svg')
#
# plt.show()


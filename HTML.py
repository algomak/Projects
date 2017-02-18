#it is used to remove all html tags from the file
from bs4 import BeautifulSoup
import os
data_root="../../cleantext"
corpus_root="../../dataset/EPS"
#filename="20021108.txt"
for filename in os.listdir(corpus_root):
	file = open(os.path.join(corpus_root, filename), 'r')
	extract=open(os.path.join(data_root,filename),'w+')

#corpus={}
#cleantext=file.read()
#BeautifulSoup is used to remove html tags
	cleantext = BeautifulSoup(file).text
#now some comments still there this, function removes them too
	import re

	def cleanhtml(raw_html):
	  cleanr = re.compile(r'<[^>]+>')
	  cleantext = re.sub(cleanr, '', raw_html)
	  return cleantext
	cleantext=cleanhtml(cleantext)
	#print(cleantext)

	extract.write(cleantext)
	# print(cleantext)

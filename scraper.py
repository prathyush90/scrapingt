import requests
from bs4 import BeautifulSoup
from collections import defaultdict

pages   = []
visitedpages = []
dictionary = defaultdict(int)

pages.append('https://hiverhq.com')


def addtodictionary(items):
    for item in items:
        if(item.text):
            if(item.text.strip()):
                #replace next line and tabs
                modified_text = item.text.strip().replace("\t"," ")
                modified_text = modified_text.replace("\n", " ")
                words = modified_text.lower().split(" ")
                for word in words:
                    if(word != ''):
                        dictionary[word] += 1

while len(pages) > 0:
    url = pages.pop(0)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    #a  tag
    a_tag = soup.find_all('a')
    #h1 tag
    h1_tag = soup.find_all('h1')
    # h2 tag
    h2_tag = soup.find_all('h2')
    # h3 tag
    h3_tag = soup.find_all('h3')
    # h4 tag
    h4_tag = soup.find_all('h4')
    # h5 tag
    h5_tag = soup.find_all('h5')
    # h6 tag
    h6_tag = soup.find_all('h6')
    # span tag
    span_tag = soup.find_all('span')
    # div tag
    div_tag = soup.find_all('div')
    #p tag
    p_tag = soup.find_all('p')

    addtodictionary(a_tag)
    addtodictionary(h1_tag)
    addtodictionary(h2_tag)
    addtodictionary(h3_tag)
    addtodictionary(h4_tag)
    addtodictionary(h5_tag)
    addtodictionary(h6_tag)
    addtodictionary(span_tag)
    addtodictionary(div_tag)
    addtodictionary(p_tag)


print(dictionary['email'])
print(dictionary['your'])
print(dictionary['gmail'])
print(dictionary['to'])
print(dictionary['with'])
dictionary = sorted(dictionary,key=dictionary.__getitem__,reverse=True)
print(dictionary)

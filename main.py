from bs4 import BeautifulSoup
import requests

# Base urls
general_intro_base_url = "https://gre.magoosh.com/lessons/996-general-introduction"
math_base_url = [
    "https://gre.magoosh.com/lessons/1390-intro-to-gre-math",
    "https://gre.magoosh.com/lessons/1187-mental-math-addition-and-subtraction",
    "https://gre.magoosh.com/lessons/1227-intro-to-percents",
    "https://gre.magoosh.com/lessons/107-divisibility-rules"
    "https://gre.magoosh.com/lessons/35-intro-to-algebra",
    "https://gre.magoosh.com/lessons/70-intro-to-word-problems",
    "https://gre.magoosh.com/lessons/21-intro-to-exponents",
    "https://gre.magoosh.com/lessons/93-geometry-strategies-part-i",
    "https://gre.magoosh.com/lessons/61-the-coordinate-plane",
    "https://gre.magoosh.com/lessons/121-mean-median-mode",
    "https://gre.magoosh.com/lessons/126-introduction-to-counting",
    "https://gre.magoosh.com/lessons/137-intro-to-probability",
    "https://gre.magoosh.com/lessons/1383-unconventional-graphs",
    "https://gre.magoosh.com/lessons/907-qc-strategies-picking-numbers"
]
verbal_base_urls = [
    "https://gre.magoosh.com/lessons/149-intro-to-text-completion",
    "https://gre.magoosh.com/lessons/155-intro-to-no-shift-sentences",
    "https://gre.magoosh.com/lessons/159-intro-to-sentence-shifts",
    "https://gre.magoosh.com/lessons/164-intro-to-double-blank-sentences",
    "https://gre.magoosh.com/lessons/169-intro-to-triple-blank-sentences",
    "https://gre.magoosh.com/lessons/180-intro-to-sentence-equivalence",
    "https://gre.magoosh.com/lessons/1014-flashcards",
    "https://gre.magoosh.com/lessons/1475-intro-to-reading-comprehension",
    "https://gre.magoosh.com/lessons/994-elements-of-the-argument",
]


# Grabbing the links
def get_links_jpg(url):
    links = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    lesson_titles = soup.findAll('div', class_='lesson-item-thumb')
    for i in lesson_titles:
        link = (i.find('img')['src'])
        links.append(link)
    return links


# going through base urls to grab links
def export_links(urls):
    links = []
    print("Getting in the data >> ")
    count = 1
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        lesson_titles = soup.findAll('div', class_='lesson-item-thumb')
        for i in lesson_titles:
            link = (i.find('img')['src'])
            links.append(link)
        print(f"Completed {count} ....")
        count = count + 1
    print("\nLinks grabbed successfully !!")
    return links


# converting into webm from jpeg
def convert_to_webm(jpg_list):
    links = []
    for i in jpg_list:
        original = i.split("/")
        original[-1] = 'web_webm.webm'
        modified = "/".join(original)
        links.append(modified)
    return links


# printing links
def show_links(a):
    for i in a:
        print(i)


# Start
general_intro_jpg = get_links_jpg(general_intro_base_url)
general_intro_webm = convert_to_webm(general_intro_jpg)
show_links(general_intro_webm)

math_links_jpg = export_links(math_base_url)
math_links_webm = convert_to_webm(math_links_jpg)
show_links(math_links_webm)

verbal_links_jpg = export_links(verbal_base_urls)
verbal_links_webm = convert_to_webm(verbal_links_jpg)
show_links(verbal_links_webm)

from bs4 import BeautifulSoup
import requests

# Base urls
general_intro_base_url = {"General Intro": "https://gre.magoosh.com/lessons/996-general-introduction"}
math_base_url = {
    "General Math Strategies": "https://gre.magoosh.com/lessons/1390-intro-to-gre-math",
    "Arithmetic and Fractions": "https://gre.magoosh.com/lessons/1187-mental-math-addition-and-subtraction",
    "Percents and Ratios": "https://gre.magoosh.com/lessons/1227-intro-to-percents",
    "Integer Properties": "https://gre.magoosh.com/lessons/107-divisibility-rules",
    "Algebra, Equations, and Inequalities": "https://gre.magoosh.com/lessons/35-intro-to-algebra",
    "Word Problems": "https://gre.magoosh.com/lessons/70-intro-to-word-problems",
    "Powers and Roots": "https://gre.magoosh.com/lessons/21-intro-to-exponents",
    "Geometry": "https://gre.magoosh.com/lessons/93-geometry-strategies-part-i",
    "Coordinate Geometry": "https://gre.magoosh.com/lessons/61-the-coordinate-plane",
    "Statistics": "https://gre.magoosh.com/lessons/121-mean-median-mode",
    "Counting": "https://gre.magoosh.com/lessons/126-introduction-to-counting",
    "Probability": "https://gre.magoosh.com/lessons/137-intro-to-probability",
    "Data Interpretation": "https://gre.magoosh.com/lessons/1383-unconventional-graphs",
    "Advanced QC Strategies": "https://gre.magoosh.com/lessons/907-qc-strategies-picking-numbers"
}
verbal_base_urls = {
    "Text Completion - Overview": "https://gre.magoosh.com/lessons/149-intro-to-text-completion",
    "Text Completion - No Shifts": "https://gre.magoosh.com/lessons/155-intro-to-no-shift-sentences",
    "Text Completion - Sentence Shifts": "https://gre.magoosh.com/lessons/159-intro-to-sentence-shifts",
    "Text Completion - Double Blanks": "https://gre.magoosh.com/lessons/164-intro-to-double-blank-sentences",
    "Text Completion - Triple Blanks": "https://gre.magoosh.com/lessons/169-intro-to-triple-blank-sentences",
    "Sentence Equivalence": "https://gre.magoosh.com/lessons/180-intro-to-sentence-equivalence",
    "Vocabulary": "https://gre.magoosh.com/lessons/1014-flashcards",
    "Reading Comprehension": "https://gre.magoosh.com/lessons/1475-intro-to-reading-comprehension",
    "Paragraph Argument": "https://gre.magoosh.com/lessons/994-elements-of-the-argument",
}


# Exports the link of each section with title
def export_links(urls_dict):
    main_data = {}
    print("Getting in the data >> ")
    for key, url in urls_dict.items():
        print(f"Section ------ {key} ------")
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        lesson_titles = soup.findAll('div', class_='lesson-item-thumb')
        section_links = return_dict(lesson_titles)
        main_data[key] = section_links
    return main_data


# Returns Dictionary of title and url
def return_dict(in_list):
    links = {}
    for i in in_list:
        title = i.parent.find('h3').text
        link_jpeg = (i.find('img')['src'])
        link_webm = convert_to_webm(link_jpeg)
        links[title] = link_webm
    return links


# converts the link in jpeg to webm
def convert_to_webm(link):
    original = link.split("/")
    original[-1] = 'web_webm.webm'
    modified = "/".join(original)
    return modified


main_data1 = export_links(verbal_base_urls)
for section, sub_section in main_data1.items():
    print(section)
    for sub_key, sub_value in sub_section.items():
        print(f"\t\t{sub_key} ---> {sub_value}")




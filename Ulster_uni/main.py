import requests
from bs4 import BeautifulSoup
import pandas as pd

"""
                                       DATA DEFINITIONS
"""

# Data for checking and execution
all_course_urls = []
location_list = []

# Required columns
course_name_list = []
course_category_list = []
course_sub_category_list = []
course_website_list = []
duration_list = []
duration_term_list = []
study_mode_list = []
degree_level_list = []
monthly_intake_list = []
intake_day_list = []
intake_month_list = []
apply_day_list = []
apply_month_list = []
city_list = []
domestic_only_list = []
international_fee_list = []
domestic_fee_list = []
fee_term_list = []
fee_year_list = []
currency_list = []
study_load_list = []
ielts_listening_list = []
ielts_speaking_list = []
ielts_writing_list = []
ielts_reading_list = []
ielts_overall_list = []
pte_listening_list = []
pte_speaking_list = []
pte_writing_list = []
pte_reading_list = []
pte_overall_list = []
tofel_listening_list = []
tofel_speaking_list = []
tofel_writing_list = []
tofel_reading_list = []
tofel_overall_list = []
english_test_list = []
english_test_reading_list = []
english_test_listening_list = []
english_test_speaking_list = []
english_test_writing_list = []
english_test_overall_list = []
acaedmic_level_list = []
academic_score_list = []
score_type_list = []
academic_country_list = []
other_test_list = []
score_list = []
other_requirements_list = []
course_description_list = []
course_structure_list = []
carrer_list = []
Scholarship_list = []
language_list = []

"""                
                        FUNTION DEFINITIONS
"""

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}


# For getting url of all pages
def get_all_page_urls():
    all_page_urls = []
    page = 481
    for i in range(10):  ## 2 rakheko check garna last mah 19 garne ho
        url = "https://www.ulster.ac.uk/courses?profile=_default-facets&&start_rank=" + str(page)
        all_page_urls.append(url)
        page += 40
    return all_page_urls


# adds each course url of  a page to all_course_urls
def get_all_course_urls(page_url):
    r = requests.get(page_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    divs = soup.find_all('div', class_='course')
    for div in divs:
        course_link = div.find('a')['href']
        all_course_urls.append(course_link)


# Each course location list
def get_all_location_with_urls():
    for page in get_all_page_urls():
        get_all_course_urls(page)
        r = requests.get(page)
        soup = BeautifulSoup(r.content, 'html.parser')
        course_divs = soup.find_all('div', class_="course")
        for all_a in course_divs:
            address = all_a.find('div', class_="meta").find_all('p')[2].text.strip()
            location_list.append(address)


# Returns list to check whether data is available or not (for few data only)
def get_checker_list(soup):
    checker_list = []
    inner_div = soup.find('div', class_='bg-navy-trans').find_all('p', class_='bl')
    for i in inner_div:
        text = i.get_text()
        text = text.strip()
        checker_list.append(text)
    return checker_list


# Returns course basic info div
def get_course_basic_div(soup):
    main_div = soup.find('div', class_='bg-navy-trans')
    return main_div


# Give  course more info div
def get_course_advance_links(soup):
    main_div_items = []
    div = soup.find('ul', class_='tabs')
    if div:
        for a in div.find_all('a', class_='bl'):
            main_div_items.append(a['href'])
    return main_div_items  # requires change


# Returns the city of study
def get_city(index):
    return location_list[index]


# Returns study load
def get_study_load(soup, outer_div):
    full_text_list = outer_div.find('p').get_text().strip().split("\r")
    study_load = (full_text_list[1]).replace("\n                              ", " ")
    study_load = study_load.strip()
    return study_load


# Returns course name
def get_course_name(soup, outer_div):
    course_name = outer_div.find('h1').get_text()
    course_name = course_name.strip()
    if course_name.find("\r") != -1:
        course_name = course_name.strip().split("\r")
        name = course_name[0] + " -" + course_name[1].replace("\n                                                 ",
                                                              " ")
        return name
    else:
        return course_name


# Returns course website
def get_course_website(url):
    return url


# Returns course category
def get_course_category(soup, outer_div):
    if 'School:' in get_checker_list(soup):
        inner_div = outer_div.find_all('div', class_='m-b-10')
        course_category = inner_div[1].find_all('p', class_='m-b-0')[1].get_text()
        return course_category
    else:
        return " "


# Returns course degree level
def get_degree_level(soup, outer_div):
    main_div = outer_div.find('p').get_text().strip().split("\r")
    degree_level = main_div[2].replace('\n                                              ', " ")
    degree_level = degree_level.strip()
    return degree_level


# Returns course intake month
def get_intake_month(soup, outer_div):
    inner_div = outer_div.find_all('p', class_='m-b-0')[-1]
    date_list = inner_div.get_text().split(" ")
    if len(date_list) == 3:
        return date_list[1]
    else:
        return date_list[0]


# Returns Monthly intake
def get_monthly_intake():
    return " "


# Returns course intake day
def get_course_intake_day(soup, outer_div):
    inner_div = outer_div.find_all('p', class_='m-b-0')[-1]
    date_list = inner_div.get_text().split(" ")
    if len(date_list) == 3:
        return date_list[0]
    else:
        return " "


# Returns course sub category (no categery so returning empty string)
def get_course_sub_category():
    return " "


# Returns course study mode
def get_Study_mode(city):
    if city == 'eLearning':
        return 'Online'
    else:
        return 'On campus'


# Returns the years to be studied
def get_duration(url, advanced_links_div):
    if '#modules' in advanced_links_div:
        r = requests.get(url + '#modules')
        soup = BeautifulSoup(r.content, 'html.parser')
        modules_list = soup.find('div', id='modules').find('ol', class_='sectionlinks').find_all('li')
        return (len(modules_list))
    else:
        return (" ")


# Returns duration term
def get_duration_term(duration):
    if duration == " ":
        return " "
    elif duration == 1:
        return 'year'
    else:
        return 'years'


# Returns IELTS info dictonary
def get_iltes_info(url, advanced_links_div):
    if '#entryconditions' in advanced_links_div:
        r = requests.get(url + '#entryconditions')
        soup = BeautifulSoup(r.content, 'html.parser')
        parent_english = soup.find('div', id='entryconditions')
        all_paras = parent_english.find_all("p")
        for para in all_paras:
            spllitted_para = para.text.split(' ')
            if ('IELTS' in spllitted_para and 'Academic' in spllitted_para):
                ielts1 = spllitted_para[(spllitted_para.index('IELTS') + 1)]
                try:
                    ielts1 = float(ielts1)
                    return ({
                        'listening': ielts1 - 0.5,
                        'speaking': ielts1 - 0.5,
                        'writing': ielts1 - 0.5,
                        'reading': ielts1 - 0.5,
                        'overall': ielts1
                    })
                except ValueError:
                    return ({
                        'listening': ' ',
                        'speaking': ' ',
                        'writing': ' ',
                        'reading': ' ',
                        'overall': ' '
                    })
    else:
        return ({
            'listening': ' ',
            'speaking': ' ',
            'writing': ' ',
            'reading': ' ',
            'overall': ' '
        })

    return ({
        'listening': ' ',
        'speaking': ' ',
        'writing': ' ',
        'reading': ' ',
        'overall': ' '
    })


# course description or overview
def get_course_description(soup):
    summary_text_para1 = soup.find('h3', id='secsummary')
    if summary_text_para1:
        return summary_text_para1.find_next().text
    else:
        return " "


# get carrer
def get_carrer_info(url, advanced_links_div):
    r = requests.get(url + '#opportunities')
    soup = BeautifulSoup(r.content, 'html.parser')
    if '#opportunities' in advanced_links_div:
        carrer_para_1 = soup.find('h3', id='seccareeroptions')
        if carrer_para_1:
            carrer = carrer_para_1.find_next('p').text
            return carrer

    return " "


# modules info
def get_course_structure(url, advanced_links):
    if '#modules' in advanced_links:
        r = requests.get(url + '#modules')
        soup = BeautifulSoup(r.content, 'html.parser')
        modules_tags = soup.find('div', id="modules").find_all("h4")
        modules = " "
        for i in modules_tags:
            modules = i.text + " , " + modules
        return modules
    else:
        return ' '


def get_domestic_only():
    return "False"


# International Fee
def get_fee_int(url, advanced_course_links):
    if '#fees' in advanced_course_links:
        r = requests.get(url + '#fees')
        soup = BeautifulSoup(r.content, 'html.parser')
        fee_block = soup.find('div', id='fees')
        all_p = fee_block.find_all('p')
        for p in all_p:
            text_list = p.text.split(" ")
            if 'International:' in text_list:
                return (text_list[text_list.index('International:') + 1].replace("£", " ").replace(".00", " "))
    else:
        return " "

    return " "


# Domestic Fee
def get_fee_domestic(url, advanced_course_links):
    if '#fees' in advanced_course_links:
        r = requests.get(url + '#fees')
        soup = BeautifulSoup(r.content, 'html.parser')
        fee_block = soup.find('div', id='fees')
        all_p = fee_block.find_all('p')
        for p in all_p:
            text_list = p.text.split(" ")
            if 'EU:' in text_list:
                return (text_list[text_list.index('EU:') + 1].replace("£", " ").replace(".00", " "))
    else:
        return " "

    return " "


def get_currency():
    return "GBP"


# Adds data to individual list
def set_data(data):
    course_name_list.append(data['course_name'])
    course_category_list.append(data['course_category'])
    course_sub_category_list.append(data['course_sub_category'])
    course_website_list.append(data['course_website'])
    city_list.append(data['city'])
    study_mode_list.append(data['study_mode'])
    degree_level_list.append(data['degree_level'])
    intake_month_list.append(data['intake_month'])
    intake_day_list.append(data['intake_day'])
    monthly_intake_list.append(data['monthly_intake'])
    study_load_list.append(data['study_load'])
    duration_list.append(data['duration'])
    duration_term_list.append(data['duration_term'])
    ielts_listening_list.append(data['ielts']['listening'])
    ielts_speaking_list.append(data['ielts']['speaking'])
    ielts_writing_list.append(data['ielts']['writing'])
    ielts_reading_list.append(data['ielts']['reading'])
    ielts_overall_list.append(data['ielts']['overall'])
    apply_day_list.append(" ")
    apply_month_list.append(" ")
    pte_listening_list.append(" ")
    pte_speaking_list.append(" ")
    pte_writing_list.append(" ")
    pte_reading_list.append(" ")
    pte_overall_list.append(" ")
    tofel_listening_list.append(" ")
    tofel_speaking_list.append(" ")
    tofel_writing_list.append(" ")
    tofel_reading_list.append(" ")
    tofel_overall_list.append(" ")
    english_test_list.append(" ")
    english_test_reading_list.append(" ")
    english_test_listening_list.append(" ")
    english_test_speaking_list.append(" ")
    english_test_writing_list.append(" ")
    english_test_overall_list.append(" ")
    acaedmic_level_list.append(" ")
    academic_score_list.append(" ")
    score_type_list.append(" ")
    academic_country_list.append(" ")
    other_test_list.append(" ")
    score_list.append(" ")
    other_requirements_list.append(" ")
    course_description_list.append(data['course_description']),
    carrer_list.append(data['carrer'])
    course_structure_list.append(data['modules'])
    domestic_only_list.append(data['domestic_only'])
    currency_list.append("GBP")
    Scholarship_list.append(" ")
    fee_year_list.append("2021")
    international_fee_list.append(data['Internationa Fee'])
    domestic_fee_list.append(data['domestic fee'])
    fee_term_list.append('year')
    language_list.append(' ')


# Make a pandas data_frame and exports a exel file
def export_exel():
    all_data_dict = {
        'Course Name': course_name_list,
        'Catagory': course_name_list,
        'Sub Category': course_sub_category_list,
        'Course Website': course_website_list,
        'Duration': duration_list,
        'Duration Term': duration_term_list,
        'Study Mode': study_mode_list,
        'Degree Level': degree_level_list,
        'Intake Day': intake_day_list,
        'Intake Month': intake_month_list,
        'Apply Day': apply_day_list,
        'Apply Month': apply_month_list,
        'City': city_list,
        'Domestic only': domestic_only_list,
        'International Fee': international_fee_list,
        'Domestic Fee': domestic_fee_list,
        'Fee Term': fee_term_list,
        'Fee Year': fee_year_list,
        'Currency': currency_list,
        'Study Load': study_load_list,
        'Language': language_list,
        'IELTS Listening': ielts_listening_list,
        'IELTS speaking': ielts_speaking_list,
        'IELTS writing': ielts_writing_list,
        'IELTS Reading': ielts_reading_list,
        'IELTS Overall': ielts_overall_list,
        'PTE Listening': pte_listening_list,
        'PTE Speaking': pte_speaking_list,
        'PTE Writing': pte_writing_list,
        'PTE Reading': pte_reading_list,
        'PTE Overall': pte_overall_list,
        'TOFEL Listening': tofel_listening_list,
        'TOFEL Speaking': tofel_speaking_list,
        'TOFEL Writing': tofel_writing_list,
        'TOFEL Reading': tofel_reading_list,
        'TOFEL Overall': tofel_overall_list,
        'English Test': english_test_list,
        'English Test Reading': english_test_reading_list,
        'English Test Listening': english_test_listening_list,
        'English Test Speaking': english_test_speaking_list,
        'English Test Writing': english_test_writing_list,
        'English Test Overall': english_test_overall_list,
        'Academic Level': acaedmic_level_list,
        'Academic Score': academic_score_list,
        'Score Type': score_type_list,
        'Academic Country': academic_score_list,
        'Other Test': other_test_list,
        'Score': score_list,
        'Other Requirement': other_requirements_list,
        'Course Description': course_description_list,
        'Course Structure': course_structure_list,
        'Career': carrer_list,
        'Scholarship': Scholarship_list,
    }

    dataframe = pd.DataFrame(all_data_dict)
    with pd.ExcelWriter('unidata2.xlsx') as writer:
        dataframe.to_excel(writer, sheet_name='Sheet_name_1')
        writer.save()


# MAIN EXECUTION FUNCTION
def test():
    print("***********START TEST *************")
    get_all_location_with_urls()
    print("*********** Course url completed ************ ")
    print(len(all_course_urls))
    x = 0
    for url in all_course_urls:
        print("\ncourse no : {0}\n-------------------------------------------\n".format(x))
        r = requests.get(url, max_redirects=1000)
        soup = BeautifulSoup(r.content, 'html.parser')
        outer_div = get_course_basic_div(soup)
        advanced_links_div = get_course_advance_links(soup)
        if outer_div:
            city = get_city(x)
            duration = get_duration(url, advanced_links_div)
            single_data = {
                'course_name': get_course_name(soup, outer_div),
                'course_category': get_course_category(soup, outer_div),
                'course_sub_category': get_course_sub_category(),
                'course_website': get_course_website(url),
                'city': city,
                'study_mode': get_Study_mode(city),
                'degree_level': get_degree_level(soup, outer_div),
                'intake_month': get_intake_month(soup, outer_div),
                'intake_day': get_course_intake_day(soup, outer_div),
                'monthly_intake': get_monthly_intake(),
                'study_load': get_study_load(url, outer_div),
                'duration': duration,
                'duration_term': get_duration_term(duration),
                'ielts': get_iltes_info(url, advanced_links_div),
                'course_description': get_course_description(soup),
                'carrer': get_carrer_info(url, advanced_links_div),
                'modules': get_course_structure(url, advanced_links_div),
                'domestic_only': get_domestic_only(),
                'Internationa Fee': get_fee_int(url, advanced_links_div),
                'domestic fee': get_fee_domestic(url, advanced_links_div),
            }
            set_data(single_data)
            export_exel()
            # seeing to print
            print("course name : ", course_name_list[x])
            # print("course category: ",course_category_list[x])
            # print("course sub category : ",course_sub_category_list[x])
            # print("city : ",city_list[x])
            # print("course website : ",course_website_list[x])
            # print("degree level : ",degree_level_list[x])
            # print("Intake month : " ,intake_month_list[x])
            # print("Intake day : ",intake_day_list[x])
            # print("Monthly Intake : ", monthly_intake_list[x])
            # print("study load : ",study_load_list[x])
            # print("study mode : ",study_mode_list[x])
            # print("Years to be studied : ", duration_list[x])
            # print("Duration Term : ", duration_term_list[x])
            # print("Itelts listening : ", ielts_listening_list[x])
            # print("Itelts speaking : ", ielts_speaking_list[x])
            # print("Itelts writing : ", ielts_writing_list[x])
            # print("Itelts reading : ", ielts_reading_list[x])
            # print("Itelts overall : ", ielts_overall_list[x])
            # print("course description : ", course_description_list[x]) 
            # print("carrer : ", carrer_list[x]) 
            # print("modulees : ", course_structure_list[x])
            # print("Domestic only : ", domestic_only_list[x] )
            # print("Currency : ", currency_list[x])
            # print("International Fee : ", international_fee_list[x])
            # print("Domestic Fee : ", domestic_fee_list[x])
        else:
            continue
        x += 1
    print("********TEST SUCCESSFUL******")


"""
                                        Execution Starts here
"""

test()

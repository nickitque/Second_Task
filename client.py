from clients.http_client import HTTPClient
from models.parser import TutByParser

"""
Current script to find and scan all vacancies from rabota.by.
Script uses word "python" to find vacancies.
Also script counts occurrence of the words 'python', 'linux', 'flask' per  each vacancy.
Also it can calculate average match of this words from all vacancies.
"""

"""marking the word by which we will search for vacancies"""
word_to_search = "python"

"""designating http client to use methods from it"""
http_client = HTTPClient()

"""designated a parser"""
parser = TutByParser()

url = parser.get_all_pages(url)

"""designated get method from http client and headers from TutByParser"""
response = http_client.get(url, parser.headers)

page_parsing = parser.parsing_the_page(response)

search_page_numbers = parser.final_page(word_to_search)

search_page_urls = parser.get_all_pages(word_to_search)

vacancies_urls = parser.get_vacancies_urls(search_page_urls=search_page_urls, word_to_search=word_to_search)

if __name__ := '__main__':
    print(f"Total number of pages: {len(search_page_urls)}")
    print(f"Total number of vacancies: {len(vacancies_urls)}")

    result = parser.get_wordsCount("Python", "Linux", "Flask")
    average_num = parser.average_number_of_occurence(average_num, "Python", "Linux", "Flask")
    print(average_num, result)

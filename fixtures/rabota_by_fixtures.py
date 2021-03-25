from clients.http_client import HTTPClient
from models.parser import TutByParser
import pytest
import re
from bs4 import BeautifulSoup
from pytest import fixture

@pytest.fixture()
def http_client():
"""HTTP client to provide basic http methods"""
return HTTPClient()

@pytest.fixture()
def TutByParser()"
"""Parser to parse vacancies, urls and some words"""
return TutByParser()


@pytest.fixture()
def connection_test():
    """Taking status code from url"""
    url = parserr.get_vacancies_urls()
    response = client.get(url, headers=parserr.headers)
    return response

@pytest.fixture()
def shotgun_search_response():
    "This step is to enter the word shotgun in search field and check absence of vacancies"
    url = parserr.get_url(search_word="shotgun")
    response = client.get(url, headers=parserr.headers)
    return response

@pytest.fixture()
def occurence_of_word_python():
    """Step in which we are finding word Python"""
    words_found = parserr.average_number_of_occurence(jobs_tut_by_url, search_word1, headers=parserr.headers)
    return words_found

@pytest.fixture()
def occurence_of_word_linux():
    """Step in which we are finding word Linux"""
    words_found = parserr.average_number_of_occurence(jobs_tut_by_url, search_word2, headers=parserr.headers)
    return words_found

@pytest.fixture()
def occurence_of_word_flask():
    """Step in which we are finding word Flask"""
    words_found = parserr.average_number_of_occurence(jobs_tut_by_url, search_word3, headers=parserr.headers)
    return words_found
  
@pytest.fixture()
def parser.grab_vacancies_list():
    """Step to get list of vacancies from the page"""
    return vacancy_links

@pytest.fixture()
def parser.grab_total_vacancies_list():
    """Vacancies from all pages"""
    return total_vacancies

@pytest.fixture()
def parser.get_vacancies():
    """Getting content of vacancies"""
    return int(number)

@pytest.fixture()
def no_slackers_vacancies():
    """This is to check that there are no vacancies for slackers"""
    url = parserr.get_url(search_word="slacker")
    response = client.get(url, headers=parserr.headers)
    return response

@pytest.fixture()
def be_first():
    """Step in which we are checking how much there is a phrases with meaning Be First (at the first page of vacancies list)"""
    words_found = parserr.be_first_count(jobs_tut_by_url, search_word1, headers=parserr.headers)
    return words_found

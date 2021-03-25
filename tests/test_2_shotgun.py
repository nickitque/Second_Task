
def shotgun(find_shotgun_phrase):

    phrase = "По запросу «shotgun» ничего не найдено"
    assert find_shotgun_phrase.status_code == 200, "The status code is f'{find_shotgun_phrase.status_code}'"
    assert phrase in find_shotgun_phrase.text, "There are no matches for phrase"

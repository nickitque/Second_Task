def slackers_check(no_slackers_vacancies):

    phrase = "По запросу «slacker» ничего не найдено"
    assert find_shotgun_phrase.status_code == 200, "Connection is ok"
    assert phrase in no_slackers_vacancies.text, "No jobs for slackers"

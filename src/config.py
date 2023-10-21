import os

# адрес для запроса на вакансии
HH_API_URL = 'https://api.hh.ru/vacancies'
# адрес для запроса по областям
HH_API_URL_AREAS = 'https://api.hh.ru/areas'
HH_AREAS_JSON = 'data/areas/headhunter_areas.json'
SJ_API_TOKEN: str = os.getenv('API_KEY_SUPER_JOB')
SJ_API_URL_AREAS = 'https://api.superjob.ru/2.0/towns/'
SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies/'
SJ_AREAS_JSON = 'data/areas/superjob_areas.json'

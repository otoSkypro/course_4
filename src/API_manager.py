from abc import ABC, abstractmethod
import requests

from src.config import HH_API_URL, SJ_API_URL, SJ_API_TOKEN
from src.vacancies import Vacancy


class APImanager(ABC):


    @abstractmethod
    def get_vacancies(self):

        pass

    @abstractmethod
    def format_data(self):

        pass

class HeadHunterApi(APImanager):


    def __init__(self, keyword):

        self.keyword = keyword

    def get_vacancies(self):

        response = requests.get(HH_API_URL, headers={"User-Agent": "HH-User-Agent"}, params={'text': self.keyword})
        return response.json()

    def format_data(self):
        formated_vacancies = []
        row_hh_data = self.get_vacancies()
        for vacancy in row_hh_data['items']:
            try:
                filtered_vacancies = {'title': vacancy.get('name'),
                                      'salary_from': vacancy['salary']['from'],
                                      'description': vacancy['snippet']['requirement'],
                                      'url': vacancy['alternate_url']}
            except (KeyError, TypeError, IndexError, ValueError):
                filtered_vacancies = {'title': vacancy.get('name'),
                                      'salary_from': 0,
                                      'description': vacancy['snippet'].get('requirement'),
                                      'url': vacancy.get('alternate_url')}


            vac = Vacancy(**filtered_vacancies)
            vac.validate_data()
            formated_vacancies.append(vac)

        return formated_vacancies


class SuperJobApi(APImanager):


    def __init__(self, keyword):

        self.keyword = keyword

    def get_vacancies(self):

        headers = {'X-Api-App-Id': SJ_API_TOKEN}
        response = requests.get(SJ_API_URL, headers=headers, params={'keyword': self.keyword})
        print(response.status_code)
        return response.json()

    def format_data(self):


        sj_formatted_vacancies = []
        row_sj_data = self.get_vacancies()
        for vacancy in row_sj_data['objects']:
            try:
                filtered_vacancies = {'title': vacancy['profession'],
                                      'salary_from': vacancy['payment_from'],
                                      'description': vacancy['candidat'],
                                      'url': vacancy['link']}
            except (KeyError, TypeError, IndexError, ValueError):
                filtered_vacancies = {'title': vacancy.get('profession'),
                                      'salary_from': 0,
                                      'description': vacancy['candidat'],
                                      'url': vacancy['link']}


            vac = Vacancy(**filtered_vacancies)
            vac.validate_data()
            sj_formatted_vacancies.append(vac)

        return sj_formatted_vacancies
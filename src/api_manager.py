from abc import ABC, abstractmethod
import requests

from src.config import HH_API_URL, SJ_API_URL, SJ_API_TOKEN
from src.vacancies import Vacancy


class APImanager(ABC):
    """Класс для работы с API сторонних сервисов"""

    @staticmethod
    def validate_data(self):
        """Функция для валидации данных"""
        if self.title is None:
            self.title = ' '
        elif self.url is None:
            self.url = ' '
        elif self.salary_from is None or self.salary_from == 'null':
            self.salary_from = 0
        elif self.description is None:
            self.description = ' '
        return self

    @abstractmethod
    def get_vacancies(self):
        """Получает ваканасии со стороннего ресурса"""
        pass

    @abstractmethod
    def format_data(self):
        """Форматирует данные, полученные по API в единый формат"""


class HeadHunterApi(APImanager):
    """Класс для работы с площадкой hh.ru"""

    def __init__(self, keyword):
        """
        Инициализатор класса.
        :param keyword: ключевое слово для создания запроса
        """
        self.keyword = keyword

    def get_vacancies(self):
        """
        Получает ваканасии со стороннего ресурса hh.ru
        :return: список вакансий в json файле
        """
        response = requests.get(HH_API_URL, headers={"User-Agent": "HH-User-Agent"}, params={'text': self.keyword})
        return response.json()

    def format_data(self):
        """
        Форматирует данные, полученные по API в единый формат
        :return: Список вакансий в едином формате
        """
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

            # создание экземпляра класса с созданием полей из словаря (распаковка словаря)
            vac = Vacancy(**filtered_vacancies)
            vac = self.validate_data(vac)
            formated_vacancies.append(vac)
        # список из объектов класса Vacancy
        return formated_vacancies


class SuperJobApi(APImanager):
    """Класс для работы с площадкой SuperJob.ru"""

    def __init__(self, keyword):
        """Инициализатор класса.
        :param keyword: ключевое слово для создания запроса
        """
        self.keyword = keyword

    def get_vacancies(self):
        """
        Получает ваканасии со стороннего ресурса SuperJob.ru
        :return: список вакансий в json файле
        """
        headers = {'X-Api-App-Id': SJ_API_TOKEN}
        response = requests.get(SJ_API_URL, headers=headers, params={'keyword': self.keyword})
        print(response.status_code)
        return response.json()

    def format_data(self):
        """
        Форматирует данные, полученные по API в единый формат
        :return: Список вакансий в едином формате
        """
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

            # создание экземпляра класса с созданием полей из словаря (распаковка словаря)
            vac = Vacancy(**filtered_vacancies)
            vac = self.validate_data(vac)
            sj_formatted_vacancies.append(vac)
        # список из объектов класса Vacancy
        return sj_formatted_vacancies

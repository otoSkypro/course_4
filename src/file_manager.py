import json
from abc import ABC, abstractmethod


class FileManager(ABC):
    """Класс для работы с файлами"""

    @abstractmethod
    def get_vacancies_by_keyword(self, keyword):
        """Функция чтения из файла"""
        pass

    @abstractmethod
    def write_file(self, vacancies):
        """Функция записи в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancies):
        """Функция удаления из файла"""
        pass

    @abstractmethod
    def get_list_vacancies(self):
        """Функция получения списка вакансии"""
        pass


class JsonFileManager(FileManager):
    """Класс для работы с файлами формата json"""

    def __init__(self, filename):
        self.filename = filename

    def write_file(self, vacancies):
        """
        Функция записи в файл.
        :param vacancies: список объектов класса Vacancy
        :return: None
        """
        data = self.data_to_json(vacancies)
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))

    @staticmethod
    def data_to_json(vacancies):
        """
        Распаковывает список объектов класса Vacancy и записывает в новый список
        :param vacancies: список объектов класса Vacancy
        :return: vacancies_lict: список словарей с вакансиями в нужном формате
        """
        vacancies_list = []
        for vacancy in vacancies:
            vacancy_dict = {'title': vacancy.title,
                            'url': vacancy.url,
                            'salary_from': vacancy.salary_from,
                            'description': vacancy.description
                            }
            vacancies_list.append(vacancy_dict)
        return vacancies_list

    def get_list_vacancies(self):
        """Функция получения списка вакансии"""
        with open(self.filename, 'r', encoding='utf-8') as f:
            data_for_filter = f.read()
        data = json.loads(data_for_filter)
        return data

    def get_vacancies_by_keyword(self, keyword: dict):
        """
         Метод получения вакансий  из файла по ключевому слову.
        :param keyword: словарь с ключевыми словами для поиска
        :return list_of_vac: список вакансий, выбранных по ключевым словам
        """
        with open(self.filename, 'r', encoding='utf-8') as f:
            data_for_filter = f.read()
        data = json.loads(data_for_filter)
        list_of_vac = []
        for vacancy in data:
            flag = True
            for key, val in keyword.items():
                if key == 'salary_input':
                    if vacancy['salary_from'] < val['salary_from']:
                        flag = False
                        break
            if flag:
                list_of_vac.append(vacancy)
        return list_of_vac

    def delete_vacancy(self, vacancies):
        """
           Функция удаления из файла.
           :param vacancies: список объектов класса Vacancy
           :return: None
           """
        with open(self.filename, 'r', encoding='utf-8') as f:
            file_data = f.read()
            data = json.loads(file_data)
        # vacancies_to_delete = self.data_to_json(vacancies)
        for vacancy in data:
            if vacancy in vacancies:
                data.remove(vacancy)
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))
import json
from abc import ABC, abstractmethod


class FileManager(ABC):


    @abstractmethod
    def get_vacancies_by_keyword(self, keyword):
        pass

    @abstractmethod
    def write_file(self, vacancies):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancies):
        pass

    @abstractmethod
    def get_list_vacancies(self):
        pass


class JsonFileManager(FileManager):


    def __init__(self, filename):
        self.filename = filename

    def write_file(self, vacancies):

        data = self.data_to_json(vacancies)
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))

    @staticmethod
    def data_to_json(vacancies):

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

        with open(self.filename, 'r', encoding='utf-8') as f:
            data_for_filter = f.read()
        data = json.loads(data_for_filter)
        return data

    def get_vacancies_by_keyword(self, keyword: dict):

        with open(self.filename, 'r', encoding='utf-8') as f:
            data_for_filter = f.read()
        data = json.loads(data_for_filter)
        list_of_vac = []
        for vacancy in data:
            flag = True
            for k, v in keyword.items():
                if k == 'salary_input':
                    if vacancy['salary_from'] < v:
                        flag = False
                        break
            if flag:
                list_of_vac.append(vacancy)
        return list_of_vac

    def delete_vacancy(self, vacancies):

        with open(self.filename, 'r', encoding='utf-8') as f:
            file_data = f.read()
            data = json.loads(file_data)

        for vacancy in data:
            if vacancy in vacancies:
                data.remove(vacancy)
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))


class CSVsaver(FileManager):
    pass


class XLSsaver(FileManager):
    pass
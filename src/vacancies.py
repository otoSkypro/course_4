class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, title: str, salary_from: int, description: str, url: str):
        """
        Инициализатор класса Vacancy.
        :param title: название вакансии
        :param salary_from: минимальная зарплата
        :param description: описание вакансии
        :param url: ссылка на вакансию
        """
        self.title = title
        self.salary_from = salary_from
        self.description = description
        self.url = url

    def __repr__(self):
        return (f"Вакансия {self.title}: заплата от {self.salary_from}, "
                f"описание {self.description} ссылка на вакансию: {self.url}")

    def __ge__(self, other):
        return self.salary_from >= other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from


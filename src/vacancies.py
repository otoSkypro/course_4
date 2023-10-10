class Vacancy:

    def __init__(self, title: str, salary_from: int, description: str, url: str):

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

    def validate_data(self):

        if self.title is None:
            self.title = ' '
        elif self.url is None:
            self.url = ' '
        elif self.salary_from is None or self.salary_from == 'null':
            self.salary_from = 0
        elif self.description is None:
            self.description = ' '
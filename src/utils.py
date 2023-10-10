from src.API_manager import HeadHunterApi, SuperJobApi
from src.file_manager import JsonFileManager


def choose_platform():
    """
    Функция для общения с пользователем и выбора площадки.
    """
    print('Выберите платформу для поиска вакансии\n'
          '1 - HeadHunter\n'
          '2 - SuperJob\n'
          '3 - на всех платформах')


def choose_vacancy():
    """
    Функция для общения с пользователем и ввода названия вакансии для формирования запроса.
    """
    print(' Ведите вакансию для поиска ')
    user_input = input()
    return user_input


def get_vacancies(api_manager: list):
    """Функция для вывода списка вакансий по запросу с API"""
    vacancies = []
    for api in api_manager:
        vacancies.extend(api.format_data())
    return vacancies


def get_top_vacancies(file_manager, user_input_n):
    """
    Функция для получения вакансий, отсортированных по зарплате.
    """
    vacancy_list = file_manager.get_list_vacancies()
    sorted_vacancies = sorted(vacancy_list, key=lambda elem: elem['salary_from'], reverse=True)[:user_input_n]
    return sorted_vacancies


def actions_for_vacancies(file_manager):
    print('Выберете действие:\n'
          '1 - получить топ-N вакансий по зарплате\n'
          '2 - Получить отфильтрованные вакансии по минимальному уровню заработной платы\n'
          '3 - удалить вакансию по указанному критерию\n'
          '0 - выйти'
          )
    while True:
        user_input = input()
        if user_input in ('1', '2', '3', '0'):
            if user_input == '1':
                user_input_n = int(input('Введите количество вакансий для вывода '))
                top_n = get_top_vacancies(file_manager, user_input_n)
                for vac in top_n:
                    print(vac)
                break
            elif user_input == '2':
                salary_input = int(input('Введите минимальную интересующую зарплату '))
                min_salary = file_manager.get_vacancies_by_keyword({'salary_input': salary_input})
                for vac in min_salary:
                    print(vac)
                break
            elif user_input == '3':
                low_salary_input = int(input('Введите уровень зарплаты, вакансии с которой хотите удалить: '))
                file_manager.delete_vacancy(file_manager.get_vacancies_by_keyword({'salary_input': low_salary_input}))
                print(f'Вакансии удалены из файла по критерию {low_salary_input}')
                break
            elif user_input == '0':
                break
        else:
            print("Некорректный запрос. Попробуйте еще раз")


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    keyword = choose_vacancy()
    choose_platform()
    while True:
        user_input = input()
        api_list = []
        if user_input in ('1', '2', '3'):
            if user_input == '1':
                hh = HeadHunterApi(keyword)
                api_list.append(hh)
                break
            elif user_input == '2':
                sj = SuperJobApi(keyword)
                api_list.append(sj)
                break
            elif user_input == '3':
                hh = HeadHunterApi(keyword)
                sj = SuperJobApi(keyword)
                api_list.append(hh)
                api_list.append(sj)
                break
        else:
            print("Некорректный запрос. Попробуйте еще раз")

    file_manager = JsonFileManager('json_file_vacancies.json')
    file_manager.write_file(get_vacancies(api_list))
    actions_for_vacancies(file_manager)
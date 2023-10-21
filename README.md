Эта программа позволяет получать информацию о вакансиях с различных платформ, сохранять ее в файл и удобно работать с ней (добавлять,фильтровать). Платформы для сбора информации: HeadHunter и SuperJob.

#УСТАНОВКА

Для работы с программой вам потребуется Python 3.7 и выше, а также следующие библиотеки:

requests
json
 
Вы можете установить эти библиотеки с помощью команды pip, например:

pip install
requests.

Затем вы можете скачать или клонировать этот репозиторий на свой компьютер.

#ИСПОЛЬЗОВАНИЕ

Для работы с сайтом SuperJob необходимо получить api_key, подробная инструкция дается по ссылке описания документации в разделе Getting started: https://api.superjob.ru/#gettin.

Для запуска программы выполните следующую команду в терминале:

python main.py

Программа просит вас выбрать платформу для получения вакансий (hh.ru,SuperJob или обе), ввести поисковый запрос, а затем предложит различные варианты работы с данными:

Получить топ N вакансий по заработной плате
Получить отфильтрованные вакансии по минимальному уровню заработной платы
Получить вакансии, в описании которых есть определенные ключевые слова
Удалить вакансии по какому-либо критерию
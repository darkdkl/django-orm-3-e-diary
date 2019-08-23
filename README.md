# Урок 3. Исправляем записи в электронном дневнике

## Запуск сайта дневника

- Скачайте код ( https://github.com/devmanorg/e-diary/tree/master )
- Установите зависимости командой `pip install -r requirements.txt`
- Скачайте архив с БД и извлеките в папку с сайтом (https://dvmn.org/filer/canonical/1562234129/166/)
- Запустите сервер командой `python3 manage.py runserver`

##Работа с Shell

В папке с сайтом выполните :

`python3 manage.py shell`

Введите в Shell построчно код из файла scrypts.py.

В первую очередь необходимо импортировать модели,далее используйте требуемую функцию
####описание функций:
- def fix_marks            - исправляет оценки
- def remove_chastisements - удаляет замечания
- def add_commendation     - добавляет похвалу

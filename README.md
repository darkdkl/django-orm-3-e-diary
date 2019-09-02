# Исправляем записи в электронном дневнике

## Запуск сайта дневника

- Скачайте код ( https://github.com/devmanorg/e-diary/tree/master )
- Установите зависимости командой `pip install -r requirements.txt`
- Скачайте архив с БД и извлеките в папку с сайтом (https://dvmn.org/filer/canonical/1562234129/166/)
- Запустите сервер командой `python3 manage.py runserver`

## Работа с Manage Shell

В папке с сайтом выполните :

`python3 manage.py shell`


В первую очередь необходимо импортировать модели и библиотеку random.

```
from datacenter.models import Mark, Schoolkid, Chastisement, Commendation, Subject, Lesson,Teacher 
import random

```

Далее используйте требуемую функцию,вводя в Shell построчно код из файла scripts.py.

### Работа в терминале

Положите scripts.py в один каталог с manage.py,

Вызывайте необходимую функцию в ifmain.

`fix_marks('Соболев Арсений')`
 
запуйскайте скрипт:

`python3 scripts.py`



#### описание функций:

- def fix_marks            - исправляет оценки
```
fix_marks('Соболев Арсений')
```

- def remove_chastisements - удаляет замечания
```
remove_chastisements('Соболев Арсений')
```
- def add_commendation     - добавляет похвалу

```
add_commendation('Соболев Арсений','Музыка')

```
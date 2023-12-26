# FOOD_MANAGER
# №1
алго.py - Файл с алгоритмом

# №2
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver

### Логика проекта

Каталог категории - /api/v1/categories   -- GET Список категорий

Каталог подкатегорий - /api/v1/categories/<category_slug>/subcategories   -- GET Список подкатегорий категории <category_slug>

Каталог продуктов - /api/v1/categories/<category_slug>/subcategories/<subcategory_slug>/products   -- GET Список продуктов подкатегории <subcategory_slug>

Действие с добавлением в корзину - /api/v1/categories/<category_slug>/subcategories/<subcategory_slug>/products/<slug>/take/ -- Метод POST с телом count создаст (или добавит в имеющуюся) корзину продукт <slug> в количестве равном count. Метод PATCH изменит текущее количество продуктов <slug> в корзине. Метод Delete удалит текущий продукт из корзины

Действия с корзиной - /api/v1/me/ -- GET просмотр текущего состояния корзины. DELETE - удаление всей корзины

# Авторизация
/api/v1/users/ -- С телом username, password создает нового пользователя

/api/v1/jwt/create/ -- С телом username, password дает пользователю username токен

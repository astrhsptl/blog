## Проект

Этот репозиторий содержит файлы с тестовым проектом

## Структура бд

Таблица "Новости":
- id -> pk
- title -> varchar (charfield) 255
- content -> varchar (textfield) 4096
- created -> date (datefield auto_now)
- updated -> date (datefield auto_now_add)
- publicated -> boolean (booleanfield default=False)


## Формы

Форма для входа:
- email
- password

Форма для авторизации:
- firstname
- lastname
- username
- email
- password

Форма для создания новости:
- title
- content
- created (AUTOMATIC)
- updated (AUTOMATIC)
- publicated

Форма для редактирования новости:
- title
- content
- created (READONLY)
- updated (READONLY)
- publicated
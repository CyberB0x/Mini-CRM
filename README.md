# MiniCRM – Простая CRM-система на Django

MiniCRM — это миниатюрная CRM-система с возможностью управления клиентами и задачами. Проект разработан с использованием Django, Django ORM и MySQL.

## 📦 Функциональность

- Управление клиентами (создание, просмотр, редактирование, удаление)
- Управление задачами для клиентов
- Django Admin для администрирования
- Поиск и фильтрация клиентов и задач
- Суперпользователь и базовая авторизация

## 🛠️ Технологии

- Python 3.12+
- Django 5.2
- MySQL
- HTML (шаблоны Django)
- Bootstrap (по желанию, для фронта)

## 🚀 Установка

1. **Клонируйте репозиторий**:

   ```bash
   git clone https://github.com/yourusername/minicrm.git
   cd minicrm
   ```

## Создайте виртуальное окружение и активируйте его:
```commandline
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
```
## Установите зависимости:
pip install -r requirements.txt

## Настройте базу данных (в settings.py):
```commandline
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crm_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
## Примените миграции:
1. python manage.py makemigrations
2. python manage.py migrate

## Создайте суперпользователя:
python manage.py createsuperuser

## Запустите сервер:
```commandline
   python manage.py runserver
```

Перейдите на http://127.0.0.1:8000/admin, чтобы войти в админку.

## 📁 Структура
```commandline
crm_project/
├── clients/            # Приложение клиентов и задач
│   ├── models.py       # Модели Client и Task
│   ├── views.py        # Представления
│   ├── urls.py         # Маршруты
│   └── templates/      # HTML-шаблоны
├── crm_project/        # Основной проект Django
│   ├── settings.py     # Настройки
│   └── urls.py         # Глобальные маршруты
└── manage.py
```

## 📌 Заметки
Убедитесь, что вы выбрали базу данных в MySQL Workbench перед просмотром данных.

Таблицы создаются только после миграций.

Только данные, сохранённые через ORM или админку, попадают в базу.




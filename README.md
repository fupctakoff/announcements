# Demo-API проекта объявлений
# О проекте
<br>
Стек: Python, FastAPI,  PostgreSQL, SQLAlchemy, Pydantic, Alembic, Docker, fastapi-users
<br><br><br>

# Установка

### 1) Клонировать репозиторий с проектом

    git clone git@github.com:fupctakoff/announcements.git

### 2) Изменить настройки подключения к базе данных, поменяв значения переменных в файле .env в корне проекта. .env.example доступен также в корне проекта


### Предупреждение: сразу после запуска проекта необходимо воспользоваться эндпоином /create_role - создать роль администратора:

В поле name указать значение: admin
<br><br>

# Запуск

### 1) Запуск проекта
  
  docker compose up

#### Примечание

Проект доступен на порту 8000. Исполняемый файл находится: src/main.py. При первом запуске бд должна быть пуста

#### Ссылка на документацию swagger: <br> http://127.0.0.1:8000/docs 

<br>


Описание эндпоинтов:<br>
/create_role - создание роли - обязательный первый шаг<br>
/auth/login - аутентификация: username - это email пользователя<br>
/auth/logout - выход<br>
/auth/register - регистрация. По умолчанию регистрируется пользователь без привилегий<br>
/set_admin - доступно для администраторов. Позволяет наделить выбранного пользователя правами администратором<br>
/set_admin_from_user - сделать себя администратором. Эндпоинт был создан как точка входа для создания администраторов (чтобы не идти в БД)
<br><br><br>
/announcement/create_announcement_type - создание типа объявления. Неободимый шаг для последующих публикаций объявлений <br>
/announcement/create_announcement - создание объявления <br>
/announcement/announcement_list - вывод всех объявлений <br>
/announcement/detail_announcement - вывод детальной информации об объявлении <br>
/announcement/delete_announcement - удаление объявления <br>
<br><br>
/comment/create_comment - создание комментария<br>
/comment/delete_comment - удаление комментария<br>
/comment/list_comments - вывод списка комментариев к объявлению<br>

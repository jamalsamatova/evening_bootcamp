# установление postgresql (система управления базами данных - суперпользователь)
# sudo apt install postgresql postgresql-contrib
# psql --version


# вход в оболочку postgres (в меню постгреса) под юзером postgres
# sudo -i -u postgres 


# команда для подключения к базе данных (по умолчанию коннектится к постгрес бд), вход в базу данных постгреса
# psql 


# к какой базе данных подключились и с какого пользователя (инфо о соединении)
# \conninfo 


# создание пользователя role_name с паролем 1
# CREATE ROLE role_name WITH PASSWORD '1';


# создание базы данных 
# CREATE DATABASE db_name;


# список баз данных
# \l


# psql -U role_name -d role_name -h 127.0.0.1 -W
# sudo -i -u postgres 
# psql


# измени роль role_name с логином
# ALTER ROLE role_name WITH LOGIN;


# разрешение создавать базу данных
# ALTER ROLE role_name WITH CREATEDB;


# установление суперюзера
# ALTER ROLE role_name WITH SUPERUSER;


# удаление роли/юзера
# DROP ROLE role_name;


# выход
# \q
# exit


# список пользователей
# \du  (display users)


# коннект напрямую из терминала под определенным юзером, к определенной базе данных
# psql -U role_name -d role_name -h 127.0.0.1 - W
# role_name =>   доступа  нет
# role_name =#    доступ есть


# создание новой базы данных того же юзера
# CREATE DATABASE test_server;


# переход на базу данных test_server
# \c test_server


# КОМАНДА ЗАВЕРШЕНА ТОЛЬКО ПРИ =#
# Команды с \ пишутся без ;


# изменение прав пользователя
# ALTER ROLE role_name WITH some_rules;
# Rules(права)
# LOGIN / NOLOGIN
# SUPERUSER / NOSUPERUSER
# CREATEDB / NOCREATEDB
# CREATEROLE / NOCREATEROLE
# CREATEUSER / NOCREATEUSER

# изменение пароля пользователя
# ALTER ROLE role_name WITH PASSWORD 'new_password';


# проверка таблицы
# \dt

# создание таблицы с названием person
# students=# CREATE TABLE person (
# students(# name  VARCHAR(255),
# students(# surname VARCHAR(255),
# students(# age INT NOT NULL);

# открываем скобку Enter (команда не закончена, ве пишется в скобках)
# создаем строку с названием name и тип поля VARCHAR(255)
# 255 - максимальная длина строки для варчара
# создаем столбец с названием surname и тип поля VARCHAR(255)
# создаем столбец с названием age и с числовым значением и ограничением NOT NULL 
# закрываем скобку и завершаем команду

# dt
# \d person

# выбери все(*) с таблицы person
# SELECT * FROM person;

# ввод данных в таблицу
# INSERT INTO person VALUES ('John', 'Snow', 30);


###########################################################################################

# students=# INSERT INTO person (name, age) VALUES ('Helen', 40);
# INSERT 0 1
# students=# SELECT * FROM person;
#  name  | surname | age 
# -------+---------+-----
#  John  | Snow    |  30
#  Helen |         |  40
# (2 rows)

# students=# INSERT INTO person (name, surname) VALUES ('Helen', 'Jackson');
# ERROR:  null value in column "age" violates not-null constraint
# DETAIL:  Failing row contains (Helen, Jackson, null).
# students=# INSERT INTO person VALUES ('Tom', 'Tomson', 32), ('Jack', 'Jackson', 52);
# INSERT 0 2
# students=# SELECT * FROM person;
#  name  | surname | age 
# -------+---------+-----
#  John  | Snow    |  30
#  Helen |         |  40
#  Tom   | Tomson  |  32
#  Jack  | Jackson |  52
# (4 rows)

# students=# SELECT name, age FROM person;
#  name  | age 
# -------+-----
#  John  |  30
#  Helen |  40
#  Tom   |  32
#  Jack  |  52
# (4 rows)

# students=# SELECT * FROM person WHERE age > 50;
#  name | surname | age 
# ------+---------+-----
#  Jack | Jackson |  52
# (1 row)

###########################################################################################

# CREATE TABLE table_name;

# добавление данных в таблицу 
# INSERT INTO table_name (optional) VALUES (data);

# запрос в бд
# SELECT * FROM table_name;

###########################################################################################

# jamal@jamal-Inspiron-11-3147:~$ mkdir test_dir
# jamal@jamal-Inspiron-11-3147:~$ cd test_dir/
# jamal@jamal-Inspiron-11-3147:~/test_dir$ ls
# jamal@jamal-Inspiron-11-3147:~/test_dir$ python3 -m venv env
# jamal@jamal-Inspiron-11-3147:~/test_dir$ . env/bin/activate
# (env) jamal@jamal-Inspiron-11-3147:~/test_dir$ ls
# env
# (env) jamal@jamal-Inspiron-11-3147:~/test_dir$ touch requirements.txt
# (env) jamal@jamal-Inspiron-11-3147:~/test_dir$ nano requirements.txt
# (env) jamal@jamal-Inspiron-11-3147:~/test_dir$ pip3 install -r requirements.txt
# Collecting Django==3.1
#   Downloading Django-3.1-py3-none-any.whl (7.8 MB)
#      |████████████████████████████████| 7.8 MB 628 kB/s 
# Collecting psycopg2-binary
#   Downloading psycopg2_binary-2.9.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
#      |████████████████████████████████| 3.0 MB 257 kB/s 
# Collecting asgiref~=3.2.10
#   Downloading asgiref-3.2.10-py3-none-any.whl (19 kB)
# Collecting pytz
#   Downloading pytz-2021.3-py2.py3-none-any.whl (503 kB)
#      |████████████████████████████████| 503 kB 152 kB/s 
# Collecting sqlparse>=0.2.2
#   Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
#      |████████████████████████████████| 42 kB 245 kB/s 
# Installing collected packages: asgiref, pytz, sqlparse, Django, psycopg2-binary
# Successfully installed Django-3.1 asgiref-3.2.10 psycopg2-binary-2.9.3 pytz-2021.3 sqlparse-0.4.2
# (env) jamal@jamal-Inspiron-11-3147:~/test_dir$ ls
# env  requirements.txt
# (env) jamal@jamal-Inspiron-11-3147:~/test_dir$ pip3 freeze
# asgiref==3.2.10
# Django==3.1
# psycopg2-binary==2.9.3
# pytz==2021.3
# sqlparse==0.4.2
# (env) jamal@jamal-Inspiron-11-3147:~/test_dir$ django-admin startproject test_project .
# (env) jamal@jamal-Inspiron-11-3147:~/test_dir$ ls
# env  manage.py  requirements.txt  test_project
# (env) jamal@jamal-Inspiron-11-3147:~/test_dir$ python3 manage.py runserver
# Watching for file changes with StatReloader
# Performing system checks...

# System check identified no issues (0 silenced).

# You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
# Run 'python manage.py migrate' to apply them.
# February 08, 2022 - 14:08:27
# Django version 3.1, using settings 'test_project.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.
# ^C(env) jamal@jamal-Inspiron-11-3147:~/test_dir$ python3 manage.py makemigrations
# No changes detected
# (env) jamal@jamal-Inspiron-11-3147:~/test_dir$ python3 manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying admin.0002_logentry_remove_auto_add... OK
#   Applying admin.0003_logentry_add_action_flag_choices... OK
#   Applying contenttypes.0002_remove_content_type_name... OK
#   Applying auth.0002_alter_permission_name_max_length... OK
#   Applying auth.0003_alter_user_email_max_length... OK
#   Applying auth.0004_alter_user_username_opts... OK
#   Applying auth.0005_alter_user_last_login_null... OK
#   Applying auth.0006_require_contenttypes_0002... OK
#   Applying auth.0007_alter_validators_add_error_messages... OK
#   Applying auth.0008_alter_user_username_max_length... OK
#   Applying auth.0009_alter_user_last_name_max_length... OK
#   Applying auth.0010_alter_group_name_max_length... OK
#   Applying auth.0011_update_proxy_permissions... OK
#   Applying auth.0012_alter_user_first_name_max_length... OK
#   Applying sessions.0001_initial... OK
# (env) jamal@jamal-Inspiron-11-3147:~/test_dir$ python3 manage.py runserver
# Watching for file changes with StatReloader
# Performing system checks...

# System check identified no issues (0 silenced).
# February 08, 2022 - 14:10:34
# Django version 3.1, using settings 'test_project.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.
# [08/Feb/2022 14:10:57] "GET / HTTP/1.1" 200 16351
# [08/Feb/2022 14:10:57] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
# [08/Feb/2022 14:10:57] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
# [08/Feb/2022 14:10:57] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
# [08/Feb/2022 14:10:57] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
# Not Found: /favicon.ico
# [08/Feb/2022 14:10:58] "GET /favicon.ico HTTP/1.1" 404 1978

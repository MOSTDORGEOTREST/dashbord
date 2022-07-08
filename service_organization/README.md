# Сервис с API для доступа к данным компании

Запускается как микросервис. Поднимает веб-сервер на порте 8000

Парсит следующие данные:
* Протоколы по всем опытам со статистикой
* Премии по статистикой
* Дни рождения и телефоны сотрудников

Работает с сетевым диском компании. Для работы надо подключить диск к папке

Для просмотра документации по API надо перейти на http://0.0.0.0:9000/docs

## Запуск:
Подключение диска:
Для Linux привяжем сетевой диск к папке:
    
`sudo mount.cifs ip_диска/files YOUR_PATH -o user=пользователь,pass=пароль`
    
Y OUR_PATH выбираем сами. Пример: 
`/home/nick/projects/reports`

Для Windows ничего не делаем. Далее испозьзуем `YOUR_PATH = ip_диска/files`

В файле settings указываем путь к файлу

Можно запустить через контейнер:
    
`docker build -t mdgt_dashboard .
docker run -v YOUR_PATH:/files -p 8000:8000 mdgt_dashboard`



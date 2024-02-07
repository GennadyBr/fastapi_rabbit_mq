# Тестовое задание для Backend Python Developer

[Ссылка на GitHub](https://github.com/GennadyBr/fastapi_es_faq)


## Проект развернут на VPS
[Ссылка на VPS](http://5.35.83.245:8003/docs)

### Логи выводятся в консоль и в файл
logs/fastapi_elk.log


## Для локального запуска выполните следующие команды

### Скопируйте репозиторий:
git clone https://github.com/GennadyBr/fastapi_es_faq.git

### Переименуйте файл .env.example в .env:

### Запустите контейнеры:
make up

### Перейдите в папку с проектом:
cd fastapi_es_faq

### Перейдите по ссылке:
http://0.0.0.0:8003/docs

### Логи выводятся в консоль и в файл
logs/fastapi_elk.log


## Задача: 
    - Ваша задача написать веб-приложение, которое позволяет пользователям 
        - отправлять сообщения брокеру RabbitMQ, а также 
        - добавлять очередь (без роутинга)
    - При отправке сообщения пользователь может выбрать себе очередь, в которую его сообщение будет помещено. 
    - Также требуется реализовать консюмер, который будет считывать сообщения из очереди и записывать их в файл.


### Требования:
    1. Backend приложение должно быть написано на Python с использованием фреймворка FastAPI.
    2. Взаимодействие с брокером RabbitMQ должно быть реализовано с помощью библиотеки aio_pika/pika.
    3. При отправке сообщения пользователь должен получать подтверждение о том, что сообщение успешно отправлено.
    4. После отправки сообщения, оно должно быть помещено в выбранную пользователем очередь брокера RabbitMQ.
    5. Консюмер должен считывать сообщения из очереди и записывать их в файл.
    6. Каждое сообщение должно быть записано на новой строке.


### Инструкции для сдачи тестового задания:
    1. Сделайте репозиторий.
    2. Создайте ветку с название rabbit_mq.
    3. Разработайте исходный код, соответствующий требованиям задачи.
    4. Сделайте коммит и пуш ваш репозиторий.
    5. Сделайте merge вашей ветки в master-ветку.
    6. Отправьте ссылку HR или техническому специалисту 

### Удачи!

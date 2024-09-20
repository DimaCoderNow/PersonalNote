## Запуск через Docker

``` docker build -t pnote . ```

```docker run -d -p 8000:8000 pnote```

После успешного запуска можно перейти на http://127.0.0.1:8000/docs и протестировать методы

**Данные пользователя для получения токена:**

name: admin\
password: 123 

## Тестирование через Curl
  **Вход пользователя**
``` curl -X 'POST' \
  'http://localhost:8000/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "admin",
  "password": "123"
}'
 ```
 **Получение заметок пользователя**
``` curl -X 'GET' \
  'http://localhost:8000/notes' \
  -H 'accept: application/json' \
  -H 'Authorization: JNtoYuinUxMsbip8'
```
 **Добавление заметки пользователя**
 ```curl -X 'POST' \
  'http://localhost:8000/notes' \
  -H 'accept: application/json' \
  -H 'Authorization: JNtoYuinUxMsbip8' \
  -H 'Content-Type: application/json' \
  -d '{
  "text_note": "content new note"
}'
```

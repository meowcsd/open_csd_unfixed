# Open CSD unfixed

## Что это такое и как оно появилось?
Это почти немодифицированный говнокод акима из бота @csd_project_bot в телеграме
Оно тут появилось в результате второго лика сурскода (первая была тут https://t.me/xaicommunitychat/1/504247, вторая в этом репозитории)

## Что было изменено от оригинала ксд бота?
 - удалено строк 500 говнокода
 - порт ксд бота на ddosxdapis
 - удалён кандиский, заменён на pixart-alpha
 - закрыты почти все 0day (бог знает скока их в таком говне)
 - удалён `/web` ибо `@ddosxd` не смог его заставить работать без говнокода акима
 - бд отвязана от директории ./

## Известные баги
 - нехуя не работает

## Запуск локально:
### Подготовка
 - ```pip install aiogram==2.25.1```
 - ```python3 wipe``` это важно чтоб создалась чистая бд с контекстом
 - в ```bot.py``` на строке 44 и 45 меняете токен и admid
 - в ```bot.py``` на строке 882 и 883 ссылки на donationallers и yoomoney
 - ```mkdir db```
### Запуск
 - ```python3 bot.py```
 -  вроде всё, ес чот не так то сообщите дудосу в x-ai чат

## Немного удалённого говнокода

```python3
def is_akim(user_id):
  if user_id == ADMIN_ID:
    return True
  else:
    return False
```

```python3
def handle_....(...):
  ...
  if ...:
    ...
    message.text = message.text
    ...
  ...
```

```python3
async def send_message(chat_id, text):
  x = await bot.send_message(chat_id, text)
  return x

async def send_reply_message(chat_id, reply_to_message_id, text):
  x = await bot.send_message(chat_id, text, reply_to_message_id=reply_to_message_id)
  return x
```

## История
Крч появился ксд бот (как это вышло спросите в x-ai чате, тут лень писать)
Сначало типа всё ок было, студия ~~разработки ботов имени Ленина~~ астрокот особо ни с кем не конфликтовала
Потом начала конфиликтовать с X-AI (кст челы из X-AI комьюнити её и создали)
Ну и от такого через многочисленные `0day` уязвимости сурскод ксдбота сливался пару тысяч раз

# Open CSD unfixed

## !!!ВАЖНО!!!
НЕ ЗАПУСКАЙТЕ ЭТОТ КОД ОТ ПОЛЬЗОВАТЕЛЯ `root` ТК В НЁМ ОЧЕНЬ МНОГО УЯЗВИМОСТЕЙ
 - старайтесь запускать бота в изолированной среде тк
   - много 0day желательно rce от рута

## ТГ демка бота
Попробовать бота можно тут https://t.me/OpenCSD_bot

## Опенсурс альтернативы
- сидни (напишите в @xaicommynitychat за сурскодом, лень искать линк на гх)

## План развития
данный код не будет изменяться и уязвимости не будут закрываться, если будут обновы репы (тип фиксы 0day) то оно будет выходить в репе `meowcsd/open_csd`
НО вероятно я (тоесть ddosxd) нечё не буду делать
все пул реквесты если будут, буду переносить в `meowcsd/open_csd`

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
 - ~~нехуя не работает~~ настройки не работают
 - admins работают нестабильно
 - система бана хз шо с ней, вроде выпилена
 - 0day уязвимости

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

## Подробнее про зеродей
### АХАХАХАХАХХАХАХАХАХХАХАХА

., [05.02.2024 21:06]

что за зеродей был

как эксплуатировал


ddosxd, [05.02.2024 21:06]

крч

создаешь канал

туда привязываешь чат

и в чат ксд

в канале пишешь /e import os; os.system("ip a")

и оно в коментах результат


., [05.02.2024 21:07]

ААХХАХАХАХАХ

., [05.02.2024 21:07]

ты без прав был в ксд?


ddosxd, [05.02.2024 21:07]

я от аноним канала

пушто я там был забанен ваще

и от нормал юзера не давало зеродей


```python3
if is_admin(user) == False: return
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

Но если будет None, то None != False

--> условие не сработало, eval открыт


P.S я от канала не прописывал /start

оно None возвращает когда просмотр настроек пользователя

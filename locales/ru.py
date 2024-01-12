locale = {
    'start': "Привет. Я бот на нейросети Claude. Она быстрее, чем ChatGPT, а в чём-то и умнее. Пиши, что хочешь, но диалоги записываются для отладки бота. ФСБ их не показываем)\n\nСоветую зайти в чат про меня: https://t.me/???.\n\nТы можешь открыть настройки (/settings) или посмотреть подсказку (/help).\n\nПожалуйста, выбери свой язык (можно сменить мозже с /lang):",
    'about_string': """
Бот создан Акимом Чепурко на базе Claude и Kandinsky 2.1. Он может вести диалог, отвечать на вопросы, а также иллюстрировать свои ответы картинками.
Бот ещё в начальной стадии разработки. Если бот отказывается что-то делать, сначала нажмите "Reset" или напишите /reset. Если это не помогло, это либо вина Claude API и Kandinskiy (они могут быть временно недоступны), либо бот сломался (что наиболее вероятно). В любом случае, напишите Акиму.
Написать создателю бота: https://t.me/???

Мы, разработчики КСД, не несем никакой ответственности за любые, высказывания, советы или рекомендации, данные нашим ботом. Мы создали КСД исключительно для развлечения. Любые высказывания КСД, могут быть незаконными, неэтичными или опасными. Пользователи должны проявлять здравый смысл и не следовать никаким советам, которые могут быть незаконными, а также причинить вред им или другим людям. Мы не контролируем и не одобряем контент, сгенерированный КСД.
""", 
    'donate_string': """
Вы можете поддержать разработчика бота. Заранее большое спасибо за любую поддержку! P.S. лучше переводить на YooMoney, комиссия меньше.
""",   
    'help_string': """
Бот может вести диалог, отвечать на вопросы, а также иллюстрировать свои ответы картинками. Вот список команд:

/lang - выбрать язык
/csd - написать боту КСД (использовать с запросом, в ЛС можно без команды)
/reset - начать новый диалог (и удалить старый)
/dark - написать Тёмному КСД (КСД с джейлбрейком)
/web - написать Веб-КСД с доступом к интернету
/gopnik - написать гопнику Коляну
/natasha - написать девушке Наташе
/kitty - написать котёнку Мурчику
/csdimg - сгенерировать изображение по запросу (если у вас нет чёткого запроса, лучше попросите "/csd нарисуй ...")
/randimg - сгенерировать случайное изображение
/donate - поддержать бота и его разработчика
/help - показывает это сообщение
/about - информация о боте
/stats - статистика бота
/settings - настройки
/getprompts - посмотреть доступных ботов
/*ID бота* - написать любому боту из списка (они тоже запоминают диалог отдельно)
""",
    'settings_string': """Доступные настройки:

    Reply - когда вы отвечаете на сообщение бота, он будет отвечать вам.
    Picture - когда отвечает какой-то персонаж, будет показана его картинка (только в ЛС. В беседах картинка будет всегда).
    Картинок за одну генерацию с /csdimg: """,
    'reset': 'История диалога сброшена.',
    'reset2': 'Диалог сброшен.',
    'wait': "Генерирую ответ...",
    'wait_pic': "Рисую...",
    'wait_web': "Ищу...",
    'censored': "\n\n⚠️ Некоторые изображения подверглись цензуре.",
    'nomore10': "\n\n⚠️ Невоможно отправить больше 10 изображений.",
    'failedgen_img': '\n\n⚠️ Не удалось сгененировать изображения: ',
    'here_are_pics': ' Вот картинки (подождите несколько секунд):',
    'failedgen_msg': 'ERROR: Не удалось сгенерировать сообщение. Попробуйте ещё раз или сбросьте диалог. \n',
    'setlang': '🇷🇺 Установлен русский язык.',
    'chooselang': 'Выберите язык:',
    'nomore5': "ℹ️ Нельзя генерировать больше 5 картинок.",
    'noless1': 'ℹ️ Нельзя генерировать меньше 1 картинки.',
    'prompt_loc': ' Отвечай на русском.',

}

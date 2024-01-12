import aiohttp
import asyncio
import json
import random 

with open('config.json', 'r') as f:config = json.load(f)

claude_endpoint = "https://api.ddosxd.ru/v1/prompt"
img_endpoint = "https://api.ddosxd.ru/v1/image"

headers = {'Authorization': config.get('api_key')}


async def claude_chat(prompt, userId):
    payload = {
        'model': config.get('model'),
        'prompt': prompt,
        'userId':userId
    }
    # Создаем клиентскую сессию
    async with aiohttp.ClientSession() as session:
        # Отправляем POST запрос
        async with session.post(claude_endpoint, headers=headers, json=payload) as response:
            # Проверяем статус ответа
            if response.status != 200:
                raise Exception(f"Ошибка запроса: {response.status}")
            
            # Парсим JSON ответ
            response_json = await response.json()
            if 'reply' not in response_json:
                raise Exception(response_json['error'])
            return response_json.get('reply')

async def Imagine(prompt):
    payload = {
        'prompt':prompt,
        'model':config.get('img_model'),
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(img_endpoint, headers=headers, json=payload) as response:
            if response.status != 200:
                raise Exception(f"Ошибка запроса: {response.status}")
            response_json = await response.json()
            return {
                **response_json,
                'prompt':prompt
            }
    

async def main():
    completion = await claude_chat("\n\nHuman: Hi\n\nAssistant: ")
    print(completion)

if __name__ == '__main__':
    asyncio.run(main())

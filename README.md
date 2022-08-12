# steamIDwine - Модуль для работы с API Steam
**steamIDwine** - асинхронный модуль для взаимодействия с API Steam. \
Обращайся к методам и работай с атрибутами, модуль будет развиваться и в скором времени будет больше возможностей

### Ссылки 🔗
Документация [Steam Web API Documentation](https://steamcommunity.com/dev) \
Получить ключ доступа [Register Steam Web API Key](https://steamcommunity.com/dev/apikey)

## Установка 💾
- Установка с помощью пакетного менеджера pip
```
$ pip install steamIDwine
```
- Установка с GitHub (требуется [git](https://git-scm.com/downloads))
```
$ git clone https://github.com/BinAlexme/steamIDwine.git
$ cd steamIDwine
$ python setup.py install
```

## Пример 👀
```py
import asyncio
from steamIDwine import Steam

api = Steam("API_KEY")


async def handler():
    friends = await api.users.friends(76561198982570889)

    for friend in friends.friends:
        usr = await api.users.get(friend.steam_id)
        print(usr.players[0].name)


asyncio.get_event_loop().run_until_complete(handler())
```

- Каждый метод возвращает атрибуты
- У каждого метода имеется атрибут `objects`, который возвращает JSON-объект

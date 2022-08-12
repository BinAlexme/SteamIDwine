import json
import asyncio
import aiohttp

from .utils import *


class Service:

    def __init__(self, api_key, format):
        self.default_params = {
            "key": api_key,
            "format": format
        }

    async def owned_games(self, steam_id: int, *, include_appinfo: str=None, include_played_free_games: str=None, appids_filter: list=None):
        self.default_params["steamid"] = steam_id

        if include_appinfo is not None:
            self.default_params["include_appinfo"] = include_appinfo
        if include_played_free_games is not None:
            self.default_params["include_played_free_games"] = include_played_free_games
        if appids_filter is not None:
            self.default_params["appids_filter"] = appids_filter

        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/", params=self.default_params) as response:
                if self.default_params["format"] == "json":
                    data = await response.json()
                    owned_games_list = OwnedGames(data, data["response"]["game_count"])

                    for obj in data["response"]["games"]:
                        owned_games_object = OwnedGamesData(
                            obj["appid"],
                            PlaytimeForever(
                                obj["playtime_forever"],
                                obj["playtime_windows_forever"],
                                obj["playtime_mac_forever"],
                                obj["playtime_linux_forever"]
                            )
                        )
                        owned_games_list.games.append(owned_games_object)

                    return owned_games_list
                else:
                    return response.text

    async def recently_played_games(self, steam_id: int, *, count: int=2):
        self.default_params["steamid"] = steam_id
        self.default_params["count"] = count

        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/", params=self.default_params) as response:
                if self.default_params["format"] == "json":
                    data = await response.json()
                    recently_played_games_list = RecentlyPlayedGames(data, data["response"]["total_count"])

                    for obj in data["response"]["games"]:
                        recently_played_games_object = RecentlyPlayedGamesData(
                            obj["appid"],
                            obj["name"],
                            obj["playtime_2weeks"],
                            obj["img_icon_url"],
                            obj["img_logo_url"],
                            PlaytimeForever(
                                obj["playtime_forever"],
                                obj["playtime_windows_forever"],
                                obj["playtime_mac_forever"],
                                obj["playtime_linux_forever"]
                            )
                        )
                        recently_played_games_list.games.append(recently_played_games_object)

                    return recently_played_games_list
                else:
                    return response.text
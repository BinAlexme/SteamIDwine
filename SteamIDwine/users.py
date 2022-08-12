from typing import Union, List

import json
import asyncio
import aiohttp

from .utils import *


class User:

    def __init__(self, api_key, format):
        self.default_params = {
            "key": api_key,
            "format": format
        }

    async def friends(self, steam_id: int, *, relationship: str="friend"):
        self.default_params["steamid"] = steam_id
        self.default_params["relationship"] = relationship

        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.steampowered.com/ISteamUser/GetFriendList/v0001/", params=self.default_params) as response:
                if self.default_params["format"] == "json":
                    data = await response.json()
                    friends_list = FriendsList(data)
                    
                    for obj in data["friendslist"]["friends"]:
                        friends_object = FriendsData(
                            obj["steamid"],
                            obj["relationship"],
                            obj["friend_since"]
                        )
                        friends_list.friends.append(friends_object)

                    return friends_list
                else:
                    return response.text

    async def get(self, steam_ids: Union[List[str], int]):
        """In Development"""

        if not isinstance(steam_ids, list):
            steam_ids = [steam_ids]
        self.default_params["steamids"] = steam_ids

        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=self.default_params) as response:
                if self.default_params["format"] == "json":
                    data = await response.json()
                    users_list = UserResponse(data)

                    for obj in data["response"]["players"]:
                        users_object = UserResponseData(
                            obj["steamid"],
                            obj["communityvisibilitystate"],
                            obj["profilestate"],
                            obj["personaname"],
                            obj["commentpermission"],
                            obj["profileurl"],
                            Avatar(
                                obj["avatar"],
                                obj["avatarmedium"],
                                obj["avatarfull"],
                                obj["avatarhash"]
                            ),
                            obj["lastlogoff"],
                            obj["personastate"],
                            obj["primaryclanid"],
                            obj["timecreated"],
                            obj["personastateflags"]
                        )
                        users_list.players.append(users_object)

                    return users_list
                else:
                    return response.text

    async def achievements(self, steam_id: int, app_id: int):
        self.default_params["steamid"] = steam_id
        self.default_params["appid"] = app_id

        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/", params=self.default_params) as response:
                if self.default_params["format"] == "json":
                    data = await response.json()
                    achievements_list = Achievements(
                        data,
                        data["playerstats"]["steamID"],
                        data["playerstats"]["gameName"],
                        data["playerstats"]["success"]
                    )

                    for obj in data["playerstats"]["achievements"]:
                        achievements_object = AchievementsData(
                            obj["apiname"],
                            obj["achieved"],
                            obj["unlocktime"]
                        )
                        achievements_list.achievements.append(achievements_object)

                    return achievements_list
                else:
                    return response.text

    async def bans(self, steam_ids: int):
        self.default_params["steamids"] = steam_ids

        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.steampowered.com/ISteamUser/GetPlayerBans/v1", params=self.default_params) as response:
                if self.default_params["format"] == "json":
                    data = await response.json()
                    bans_list = PlayerBans(data)

                    for obj in data["players"]:
                        bans_object = PlayerBansData(
                            obj["SteamId"],
                            obj["CommunityBanned"],
                            obj["VACBanned"],
                            obj["NumberOfVACBans"],
                            obj["DaysSinceLastBan"],
                            obj["NumberOfGameBans"],
                            obj["EconomyBan"]
                        )
                        bans_list.players.append(bans_object)

                    return bans_list
                else:
                    return response.text

    async def group_list(self, steam_id: int):
        # what's this?
        self.default_params["steamid"] = steam_id

        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.steampowered.com/ISteamUser/GetUserGroupList/v1", params=self.default_params) as response:
                if self.default_params["format"] == "json":
                    data = await response.json()
                    return data
                else:
                    return response.text

    async def resolve_vanity_url(self, url: str):
        # what's this?
        self.default_params["vanityurl"] = url

        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/", params=self.default_params) as response:
                if self.default_params["format"] == "json":
                    data = await response.json()
                    return data
                else:
                    return response.text
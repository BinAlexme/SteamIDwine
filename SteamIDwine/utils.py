from dataclasses import dataclass


@dataclass
class FriendsList:

	objects: dict
	friends = []


@dataclass
class FriendsData:

	steam_id: str
	relationship: str
	friend_since: int


@dataclass
class Avatar:

	url: str
	medium: str
	full: str
	avatar_hash: str


@dataclass
class UserResponse:

	objects: dict
	players = []


@dataclass
class UserResponseData:

	steam_id: str
	community_visibility_state: int
	profile_state: int
	name: str
	comment_permission: int
	profile_url: str
	avatar: Avatar
	last_logoff: int
	personastate: int
	primary_clan_id: str = None
	time_created: str = None
	persona_state_flags: int = None
	game_id: int = None
	game_server_ip: str = None
	game_extra_info: str = None
	city_id: int = None
	loc_country_code: int = None
	loc_state_code: int = None
	loc_city_id: int = None


@dataclass
class Achievements:

	objects: dict
	steam_id: str
	game_name: str
	success: bool
	achievements = []


@dataclass
class AchievementsData:

	api_name: str
	achieved: int
	unlock_time: int


@dataclass
class OwnedGames:

	objects: dict
	game_count: int
	games = []


@dataclass
class PlaytimeForever:

	playtime_forever: int
	windows: int
	mac: int
	linux: int


@dataclass
class OwnedGamesData:

	app_id: int
	playtime: PlaytimeForever


@dataclass
class RecentlyPlayedGames:

	objects: dict
	total_count: int
	games = []


@dataclass
class RecentlyPlayedGamesData:

	app_id: int
	name: str
	playtime_2weeks: int
	icon_url: str
	logo_url: str
	playtime: PlaytimeForever


@dataclass
class PlayerBans:

	objects: dict
	players = []


@dataclass
class PlayerBansData:

	steam_id: str
	community_banned: bool
	vac_banned: bool
	number_of_vac_bans: int
	days_since_last_ban: int
	number_of_game_bans: int
	economy_ban: str
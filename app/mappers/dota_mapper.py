from typing import List

from app.models.dota_model import DotaPlayerStats, DotaTeams


def map_dota_team(team: str) -> DotaTeams:
    return DotaTeams.from_str(team=team)


def map_dota_players(request: List[dict]) -> List[DotaPlayerStats]:
    return [map_dota_player(player_json) for player_json in request]


def map_dota_player(request: dict) -> DotaPlayerStats:
    steam_id = request['steam_id']
    steam_slug = request['steam_slug']
    hero_id = request['hero_id']
    hero_name = request['hero_name']
    team = map_dota_team(request['team'])
    damage_dealt = request['damage_dealt']
    damage_taken = request['damage_taken']
    gold = request['gold']
    kills = request['kills']
    deaths = request['deaths']
    assists = request['assists']
    did_random = request['did_random']
    if not steam_id:
        raise NotImplementedError('steam_id is a required field')
    return DotaPlayerStats(
        steam_id=steam_id,
        steam_slug=steam_slug,
        hero_id=hero_id,
        hero_name=hero_name,
        team=team,
        damage_dealt=damage_dealt,
        damage_taken=damage_taken,
        gold=gold,
        kills=kills,
        deaths=deaths,
        assists=assists,
        did_random=did_random,
    )

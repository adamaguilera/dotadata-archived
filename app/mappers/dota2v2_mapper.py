from datetime import datetime

from app.mappers.dota_mapper import map_dota_players, map_dota_team
from app.models.dota2v2_model import Dota2v2WinCondition, Dota2v2PostGame


def map_dota2v2_win_condition(value: str) -> Dota2v2WinCondition:
    return Dota2v2WinCondition.from_str(label=value)


def map_dota2v2_post_game(request: dict) -> Dota2v2PostGame:
    if not request:
        raise NotImplementedError('PostGame cannot be null!')
    match_id = request['match_id']
    players = map_dota_players(request['players'])
    winner = map_dota_team(request['winner'])
    winner_reason = map_dota2v2_win_condition(request['winner_reason'])
    duration = request['duration']
    start_time = datetime.strptime(request['start_time'], '%m-%d-%Y')
    if not match_id:
        raise NotImplementedError('Match id is a required field!')
    return Dota2v2PostGame(
        match_id=match_id,
        players=players,
        winner=winner,
        winner_reason=winner_reason,
        duration=duration,
        start_time=start_time,
    )

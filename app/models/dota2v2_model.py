from enum import Enum

from pynamodb.attributes import UnicodeAttribute, NumberAttribute, ListAttribute, UTCDateTimeAttribute
from pynamodb.models import Model
from pynamodb_attributes import UnicodeEnumAttribute

from app.models.dota_model import DotaTeams, DotaPlayerStats
from app.models.meta import get_table_meta

game = 'dota2v2'


class Dota2v2WinCondition(Enum):
    UNKNOWN = 'unknown'
    ANCIENT = 'ancient'
    GG = 'gg'
    DISCONNECT = 'disconnect'

    @staticmethod
    def get_mapping() -> dict:
        return {
            'unknown': Dota2v2WinCondition.UNKNOWN,
            'ancient': Dota2v2WinCondition.ANCIENT,
            'gg': Dota2v2WinCondition.GG,
            'disconnect': Dota2v2WinCondition.DISCONNECT
        }

    @staticmethod
    def from_str(label: str):
        if label and Dota2v2WinCondition.get_mapping()[label.lower()]:
            return Dota2v2WinCondition.get_mapping()[label.lower()]
        else:
            raise NotImplementedError(f'No matching enum found for string: {label}')


class Dota2v2PostGame(Model):
    Meta = get_table_meta(game=game, name='post-game')
    match_id = UnicodeAttribute(hash_key=True)
    players = ListAttribute(of=DotaPlayerStats)
    winner = UnicodeEnumAttribute(enum_type=DotaTeams)
    winner_reason = UnicodeEnumAttribute(enum_type=Dota2v2WinCondition)
    duration = NumberAttribute()
    start_time = UTCDateTimeAttribute()

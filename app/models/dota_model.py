from enum import Enum

from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute, BooleanAttribute
from pynamodb_attributes import UnicodeEnumAttribute


class DotaTeams(Enum):
    UNKNOWN = 'unknown'
    RADIANT = 'radiant'
    DIRE = 'dire'
    SPECTATOR = 'spectator'

    @staticmethod
    def get_mapping() -> dict:
        return {
            'unknown': DotaTeams.UNKNOWN,
            'radiant': DotaTeams.RADIANT,
            'dire': DotaTeams.DIRE,
            'spectator': DotaTeams.SPECTATOR
        }

    @staticmethod
    def from_str(team: str):
        if team and DotaTeams.get_mapping()[team.lower()]:
            return DotaTeams.get_mapping()[team.lower()]
        else:
            raise NotImplementedError(f'No matching enum found for string: {team}')


class DotaPlayerStats(MapAttribute):
    steam_id = UnicodeAttribute(hash_key=True)
    steam_slug = UnicodeAttribute()
    hero_id = NumberAttribute()
    hero_name = UnicodeAttribute()
    team = UnicodeEnumAttribute(enum_type=DotaTeams)
    damage = NumberAttribute()
    damage_taken = NumberAttribute()
    gold = NumberAttribute()
    kills = NumberAttribute()
    deaths = NumberAttribute()
    assists = NumberAttribute()
    did_random = BooleanAttribute()

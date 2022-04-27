import requests

address = 'http://127.0.0.1:5000'
# url = 'https://httpbin.org/post'
url_prefix = '/dota2v2'
url = '/post-game'

# POST/form data
payload = {
    'match_id': '123456789',
    'source': 'development',
    'players': [
        {
            'steam_id': '987654321',
            'steam_slug': 'adam',
            'hero_id': 1,
            'hero_name': 'npc_dota_hero_antimage',
            'team': 'radiant',
            'damage_dealt': 12000,
            'damage_taken': 4000,
            'gold': 100000,
            'kills': 12,
            'deaths': 11,
            'assists': 10,
            'did_random': False,
        }
    ],
    'winner': 'radiant',
    'winner_reason': 'ancient',
    'duration': 1234,
    'start_time': '12-02-2022'
}

r = requests.post(f'{address}{url_prefix}{url}', json=payload)

print(r.text)

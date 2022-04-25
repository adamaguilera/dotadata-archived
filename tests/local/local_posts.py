import requests

address = 'http://127.0.0.1:5000'
# url = 'https://httpbin.org/post'
url_prefix = '/dota2v2'
url = '/post-game'

# POST/form data
payload = {
    'match_id': '123456789',
    'players': [
        {
            'steam_id': '987654321',
            'steam_slug': 'adam',
            'team': 'radiant',
            'damage': 12000,
            'gold': 100000,
            'kills': 12,
            'deaths': 11,
            'assists': 10,
        }
    ],
    'winner': 'radiant',
    'winner_reason': 'ancient',
    'duration': 1234,
    'start_time': '12-02-2022'
}

r = requests.post(f'{address}{url_prefix}{url}', json=payload)

print(r.text)

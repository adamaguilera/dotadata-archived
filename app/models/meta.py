from app.app import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY, ENV


def get_table_meta(game: str, name: str):
    class Meta:
        table_name = f'{ENV}-{game}-{name}'
        read_capacity_units = 50
        write_capacity_units = 50
        aws_access_key_id = AWS_ACCESS_KEY
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    return Meta

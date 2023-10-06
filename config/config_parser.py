import configparser

config = configparser.ConfigParser()
config.read("config/development.ini")


def get_open_ai_key():
    return config["openai"]["api_key"]

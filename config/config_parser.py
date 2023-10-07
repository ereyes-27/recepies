import configparser

config = configparser.ConfigParser()
config.read("config/development.ini")


def get_open_ai_key():
    return config["openai"]["api_key"]


def get_mongo_cloud_conn():
    return config["mongodb"]["cloud_conn"]


def get_mongo_local_conn():
    return config["mongodb"]["local_conn"]

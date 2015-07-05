__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'


from os import environ
def __from_env_or_default(key, default):
    """
    Check the environment for variable or return default
    :param key: variable to get
    :type: str
    :param default: default value if missing
    :return: value

    """
    if key in environ:
        return environ[key]
    else:
        return default

"""Application configuration variables"""
MONGO_IP    = __from_env_or_default("MONGO_IP", "127.0.0.1")
MONGO_PORT  = __from_env_or_default("MONGO_PORT", 27017)
MONGO_DATABASE = __from_env_or_default("MONGO_DATABASE", "preprocessing")
TROVE_KEY      = __from_env_or_default("TROVE_KEY", "")
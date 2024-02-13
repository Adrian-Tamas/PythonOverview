import configparser
import os

# os.environ.__setitem__("secret", "newsecretpass")
env = os.environ.get("secret") or "secretpass"

configuration = configparser.ConfigParser(allow_no_value=True)
configuration.read("config.ini")

if __name__ == '__main__':
    print("Environment variable", env)
    print("Default section")
    print("User: ", configuration['default']["user"])
    print("Auth: ", configuration['default']["auth"])
    print("Prod section")
    print("User: ", configuration['prod']["user"])
    print("Auth: ", configuration['prod']["auth"])

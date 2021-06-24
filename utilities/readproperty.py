import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('basic info','baseurl')
        return url

    @staticmethod
    def getusername():
        username = config.get('basic info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('basic info', 'password')
        return password

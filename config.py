# config.py
import configparser
import os

class Config:
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self._check_and_create_config()
        self._load_config()

    def _check_and_create_config(self):
        if not os.path.exists(self.config_file):
            self.config['DEFAULT'] = {
                'Creator': 'SK_la',
                'HP': '8',
                'OD': '7',
                'Source': 'EZ2AC',
                'Tags': '',
                'noS': 'N',
                'noP': 'N',
                'Packset': 'N'
            }
            with open(self.config_file, 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)

    def _load_config(self):
        self.config.read(self.config_file)
        self.creator = self.config.get('DEFAULT', 'Creator')
        self.HP = self.config.get('DEFAULT', 'HP')
        self.OD = self.config.get('DEFAULT', 'OD')
        self.source = self.config.get('DEFAULT', 'Source')
        self.tags = self.config.get('DEFAULT', 'Tags')
        self.noS = self.config.get('DEFAULT', 'noS')
        self.noP = self.config.get('DEFAULT', 'noP')
        self.packset = self.config.get('DEFAULT', 'Packset')

    def save_config(self, settings):
        self.config['DEFAULT'] = {
            'Creator': settings['creator'],
            'HP': settings['HP'],
            'OD': settings['OD'],
            'Source': settings['source'],
            'Tags': settings['tags'],
            'noS': settings['noS'],
            'noP': settings['noP'],
            'Packset': settings['packset']
        }
        with open(self.config_file, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

# 单例模式实现
_config_instance = None

def get_config():
    global _config_instance
    if _config_instance is None:
        _config_instance = Config()
    return _config_instance

config = get_config()

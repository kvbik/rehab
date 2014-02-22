from paver.easy import path

class Configuration(object):
    "configuration wrapper"
    _CONFIG = {}

    def __init__(self, name):
        self.name = name
        self.data = {}

    def load_data(self):
        self.data.update(self._CONFIG)

    @classmethod
    def parse(cls, argv):
        "parse command line options and load configuration"
        config = cls('empty')
        config.load_data()
        options = {}
        return config, options

    @property
    def repodir(self):
        return path(self.data['repodir'])

    def get_updatehooks(self, name):
        updatehooks = self.data['updatehooks']
        return updatehooks.get(name, [])


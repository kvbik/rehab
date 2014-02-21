class Configuration(object):
    "configuration wrapper"
    _CONFIG = {}

    def __init__(self, config):
        self.config = config
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


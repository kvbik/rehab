import yaml
from paver.easy import path

class ConfigurationNoFile(object):
    "configuration wrapper"
    _D = {}

    def __init__(self, name):
        self.name = name
        self.data = {}

    @classmethod
    def default(cls):
        # FIXME: use venv as default and fallback to /etc/
        return cls._D.get('name', '/etc/rehab.yml')

    @classmethod
    def parse(cls, options):
        "parse command line options and load configuration"
        name = options.get('config', cls.default())
        config = cls(name)
        config.load()
        return config

    def load(self):
        pass

    @property
    def repodir(self):
        return path(self.data['repodir'])

    def get_updatehooks(self, name):
        updatehooks = self.data['updatehooks']
        return updatehooks.get(name, [])

    def get_previous_version(self, name):
        previous_versions = self.data.get('previous_versions', {})
        return previous_versions.get(name)

    def set_previous_version(self, name, current_version):
        self.data.setdefault('previous_versions', {})
        self.data['previous_versions'][name] = current_version

class Configuration(ConfigurationNoFile):
    "configuration wrapper that can store data in file"

    def load(self):
        f = open(self.name)
        d = yaml.load(f.read())
        self.data.update(d)
        f.close()

    def dump(self):
        d = yaml.dump(self.data)
        f = open(self.name, 'w')
        f.write(d)
        f.close()


import sys

class Repository(object):
    @classmethod
    def by_tag(cls, tag, name, *args):
        "create repository of proper class given by tag"
        classes = {
            'git': Git,
        }
        C = classes.get(tag, cls)
        return C(name, *args)

    @classmethod
    def loop(cls, config, options):
        "iterate through repositories from config"
        for i in config.data['repositories']:
            tag, name = i[:2]
            args = i[2:]
            yield cls.by_tag(tag, name, *args)

    def __init__(self, name, *args, **kwargs):
        self.name = name

class Git(Repository):
    "git vcs abstraction"

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

class Configuration(object):
    "configuration wrapper"

    def __init__(self, config, data=None):
        self.config = config
        self.data = data or {}

    @classmethod
    def parse(cls, argv):
        "parse command line options and load configuration"
        config = cls('empty')
        options = {}
        return config, options

def main(argv=None):
    if argv is None:
        argv = sys.argv
    config, options = Configuration.parse(argv)

if __name__ == '__main__':
    main()


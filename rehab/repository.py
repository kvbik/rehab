class Repository(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name

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
        for i in config.data.get('repositories', []):
            tag, name = i[:2]
            args = i[2:]
            yield cls.by_tag(tag, name, *args)

    @property
    def updatehooks(self):
        # TODO: take values from config
        return [('file.txt', 'echo file.txt has changed')]

    @property
    def current_version(self):
        return '1'

    def has_changed(self, file_path):
        return True

    def run_command(self, command):
        pass

    def run_update_hooks(self):
        "tak all the hooks and run commands if given file has changed"
        for file_path, command in self.updatehooks:
            if self.has_changed(file_path):
                self.run_command(command)

class Git(Repository):
    "git vcs abstraction"

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch


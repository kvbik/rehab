import sys
from paver import tasks
from paver.easy import cmdopts, path

import rehab
from rehab.configuration import ConfigurationFile
from rehab.repository import Repository

def main(argv=None):
    if argv is None:
        argv = sys.argv

    if not ('-f' in argv and '--file' in argv):
        pavement = path(rehab.__file__).dirname() / 'main.py'
        args = ['-f', pavement] + argv[1:]

    tasks.main(args)

@cmdopts([
    ('config=', 'c', 'custom configuration file'),
])
def update(options):
    "update repositories and run hooks there"
    config = ConfigurationFile.parse(options)

    for r in Repository.loop(config, options):
        r.update()
        r.run_update_hooks()
        config.set_previous_version(r.name, r.current_version)

    config.dump()

if __name__ == '__main__':
    main()


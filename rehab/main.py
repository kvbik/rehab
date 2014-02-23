import sys

from rehab.configuration import Configuration
from rehab.repository import Repository

def main(argv=None):
    if argv is None:
        argv = sys.argv
    config, options = Configuration.parse(argv)

    for r in Repository.loop(config, options):
        r.update()
        r.run_update_hooks()
        config.set_previous_version(r.name, r.current_version)

    config.dump()

if __name__ == '__main__':
    main()


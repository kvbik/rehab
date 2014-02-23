from nose import tools

from paver.easy import path
import tempfile
import yaml

from rehab.main import main
from rehab.configuration import Configuration

# basic rehab configuration, default values will be pretty similar
EXAPMLE_CONFIG = {
    # where your repositories will checkout to
    'repodir': '/var/repos/',

    # list of repositories: type, name and other params
    'repositories': [
        ('git', 'git@github.com:kvbik/python-baf.git', 'master'),
    ],

    # run commands for each file which has changed since the last run
    'updatehooks': {
        'git@github.com:kvbik/python-baf.git': [
            ('requirements.txt', 'pip install -r requirements.txt'),
            ('requirements.txt', 'python setup.py develop'),
            ('setup.py', 'python setup.py develop'),
        ],
    },

    # versions stored from previous update run
    'previous_versions': {
        'git@github.com:kvbik/python-baf.git': 'f917730de114db30e79e362cdd3ce39974f5ba84',
    },
}

# we use yaml as a config parser
DUMMY_CONFIG = """
repositories:
- [base, a-repo]
updatehooks:
  a-repo:
  - [a-file, do something]
  - [another-file, do something else]
previous_versions:
  a-repo: '10'
  another-repo: '123'
"""

def test_main_just_run_it_so_there_is_no_syntax_error():
    # TODO: use TestCase and SetUp/TearDown
    temp = path(tempfile.mkdtemp(prefix='test_rehab_'))
    name = temp / 'rehab.yml'
    f = open(name, 'w')
    f.write(DUMMY_CONFIG)
    f.close()

    Configuration._D['name'] = name

    main(['rehab.py', 'update'])

    # previous commits has changed
    f = open(name)
    tools.assert_in("a-repo: '1'", f.read())
    f.close()

    del Configuration._D['name']
    temp.rmtree()


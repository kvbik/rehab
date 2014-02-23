from nose import tools
from unittest import TestCase

from paver.easy import path
import tempfile

from rehab.main import main
from rehab.configuration import ConfigurationFile

from test_rehab.utils import RepositoryTesting

# basic rehab configuration, default values will be pretty similar
EXAMPLE_CONFIG = {
    # where your repositories will checkout to
    'repodir': '/var/repos/',

    # list of repositories: type, name and other params
    'repositories': [
        ('git', 'git@github.com:kvbik/rehab.git', 'master'),
    ],

    # run commands for each file which has changed since the last run
    'updatehooks': {
        'git@github.com:kvbik/rehab.git': [
            ('requirements.txt', 'pip install -r requirements.txt'),
            ('requirements.txt', 'python setup.py develop'),
            ('setup.py', 'python setup.py develop'),
        ],
    },

    # versions stored from previous update run
    'previous_versions': {
        'git@github.com:kvbik/rehab.git': 'f917730de114db30e79e362cdd3ce39974f5ba84',
    },
}

# we use yaml as a config parser
DUMMY_CONFIG = """
repodir: /var/repos
repositories:
- [test, a-repo]
updatehooks:
  a-repo:
  - [a-file, do something]
  - [another-file, do something else]
previous_versions:
  a-repo: '10'
  another-repo: '123'
"""

class TestMain(TestCase):
    def setUp(self):
        self.temp = path(tempfile.mkdtemp(prefix='test_rehab_'))
        self.name = self.temp / 'rehab.yml'
        with open(self.name, 'w') as f:
            f.write(DUMMY_CONFIG)

        ConfigurationFile._D['name'] = self.name
        RepositoryTesting.register()

    def test_main_just_run_it_so_there_is_no_syntax_error(self):
        main(['rehab.py', 'update'])

        # previous commits has changed
        with open(self.name) as f:
            tools.assert_in("a-repo: '1'", f.read())

    def tearDown(self):
        del ConfigurationFile._D['name']
        RepositoryTesting.unregister()
        self.temp.rmtree()


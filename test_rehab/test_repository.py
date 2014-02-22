from nose import tools
from unittest import TestCase

from paver.easy import path
import tempfile
import tarfile

from rehab.repository import Git, Repository
from rehab.configuration import Configuration

import test_rehab

def extract_git(where):
    tar = tarfile.open(path(test_rehab.__file__).dirname() / "repos.tar")
    tar.extractall(where)
    tar.close()

class TestGitRepository(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = path(tempfile.mkdtemp(prefix='test_rehab_'))
        extract_git(cls.temp)
        cls.repo = cls.temp / 'repos' / 'repo'
        cls.origin = cls.temp / 'repos' / 'repo.git'
        cls.config = Configuration('/etc/rehab.yml')
        cls.config.data = {
            'repodir': str(cls.temp / 'repos'),
        }

    @classmethod
    def tearDownClass(cls):
        cls.temp.rmtree()

    def test_repository_exists(self):
        tools.assert_true(self.repo.exists())
        tools.assert_true(self.origin.exists())

    def test_repository_properties(self):
        git = Git(self.origin, config=self.config, branch='master')
        tools.assert_equals(self.origin, git.name)
        tools.assert_equals(self.origin, git.url)
        tools.assert_equals('repo', git.directory)

    def test_repository_run_command_output(self):
        git = Git(self.origin, config=self.config, branch='master')
        tools.assert_equals(str(self.repo), git.run_command('pwd'))

def test_repo_object_and_its_properties():
    repo = Repository('name', config=None)
    tools.assert_equals('name', repo.name)
    tools.assert_equals('1', repo.current_version)
    tools.assert_true(repo.has_changed('any-file-name.txt'))

def test_repo_create_by_tag_proper_object():
    repo = Repository.by_tag('a-default', 'name', config=None)
    tools.assert_is_instance(repo, Repository)

def test_repo_run_update_hooks_iterates_over_all_given_files():
    conf = Configuration('conf')
    conf.data.update({'updatehooks': {
        'REPO': [('file.txt', 'echo file.txt has changed')],
    }})
    repo = Repository('REPO', config=conf)
    repo.run_update_hooks()

def test_repo_loop_iterates_over_repositories_from_config():
    conf = Configuration('conf')
    conf.data.update({'repositories': [
        ('git', 'git@github.com:kvbik/python-baf.git', 'master'),
    ]})
    repo = list(Repository.loop(conf, {}))[0]
    tools.assert_is_instance(repo, Git)
    tools.assert_equals('git@github.com:kvbik/python-baf.git', repo.name)
    tools.assert_equals('master', repo.branch)


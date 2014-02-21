from nose import tools

from rehab.repository import Git, Repository
from rehab.configuration import Configuration

from test_rehab import CONFIG

def test_repo_object_and_its_properties():
    repo = Repository('name')
    tools.assert_equals('name', repo.name)
    tools.assert_equals([('file.txt', 'echo file.txt has changed')], repo.updatehooks)
    tools.assert_equals('1', repo.current_version)
    tools.assert_true(repo.has_changed('any-file-name.txt'))

def test_repo_create_by_tag_proper_object():
    repo = Repository.by_tag('a-default', 'name')
    tools.assert_is_instance(repo, Repository)

def test_repo_run_update_hooks_iterates_over_all_given_files():
    repo = Repository('name')
    repo.run_update_hooks()

def test_repo_loop_iterates_over_repositories_from_config():
    conf = Configuration('conf')
    conf.data.update(CONFIG)
    tools.assert_equals(CONFIG, conf.data)
    repo = list(Repository.loop(conf, {}))[0]
    tools.assert_is_instance(repo, Git)
    tools.assert_equals('git@github.com:kvbik/python-baf.git', repo.name)
    tools.assert_equals('master', repo.branch)


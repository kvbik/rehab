from nose import tools

from rehab.main import main
from rehab.main import Git, Repository
from rehab.main import Configuration

# basic rehab configuration, default values will be pretty similar
CONFIG = {
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
}

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

def test_config_object_and_its_properties():
    conf = Configuration('/etc/rehab.yml')
    tools.assert_equals('/etc/rehab.yml', conf.config)
    tools.assert_equals({}, conf.data)

def test_config_parse_load_some_config_object_and_create_options_dict():
    config, options = Configuration.parse(['rehab', 'option'])
    tools.assert_is_instance(config, Configuration)
    tools.assert_equals({}, options)

def test_main_just_run_it_so_there_is_no_syntax_error():
    Configuration._CONFIG.update(CONFIG)
    main(['rehab', 'option'])
    main()
    Configuration._CONFIG.clear()


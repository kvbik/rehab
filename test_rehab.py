from nose import tools

from rehab import main
from rehab import Git, Repository
from rehab import Configuration

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
    tools.assert_equals('name', Repository('name').name)

def test_repo_create_by_tag_proper_object():
    repo = Repository.by_tag('whatever', 'name')
    tools.assert_is_instance(repo, Repository)

def test_repo_loop_iterates_over_repositories_from_config():
    conf = Configuration('conf', CONFIG)
    repo = list(Repository.loop(conf, {}))[0]
    tools.assert_is_instance(repo, Git)
    tools.assert_equals('git@github.com:kvbik/python-baf.git', repo.name)
    tools.assert_equals('master', repo.branch)

def test_config_object_and_its_properties():
    conf = Configuration('blah')
    tools.assert_equals('blah', conf.config)
    tools.assert_equals({}, conf.data)

def test_config_with_data_contains_data():
    conf = Configuration('with-data', CONFIG)
    tools.assert_equals('with-data', conf.config)
    tools.assert_equals(CONFIG, conf.data)

def test_config_parse_load_some_config_object_and_create_options_dict():
    config, options = Configuration.parse(['rehab', 'option'])
    tools.assert_is_instance(config, Configuration)
    tools.assert_equals({}, options)

def test_main_just_run_it_so_there_is_no_syntax_error():
    main(['rehab', 'option'])
    main()


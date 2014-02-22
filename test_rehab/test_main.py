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

DUMMY_CONFIG = {
    'repositories': [
        ('base', 'a-repo'),
    ],
    'updatehooks': {
        'a-repo': [
            ('a-file', 'do something'),
            ('another-file', 'do something else'),
        ],
    },
}

def test_main_just_run_it_so_there_is_no_syntax_error():
    Configuration._CONFIG.update(DUMMY_CONFIG)
    main(['rehab', 'option'])
    main()
    Configuration._CONFIG.clear()


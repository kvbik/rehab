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


coverage erase
nosetests --with-coverage --cover-package=rehab
coverage html --include='rehab*'

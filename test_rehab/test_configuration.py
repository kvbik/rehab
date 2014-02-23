from nose import tools

from rehab.configuration import Configuration

def test_config_object_and_its_properties():
    conf = Configuration('/etc/my-rehab.yml', '/var/my-rehab.yml')
    tools.assert_equals('/etc/my-rehab.yml', conf.config_file)
    tools.assert_equals('/var/my-rehab.yml', conf.data_file)
    tools.assert_equals({}, conf.configuration)

    conf = Configuration(configuration={'repodir': '/var/repos'})
    tools.assert_equals('/var/repos', str(conf.repodir))

def test_config_parse_load_some_config_object():
    config = Configuration.parse({'config': '/etc/rehab.yml', 'data': '/var/rehab.yml'})
    tools.assert_is_instance(config, Configuration)

def test_config_set_current_version():
    conf = Configuration()
    conf.set_previous_version('repo', '10')
    tools.assert_equals('10', conf.get_previous_version('repo'))


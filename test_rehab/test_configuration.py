from nose import tools

from rehab.configuration import Configuration, ConfigurationFile

def test_config_object_and_its_properties():
    conf = Configuration()
    tools.assert_equals({}, conf.configuration)
    tools.assert_equals({}, conf.data)

    conf = Configuration(configuration={
        'repodir': '/var/repos',
        'updatehooks': {'name': [(1,1), (2,2)]},
    })
    tools.assert_equals('/var/repos', str(conf.repodir))
    tools.assert_equals([(1,1), (2,2)], conf.get_updatehooks('name'))

def test_config_set_current_version():
    conf = Configuration()
    conf.set_previous_version('repo', '10')
    tools.assert_equals('10', conf.get_previous_version('repo'))

def test_config_parse_load_some_config_object():
    config = ConfigurationFile.parse({'config': '/etc/my-rehab.yml', 'data': '/var/my-rehab.yml'})
    tools.assert_is_instance(config, ConfigurationFile)
    tools.assert_equals('/etc/my-rehab.yml', config.config_file)
    tools.assert_equals('/var/my-rehab.yml', config.data_file)

def test_config_with_default_values():
    config = ConfigurationFile()
    tools.assert_equals('/etc/rehab.yml', config.config_file)
    tools.assert_equals('/var/rehab.yml', config.data_file)


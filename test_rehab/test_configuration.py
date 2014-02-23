from nose import tools

from rehab.configuration import ConfigurationNoFile

def test_config_object_and_its_properties():
    conf = ConfigurationNoFile('/etc/rehab.yml')
    tools.assert_equals('/etc/rehab.yml', conf.name)
    tools.assert_equals({}, conf.data)

def test_config_parse_load_some_config_object():
    ConfigurationNoFile._D['name'] = '/etc/rehab.yml'
    config = ConfigurationNoFile.parse({})
    tools.assert_is_instance(config, ConfigurationNoFile)
    del ConfigurationNoFile._D['name']

def test_config_set_current_version():
    conf = ConfigurationNoFile('/etc/rehab.yml')
    conf.set_previous_version('repo', '10')
    tools.assert_equals('10', conf.get_previous_version('repo'))



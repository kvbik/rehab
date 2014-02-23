from nose import tools

from rehab.configuration import Configuration

def test_config_object_and_its_properties():
    conf = Configuration('/etc/rehab.yml')
    tools.assert_equals('/etc/rehab.yml', conf.name)
    tools.assert_equals({}, conf.data)

def test_config_parse_load_some_config_object():
    Configuration._D['name'] = '/etc/rehab.yml'
    config = Configuration.parse({})
    tools.assert_is_instance(config, Configuration)
    del Configuration._D['name']

def test_config_set_current_version():
    conf = Configuration('/etc/rehab.yml')
    conf.set_previous_version('repo', '10')
    tools.assert_equals('10', conf.get_previous_version('repo'))



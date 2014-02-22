from nose import tools

from rehab.configuration import Configuration

def test_config_object_and_its_properties():
    conf = Configuration('/etc/rehab.yml')
    tools.assert_equals('/etc/rehab.yml', conf.name)
    tools.assert_equals({}, conf.data)

def test_config_parse_load_some_config_object_and_create_options_dict():
    config, options = Configuration.parse(['rehab', 'option'])
    tools.assert_is_instance(config, Configuration)
    tools.assert_equals({}, options)


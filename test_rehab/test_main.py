from rehab.main import main

from rehab.configuration import Configuration

from test_rehab import CONFIG

def test_main_just_run_it_so_there_is_no_syntax_error():
    Configuration._CONFIG.update(CONFIG)
    main(['rehab', 'option'])
    main()
    Configuration._CONFIG.clear()


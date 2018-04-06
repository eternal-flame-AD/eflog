import os
import sys


parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


def test_write_log():
    from eflog import logger
    f = open('tests/test.log', mode='w')
    test_logger = logger(writer=f)
    test_logger.log_info_message('tester', 'this is a info message')
    test_logger.log_warning_message('tester', 'this is a warning message')
    test_logger.log_severe_message('tester', 'this is a severe message')
    test_logger.log_fatal_message('tester', 'this is a fatal message')
    f.close()
    f = open('tests/test.log', mode='r')
    for row in f.readlines():
        assert 'tester' in row
        assert 'this is' in row
        if 'INFO' in row:
            assert 'info' in row
        elif 'WARNING' in row:
            assert 'warning' in row
        elif 'SEVERE' in row:
            assert 'severe' in row
        elif 'FATAL' in row:
            assert 'fatal' in row
        else:
            assert False

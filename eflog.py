import sys
from common import loghandler


class logger():
    def __init__(self, stdout=True, writer=None, showdate=False):
        self.stdout = stdout
        self.showdate = showdate
        self.writer = writer

    def _outputitem(self, item):
        if self.stdout:
            item.Printlogitem(self.showdate)
        if self.writer:
            item.Writelogitem(self.writer, self.showdate)

    def log_info_message(self, source, desc):
        item = loghandler.logitem(source, 'INFO', desc)
        self._outputitem(item)

    def log_warning_message(self, source, desc):
        item = loghandler.logitem(source, 'WARNING', desc)
        self._outputitem(item)

    def log_severe_message(self, source, desc):
        item = loghandler.logitem(source, 'SEVERE', desc)
        self._outputitem(item)

    def log_fatal_message(self, source, desc):
        item = loghandler.logitem(source, 'FATAL', desc)
        self._outputitem(item)

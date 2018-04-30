from common import loghandler


class logger():
    def __init__(self, stdout=True, writer=None, showdate=False,
                 minseverity="INFO"):
        self.stdout = stdout
        self.showdate = showdate
        self.writer = writer
        self.minseverity = minseverity

    def _outputitem(self, item):
        if loghandler.severity_gt(self.minseverity, item.severity):
            return  # log item is less severe than minseverity
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

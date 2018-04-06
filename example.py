import eflog
logger = eflog.logger(writer=open("./example.log", mode="a"), showdate=True)
logger.log_fatal_message("tester", "test fatal message")
logger.log_severe_message("tester3", "test sev")
logger.log_warning_message("e3e2", "warn")
logger.log_info_message("infotester", "test info message")

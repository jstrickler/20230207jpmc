import sys
import logging
import logging.handlers
from getpass import getpass

# logging.basicConfig(level=logging.DEBUG, format="huh??")

LOG_FILENAME = '../LOGS/multiple.log'

# set up formatting for all handlers (but could be different for each)
formatter = logging.Formatter(
    '%(levelname)-9s %(name)s %(asctime)s %(message)s',
    '%x %X',
)  # create formatter for all logs


# log to STDOUT for DEBUG and higher
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

# log to a file for all levels INFO and higher
file_handler = logging.FileHandler(LOG_FILENAME)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
from apple import apple
from banana import banana

# log to email for CRITICAL
smtp_password = getpass("smtp password: ")

email_handler = logging.handlers.SMTPHandler(
    ('smtp2go.com', 2525),
    f'{__name__}@pythonclass.com',
    ['jstrickler@gmail.com'],
    'ThisApplication Log Entry',
    ('pythonclass', smtp_password),
)
email_handler.setLevel(logging.CRITICAL)

log = logging.getLogger()  # create Logger object

log.addHandler(stream_handler)
log.addHandler(file_handler)
log.addHandler(email_handler)

# list handlers
print("HANDLERS:")
for handler in log.handlers:
    print(handler)
print()

log.setLevel(logging.DEBUG)  # optional

apple()
log.debug("alpha")
log.info("beta")
log.warning("gamma")
log.error("delta")
banana()
log.critical("epsilon")
log.warning('zeta')
log.warning('eta')
log.critical("theta")
apple()
banana()
log.debug("iota")
log.error("kappa")
log.warning("lambda")
log.warning("mu")
log.warning("nu")
log.critical("rho")
banana()

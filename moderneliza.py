#import support and python2/3 compatability support
import logging
import random
import re
from collections import namedtuple

# Fix Python2/Python3 incompatibility
try: input = raw_input
except NameError: pass

log = logging.getLogger(__name__)
import os
from setup import firstrun
from utils.stt import listen

if (os.getenv('SCHOOLBUDDY_FIRSTRUN') == "yes"):
    firstrun()
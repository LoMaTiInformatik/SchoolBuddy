import os
from setup import first_run
from utils.stt import listen

if (os.getenv('SCHOOLBUDDY_FIRSTRUN') == "yes"):
    first_run()
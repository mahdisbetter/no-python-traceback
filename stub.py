#-----------ANTIDBG
import sys
import traceback
import logging
import warnings
traceback.print_tb = lambda *args, **kwargs: None
traceback.print_exception = lambda *args, **kwargs: None
traceback.format_exc = lambda *args, **kwargs: ''
traceback.format_exception = lambda *args, **kwargs: ''
traceback.extract_tb = lambda *args, **kwargs: []
traceback.format_tb = lambda *args, **kwargs: ''
logging.getLogger().setLevel(logging.NOTSET)
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
warnings.filterwarnings("ignore")
def custom_excepthook(exc_type, exc_value, exc_traceback):
    pass
def custom_settrace(func):
    pass 
sys.excepthook = custom_excepthook
sys.settrace = custom_settrace
sys.stderr = None
#-----------ANTIDBG

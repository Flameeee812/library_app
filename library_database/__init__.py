from .library_funcs.main_library_funcs import *
from .config import DATABASE_PATH


Library = get_connection(path=DATABASE_PATH)

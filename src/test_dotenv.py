import pprint as pp
from dotenv import dotenv_values

pp.pprint(dotenv_values(".env"))

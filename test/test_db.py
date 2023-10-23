from unittest.mock import Mock
from scripts import sql_pyscript
class TestApp(unittest.TestCase): 
    @classmethod
    def setUpClass(cls): 
        db = sql_pyscript.init() 
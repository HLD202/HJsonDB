from json import dump, loads
from os import listdir, makedirs
from shutil import rmtree


INTIGER = "INTIGER"
FLOAT = "FLOAT"
STRING = "STRING"
BOAL = "BOAL"
BLOB = "BLOB"


class DBManager():
    def __init__(self, 
        db_name: str, 
        path: str = './',
        secret_key: str = None): 

        self.db_name = db_name
        self.path = path
        self.secret_key = secret_key


    def __check_db_name(self, db_name: str = None) -> str:
        if db_name == None or type(db_name) != str:
            raise ValueError('unacceptable Value for db_name')

        if db_name[:-5] != '.json': 
            db_name = db_name + '.json'

        print(db_name)
        return db_name
        

    def _exist_db(self, db_name: str = None):
            if db_name:
                db_name = self.__check_db_name(db_name)
                path = self.path
                if db_name in listdir(path): 
                    return True
                
                else:
                    return False
            
            else: 
                db_name = self.db_name
                db_name = self.__check_db_name(db_name)
                path = self.path

                if db_name in listdir(path): 
                    return True
                
                else:
                    return False


    def _exist_tb(self): ... 
        

    def create_db(self): ...

    def remove_db(self, force_remove: bool = False): ...

    def create_table(self, table_name: str): ...

    def remove_table(self, table_name: str, force_remove: bool = False): ...


    




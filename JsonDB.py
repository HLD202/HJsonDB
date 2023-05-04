from json import dump, loads
from os import listdir, makedirs
from os.path import exists as fileExists
from os import remove
from shutil import rmtree


INTIGER = "INTIGER"
FLOAT = "FLOAT"
STRING = "STRING"
BOOL = "BOOL"
BLOB = "BLOB"


class DBManager():
    def __init__(self, db_name: str = None, db_path: str = './', secret_key: str = None): 

        if db_name != None:
            self.db_name = self.__check_db_name(db_name)

        self.db_path = self.__check_path_name(db_path)
        self.secret_key = secret_key


    def __check_db_name(self, db_name: str = None) -> str:
        if db_name == None:
            db_name = self.db_name
        
        if type(db_name) != str:
            raise ValueError('unacceptable Value for db_name')

        if db_name[-5:] != '.json': 
            db_name = db_name + '.json'

        return db_name
        
    
    def __check_path_name(self, db_path: str = None) -> str:

        if db_path == None:
            db_path = self.db_path

        if db_path[0] != '/':

            # it means relative db_path
            if db_path[:2] != './':
                db_path = './' + db_path

        if db_path[-1] != '/':
            db_path = db_path + '/'

        return db_path    


    def create_db(self, db_name: str = None, db_path: str = './', replace: bool = False) -> None: 

        db_name = self.__check_db_name(db_name)
        db_path = self.__check_path_name(db_path)

        full_path = db_path + db_name
        if replace == False:
            if fileExists(full_path):
                raise FileExistsError

        try: 
            makedirs(db_path)
            
        except FileExistsError:
            pass

        # create an emplty json file
        with open(full_path, 'w') as f:
            f.write("")


    def remove_db(self, db_name: str = None, db_path: str = None ,force_remove: bool = False) -> None: 
        db_name = self.__check_db_name(db_name)
        db_path = self.__check_path_name(db_path)

        full_path = db_path + db_name
        if force_remove == False:
            if fileExists(full_path):
                with open(full_path, 'r') as f:
                    if f.read() != '':
                        raise FileExistsError("File is not Empty")
       
        remove(full_path)


    # def _exist_tb(self): ... 

    # def create_table(self, table_name: str): ...

    # def remove_table(self, table_name: str, force_remove: bool = False): ...


    




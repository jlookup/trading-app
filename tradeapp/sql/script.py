
import os

SQL_SCRIPT_DIR: str = 'sql/queries'
script_types: tuple(str) = ('.sql', '.txt')


def read(file_name: str, dir: str = SQL_SCRIPT_DIR) -> str:
    """
    Store your sql in .sql files, not in your app code.
    
    Reads a script file into a string variable 
    that can be executed by a db engine,
    for example, slqite3.executescript()

    Because this reads scripts into strings, 
    it does not allow for parameterization.
    It is only for fixed, raw queries.
    Vunerable to files with malicious code. 
    Do not use public-facing.
    """

    file_path = os.path.join(dir,file_name)

    if not file_name.lower().endswith(script_types):
        raise Exception
    if not os.path.exists(file_path):
        raise Exception

    try:
        with open(file_path, 'r') as script_file:
            script: str = script_file.read()
        return script
        
    except:
        raise Exception
    


def execute_file(db_connection, file_name: str, dir: str = SQL_SCRIPT_DIR) -> bool:
    """
    For SQLite3.
    Executes a .sql script file
    """
    try:
        script = read(file_name, dir)
        db_connection.executescript(script)
        result = True
    except:
        result = False
    
    return result
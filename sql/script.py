
import os

SQL_SCRIPT_DIR: str = 'sql/queries'


def read(file_name: str, dir: str = SQL_SCRIPT_DIR) -> str:
    """
    reads a script file 
    into a string variable 
    that can be executed by a db engine,
    for example, slqite3.executescript()

    Currently, does not allow for parameterization.
    Vunerable to SQL injection. do not use public-facing.
    """
    file_path = os.path.join(dir,file_name)
    
    with open(file_path, 'r') as script_file:
        script: str = script_file.read()

    return script
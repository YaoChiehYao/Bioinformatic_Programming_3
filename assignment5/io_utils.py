"""
Module Name: io_utils.py
This module stores file-handling-related functions
such as input/output and check if the file exists
or not
"""
import os
from typing import IO
from assignment5 import config


def get_filehandle(file: str, mode: str) -> IO:
    """
    filehandle : get_filehandle(infile, "r")
    Takes : 2 arguments fh_in name and mode i.e. what is needed to be done with
    this fh_in. This function opens the fh_in based on the mode passed in
    the argument and returns filehandle.
    @param file: The fh_in to open for the mode
    @param mode: They way to open the fh_in, e.g. reading, writing, etc
    @return: filehandle
    """
    try:
        fobj = open(file=file, mode=mode, encoding='utf-8')
        return fobj
    except OSError:
        config.get_error_string_4_opening_file_os_error(file=file, mode=mode)
        # raising like this allows the overall application to choose whether
        # to stop running gracefully or handle the exception.
        # you could have a function you implement like log_the_error(err), and then raise
        raise
    # test something like io_utils.get_filehandle("does_not_exist.txt", "rrr")
    except ValueError:
        config.get_error_string_4_value_error()
        raise
    except TypeError:  # test something like io_utils.get_filehandle([], "r")
        config.get_error_string_4_type_error()
        raise


def is_gene_file_valid(file_name):
    """Check if file_name is valid path
    Existed return True
    Not existed return False
    """

    return os.path.exists(file_name)

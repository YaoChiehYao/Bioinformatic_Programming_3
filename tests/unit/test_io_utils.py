"""Test suite for io_utils.py"""
import os
import sys
import pytest

from assignment5.io_utils import (
    get_filehandle, is_gene_file_valid)

from get_gene_level_information import (
    update_host_name, get_data_for_gene_file, _print_directories_for_hosts)


FILE_TO_TEST = "test.txt"

EXIST_PATH = './assignment5_data/Equus_caballus/ABI1.unigene'
NOT_EXIST_PATH = './assignment5/Equus_caballus/ABI1.unigene'


def test_existing_get_filehandle_for_reading():
    """Test get_filehandle for reading"""
    # does it open a file for reading
    # create a test file
    _create_file_for_testing(FILE_TO_TEST)
    # test
    test = get_filehandle(FILE_TO_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_TO_TEST)


def test_existing_get_filehandle_for_writing():
    """Test get_filehandle for writting"""
    # does it open a file for writing
    # test
    test = get_filehandle(file=FILE_TO_TEST, mode="w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_TO_TEST)


def test_get_filehandle_for_os_error():
    """Test get_filehandle for OSError"""
    # does it raise OSError
    # this should exit
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")


def test_get_filehandle_for_value_error():
    """Test get_filehandle for ValueError"""
    # does it raise ValueError
    # this should exit
    _create_file_for_testing(FILE_TO_TEST)
    with pytest.raises(ValueError):
        get_filehandle("does_not_exist.txt", "rrr")
    os.remove(FILE_TO_TEST)


def _create_file_for_testing(file):
    """Test creat_file_for_testing for writting"""
    # not actually run, the are just helper funnctions for the test script
    # create a test file
    open(file, "w", encoding="utf-8").close()


def test_is_gene_file_valid():
    """Test merge_dict_value for merging two dictionary"""
    # merge two dictionaries by the common keys, and append values into a list
    assert is_gene_file_valid(EXIST_PATH) == True
    assert is_gene_file_valid(NOT_EXIST_PATH) == False


def test_get_data_for_gene_file():
    """Retrieve the tissue data in a sorted list"""
    assert get_data_for_gene_file(EXIST_PATH) == ['adult', 'cartilage']


def test_update_host_name():
    """Test if hostname of cml is valid"""
    assert update_host_name('Homo_sapiens') == 'Homo_sapiens'
    assert update_host_name('Homo sapiens') == 'Homo_sapiens'
    assert update_host_name('human') == 'Homo_sapiens'

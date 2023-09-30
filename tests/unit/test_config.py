"""Test suite for config.py"""
import pytest
import os
from assignment5.config import (
    _DIRECTORY_FOR_UNIGENE, _FILE_ENDING_FOR_UNIGENE, get_directory_for_unigene, get_extension_for_unigene, get_keywords_for_hosts)


_INVALID_EXTENSION = "unigeme"
_VALID_EXTENSION = "unigene"


def test_get_directory_for_unigene():
    """Validate directory path """
    # valid scenario
    assert get_directory_for_unigene() == _DIRECTORY_FOR_UNIGENE
    # invalid scenario


def test_get_extension_for_unigene():
    """Validate entension"""
    assert get_extension_for_unigene() == _FILE_ENDING_FOR_UNIGENE


def test_get_keywords_for_hosts():
    """Test through scenarios"""
    # Entered name is capitalized common name ex. Homo sapiens
    assert get_keywords_for_hosts('Homo sapiens') == 'Homo_sapiens'
    # Entered name is common name ex. horse
    assert get_keywords_for_hosts('horse') == 'Equus_caballus'
    # Entered name is scientific name ex. Homo_sapiens
    assert get_keywords_for_hosts('Homo_sapiens') == 'Homo_sapiens'
    # Entered a misspelling name ex. horrse
    assert get_keywords_for_hosts('horrse') == "error"

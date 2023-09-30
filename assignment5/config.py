"""
Module Name: config.py
This module stores configuration data and data path
related functions and requires modification only
when data is moved or format updated
"""
_DIRECTORY_FOR_UNIGENE = "./assignment5_data"
_FILE_ENDING_FOR_UNIGENE = "unigene"


def get_directory_for_unigene():
    """Retrun the varaible of unigene"""
    # Add try and except
    return _DIRECTORY_FOR_UNIGENE


def get_extension_for_unigene():
    """Retrun file extension"""
    # Might consider .endwith to check extension
    return _FILE_ENDING_FOR_UNIGENE


def get_keywords_for_hosts(host_name):
    """Return the scientific name (_) in the dictionary"""
    bos_tarus = "Bos_taurus"
    equus_caballus = "Equus_caballus"
    homo_sapiens = "Homo_sapiens"
    ovis_aries = "Ovis_aries"
    mus_musculus = "Mus_musculus"
    rattus_norvegicus = "Rattus_norvegicus"
    host_keywords = {
        "bos taurus": bos_tarus,
        "cow": bos_tarus,
        "cows": bos_tarus,
        "homo sapiens": homo_sapiens,
        "human": homo_sapiens,
        "humans": homo_sapiens,
        "equus caballus": equus_caballus,
        "horse": equus_caballus,
        "horses": equus_caballus,
        "ovis aries": ovis_aries,
        "sheep": ovis_aries,
        "sheeps": ovis_aries,
        "mus musculus": mus_musculus,
        "mouse": mus_musculus,
        "mice": mus_musculus,
        "rattus norvegicus": rattus_norvegicus,
        "rat": rattus_norvegicus,
        "rats": rattus_norvegicus,
    }
    # Entered name is common name ex. rat
    if host_name in host_keywords.keys():
        return host_keywords[host_name]
    # Entered name is scientific name ex. Rattus_norvegicus
    elif host_name in host_keywords.values():
        return host_name
    # Entered name is capitalized common name ex. Rat
    elif host_name.lower() in host_keywords.keys():
        return host_keywords[host_name.lower()]
    else:
        return "error"


def get_error_string_4_value_error() -> None:  # error when used get_filehandle(fh_in, "1234")
    """
    Print the invalid argument message for ValueError
    """
    print("Invalid argument Value for opening a fh_in for reading/writing")


def get_error_string_4_type_error() -> None:  # error when used get_filehandle(fh_in, "r", "w")
    """
    Print the invalid argument message for TypeError
    """
    print("Invalid argument Type passed in:")


def get_error_string_4_opening_file_os_error(file: str, mode: str) -> None:
    """
    Print the invalid argument message for OSError
    @param file: The fh_in name
    @param mode: The mode to open the fh_in
    """
    print(f"Could not open the fh_in (os error): {file} with mode {mode}")

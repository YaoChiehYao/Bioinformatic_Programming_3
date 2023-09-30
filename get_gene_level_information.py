"""
Program Name: get_gene_level_information.py
This program takes two command line arguments. The first
is a hostname, and the second is a gene name, combining
those as part of the directory and file path to get the
target file. Then use that path to access and retrieve
and parse data. Ultimately, it returns the gene expression
information on the command line interface.
"""
import sys
import os
import re
import argparse
from assignment5 import config
from assignment5 import io_utils


def get_cli_args() -> argparse.Namespace:
    """
    argparse : get_cli_args()
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(
        description='Give the Host and Gene name')

    parser.add_argument('--host', metavar='HOST',
                        type=str, help='Name of Host', required=False,
                        default='human')
    parser.add_argument('-g', '--gene', metavar='GENE',
                        type=str, help='Name of Gene', required=False,
                        default='TGM1')
    return parser.parse_args()


def update_host_name(host_name):
    """Search if the input is a common or a scientific name or invalid"""
    if config.get_keywords_for_hosts(host_name) != "error":
        return config.get_keywords_for_hosts(host_name)
    _print_directories_for_hosts()
    sys.exit()


def _print_directories_for_hosts():
    """Print helper information for invalid hostname"""
    print(
        """
    Either the Host Name you are searching for is not in the database

    or If you are trying to use the scientific name please put the name in double quotes:

    "Scientific name"

    Here is a (non-case sensitive) list of available Hosts by scientific name

    1. Bos_taurus
    2. Equus_caballus
    3. Homo_sapiens
    4. Mus_musculus
    5. Ovis_aries
    6. Rattus_norvegicus


    Here is a (non-case sensitive) list of available Hosts by common name

    1. Bos taurus
    2. Cow
    3. Cows
    4. Equus caballus
    5. Homo sapiens
    6. Horse
    7. Horses
    8. Human
    9. Humans
    10. Mice
    11. Mouse
    12. Mus musculus
    13. Ovis aries
    14. Rat
    15. Rats
    16. Rattus norvegicus
    17. Sheep
    18. Sheeps
    """, file=sys.stderr)


def get_data_for_gene_file(gene_file_name):
    """Get gene expression data from the file path"""
    in_file = io_utils.get_filehandle(gene_file_name, "r")
    # use regular expression to get the tissue datas
    match = re.search(r"(.+\|[\s|\S].+)", in_file.read())
    # parsing tissue data and store in a list
    if match is not None:  # matched
        tissue_strig = match.group(1)  # match here is an object. group1
        tissue_list = []
        for tissue in tissue_strig.split("|"):
            tissue_list.append(tissue.replace("EXPRESS", "").strip())
        return sorted(tissue_list)
    return "no match found"


def print_host_to_gene_name_output(host_name, gene_name, tissue_list):
    """Print the header and querying result"""
    # Convert directory name to scientific name
    scientific_name = update_host_name(host_name).replace("_", " ")
    # Print header
    print(f"In {scientific_name}, There are {len(tissue_list)} \
tissues that {gene_name} is expressed in:\n")
    # Print the querying result
    for index, tissue in enumerate(tissue_list):
        num = index+1
        letter = tissue.capitalize()
        peroid = "."
        print(f"{num : >4}{peroid : <2}{letter}")


def main():
    """Main business logic"""
    args = get_cli_args()
    # Get directory and extension from config module (not often change required)
    file = os.path.join(config.get_directory_for_unigene(), update_host_name(args.host), args.gene
                        + "." + config.get_extension_for_unigene())
    # check for the existence of file
    if io_utils.is_gene_file_valid(file):
        # using f-strings
        print(f"\nFound Gene {args.gene} for {args.host}")
    else:
        print("Not found")
        print(
            f"Gene {args.gene} does not exist for {args.host}. exiting now...", file=sys.stderr)
        sys.exit(1)
    print_host_to_gene_name_output(
        args.host, args.gene, get_data_for_gene_file(file))


if __name__ == "__main__":
    main()

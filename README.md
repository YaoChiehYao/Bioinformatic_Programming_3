#  Assignment 5

## Description

Program Name: ***get_gene_level_information.py***
This program takes two command line arguments. The first  
is a hostname, and the second is a gene name, combining 
those as part of the directory and file path to get the 
target file. Then use that path to access and retrieve 
and parse data. Ultimately, it returns the gene expression 
information on the command line interface.


## Getting Started

* Hi, this is the documentation for assignment 5 of the bio programming course.
* This project demos students' capability to handle slightly larger and quantitative files, access and retrieve data for informational purposes, unit testing, and structure the functions into config and utils, which have separate tests. Like the previous assignment, this program requires using generic python code with a command line interface. Therefore, this project might be something for your reference if you are interested in programming skills.

### Dependencies

* Python version 3.8.10 and compatible modules (if needed) 

### Installing

* The file can download from the Canvas
* Python3 and Python IDE is required
* Required only use argparse,re,os,and sys modules

### Executing program

* Use python IDE to open the file
* Run the python file by command line
* Follow exceptions if there is any error from command line input 
* Execute the programs by the following commands 


***  get_gene_level_information.py ***
Please refer to the successful output examples as follows: 

>>> python3 get_gene_level_information.py
```
Found Gene TGM1 for Homo sapiens
In Homo sapiens, There are 41 tissues that TGM1 is expressed in:

  1. Adipose tissue
  2. Adult
  3. Bladder
  4. Bladder carcinoma
  5. Brain
  6. Breast (mammary gland) tumor
  7. Cervical tumor
  8. Cervix
  9. Colorectal tumor
 10. Embryoid body
 11. Embryonic tissue
 12. Esophageal tumor
 13. Esophagus
 14. Eye
 15. Fetus
 16. Germ cell tumor
 17. Head and neck tumor
 18. Intestine
 19. Kidney
 20. Kidney tumor
 21. Larynx
 22. Lung
 23. Mammary gland
 24. Mouth
 25. Muscle
 26. Neonate
 27. Non-neoplasia
 28. Normal
 29. Ovarian tumor
 30. Ovary
 31. Pancreas
 32. Pancreatic tumor
 33. Pharynx
 34. Placenta
 35. Skin
 36. Skin tumor
 37. Thymus
 38. Trachea
 39. Umbilical cord
 40. Uterine tumor
 41. Uterus
```


>>> python3 get_gene_level_information.py --host horse --gene API5
```
Found Gene API5 for Equus caballus
In Equus caballus, There are 3 tissues that API5 is expressed in:

  1. Adult
  2. Blood
  3. Cartilage
```


>>> python3 get_gene_level_information.py --host "Homo sapiens" --gene AATK 
```
Found Gene AATK for Homo sapiens
In Homo sapiens, There are 31 tissues that AATK is expressed in:

  1. Adrenal gland
  2. Adult
  3. Ascites
  4. Blood
  5. Brain
  6. Breast (mammary gland) tumor
  7. Cervical tumor
  8. Cervix
  9. Connective tissue
 10. Ear
 11. Eye
 12. Fetus
 13. Gastrointestinal tumor
 14. Glioma
 15. Intestine
 16. Juvenile
 17. Kidney
 18. Kidney tumor
 19. Leukemia
 20. Mammary gland
 21. Muscle
 22. Nerve
 23. Non-neoplasia
 24. Normal
 25. Pancreas
 26. Pancreatic tumor
 27. Parathyroid
 28. Prostate
 29. Skin
 30. Skin tumor
 31. Soft tissue/muscle tissue tumor 
```


>>> python3 get_gene_level_information.py --host Homo_sapiens --gene EXD1
```
Found Gene EXD1 for Homo sapiens
In Homo sapiens, There are 5 tissues that EXD1 is expressed in:

  1. Adult
  2. Brain
  3. Muscle
  4. Normal
  5. Testis
```


## Help

Any issue contact with yao.yao-@northeastern.edu

## Authors

Yao Chieh Yao
Northeastern University Bioinformatics

## Version History

* 1.0
    * Assignment01 Finish 
* 0.1
    * Assignment01 Release 

## License

This project is an assignment work and only license to TA and professors of Northeastern University Bioinformatics 

## Acknowledgments



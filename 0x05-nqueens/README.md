0x05. N Queens
Algorithm
Python
 Weight: 1


Requirements:

    - Allowed editors: vi, vim, emacs
    - All my files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
    - The first line of all my files should be exactly #!/usr/bin/python3
    - My code should use the PEP 8 style (version 1.7.*)
    - All my files must be executable



Argument Parsing and Validation:

1. Check the number of arguments: The program should accept exactly one argument (N) from the command line. If not, print the usage message and exit with status 1.
2. Check if N is a number: Use a try-except block to handle cases where the argument is not an integer. If it’s not, print the error message and exit with status 1.
3. Check if N is at least 4: Since the N queens problem is only solvable for N >= 4, ensure that N is greater than or equal to 4. If not, print the error message and exit with status 1.
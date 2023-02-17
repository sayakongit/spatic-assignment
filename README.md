# Spatic Assignment
==============================

This document will help you to setup the environment to execute the script.


## Table of Contents
- [Project Organization](#project-organization)
- [Getting Started](#getting-started)

## Project Organization
------------
    |
    ├── README.md          <- The top-level README for using/validating this project.
    │
    ├── app.py       <- Main python file containing the script.
    │
    └── requirements.txt   <- The requirements file for reproducing the analysis environment.
    |
    └── data.csv   <- The input dataset provided in the assignment.
    |
    └── output.csv   <- The output csv file.


## Getting Started
------------

### On your Windows machine
1. To get this repository, run the following command inside your git enabled terminal

```bash
$ git clone https://github.com/sayakongit/spatic-assignment.git
```

2. Change the name of folder that contains this whole repo: `spatic-assignment` -> `{your project name}` and navigate to that folder.

3. Install Python version 3.11.1

4. Install virtual environment by running 

```
pip install virtualenv
```

5. Create a virtual environment named `spatic` by running,

```
virtualenv spatic
```

6. Activate the environment by running the following on Windows PowerShell.
```
.\spatic\Scripts\activate.ps1 
```
on Windows PowerShell.
(If you get `UnauthorizedAccess` error, enter this command `Set-ExecutionPolicy Unrestricted -Scope Process` followed by `Y` before activating the environment.)

7. Install the package's dependencies in `requirements.txt` with pip by running 

```
pip install -r requirements.txt
```

8. To execute the script and get the CSV file, run the .py file using the following command [NOTE: Don't have the output CSV file open while running the script]
```
python app.py
```


10. Deactivate the virtual environment by running 
```
deactivate
```

    
--------

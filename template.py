import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "cnn_model"

list_of_files = [ #Just add a name to create a file,  like: "subdir/filename.py"
    ".github/workflows/.gitkeep", # .gitkeep, just to keep something inside the folder, so that it can be pushed to github
    f"src/{project_name}/__init__.py", # __init__.py, to make the folder a package- local constr file
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb", # Research before implementation of the model, to keep track of the experiments
    "templates/index.html"
    
]



for filepath in list_of_files:
    filepath = Path(filepath) # As we are using pathlib, we need to convert the string path to a Path object -> Windows uses \ and Linux uses /, so to avoid this issue, we use pathlib
    filedir, filename = os.path.split(filepath) # Split the path into directory and filename
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # Create the directory if it doesn't exist, exist_ok=True means it won't raise an error if the directory already exists
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # Check if the file doesn't exist or is empty
        with open(filepath, "w") as f: # Open the file in write mode
            pass # Create an empty file, just to keep the structure of the project
        logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{filename} already exists and is not empty, skipping file creation.")
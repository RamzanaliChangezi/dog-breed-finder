# notebook_processor.py

import os
import nbformat
import zipfile

def unzip_dataset(zip_path, extract_to):
    """
    Function to unzip a dataset.
    
    Parameters:
    - zip_path: str, the path to the zip file.
    - extract_to: str, the directory to extract the files to.
    """
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Extracted {zip_path} to {extract_to}")
    else:
        print(f"File {zip_path} not found")

def check_gpu():
    try:
        result = os.popen('nvidia-smi').read()
        return result
    except Exception as e:
        return str(e)

def process_notebook(file_path):
    """
    Function to process the notebook. It reads and executes the cells.
    
    Parameters:
    - file_path: str, the path to the notebook file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        notebook_content = nbformat.read(file, as_version=4)
    
    for cell in notebook_content.cells:
        if cell.cell_type == 'code':
            try:
                exec(cell.source)
            except ModuleNotFoundError as e:
                print(f"ModuleNotFoundError: {e}")
            except Exception as e:
                print(f"Error executing cell: {e}")
    
    return notebook_content

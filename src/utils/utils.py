import os
import json
import PyPDF2
import docx2txt


def read_pdf(file_path):
    """
    Reads a PDF file and extracts text from it.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF file.
    """
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        return ' '.join(page.extract_text() for page in reader.pages)


def read_docx(file_path):
    """
    Reads a DOCX file and extracts text from it.

    Args:
        file_path (str): The path to the DOCX file.

    Returns:
        str: The extracted text from the DOCX file.
    """
    return docx2txt.process(file_path)


def read_file(file_path):
    """
    Reads a file and extracts text based on its format.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The extracted text from the file.

    Raises:
        ValueError: If the file format is unsupported.
    """
    try:
        if file_path.endswith('.pdf'):
            return read_pdf(file_path)
        elif file_path.endswith('.docx'):
            return read_docx(file_path)
        else:
            raise ValueError('Unsupported file format')
    except Exception as e:
        print(f'Error reading file: {str(e)}')


def set_key(configfile: str, var: str):
    """
    Sets an environment variable from a configuration file.

    Args:
        configfile (str): The path to the configuration file.
        var (str): The name of the environment variable to set.

    Raises:
        ValueError: If the variable is not found in the configuration file.
    """
    with open(configfile, 'r') as file:
        config = json.load(file)

    if not os.environ.get(var):
        api_key = config.get(var)
        if api_key:
            os.environ[var] = api_key
        else:
            raise ValueError(f'{var} not found in {configfile}')


def StateToDict(state, output):
    """
    Converts a state object to a dictionary.

    Args:
        state: The state object.
        output: The output object.

    Returns:
        dict: A dictionary representation of the state object.
    """
    result = {}
    keys = state.model_fields.keys()
    for key in keys:
        result[key] = getattr(output, key, None)
    return result

def load_config(file):
    with open(file, 'r') as f:
        return json.load(f)
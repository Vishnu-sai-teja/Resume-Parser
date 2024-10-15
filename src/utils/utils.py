import os
import json
import PyPDF2
import docx2txt

def read_pdf(file_path):
    with open(file_path, 'rb') as file:    
        reader = PyPDF2.PdfReader(file)
        return ' '.join(page.extract_text() for page in reader.pages)

def read_docx(file_path):
    return docx2txt.process(file_path)

def read_file(file_path):
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
    with open(configfile, 'r') as file:
        config = json.load(file)

    if not os.environ.get(var):
        api_key = config.get(var)
        if api_key:
            os.environ[var] = api_key
        else:
            raise ValueError(f'{var} not found in {configfile}')

def StateToDict(state, output):
    dict = {}
    # Get all the keys in each of the state
    keys = state.model_fields.keys()
    for key in keys:
        dict[key] = getattr(output, key, None)
    return dict

def load_config(configfile: str):
    with open(configfile, 'r') as file:
        return json.load(file)
    
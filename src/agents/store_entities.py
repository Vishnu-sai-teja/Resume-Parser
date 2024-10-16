import json
import os
from .state import ResumeState
from utils.utils import set_key, load_config, StateToDict
from utils.validators import validate_entities
from langchain_google_genai import ChatGoogleGenerativeAI


def store_entities(state: ResumeState):
    """
    Stores the extracted entities from the resume text into a JSON file.

    Args:
        state (ResumeState): A dictionary containing the extracted entities and other state information.

    Returns:
        dict: A dictionary indicating the current stage of processing.
    """
    set_key('./config.json', 'GOOGLE_API_KEY')
    config = load_config('./config.json')
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

    output_file_path = config.get('output_file_path')
    if output_file_path:
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        with open(output_file_path, 'w') as output_file:
            json.dump(state['extracted_entities'], output_file, indent=4)
        
        return {"current_stage": "END"}
    else:
        raise ValueError("Output file path not found in the configuration.")
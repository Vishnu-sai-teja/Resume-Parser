import json
from .state import ResumeState
from utils.utils import set_key, load_config, StateToDict
from utils.validators import validate_entities
from langchain_google_genai import ChatGoogleGenerativeAI
import os

def store_entities(state: ResumeState):
    set_key('./config.json', 'GOOGLE_API_KEY')
    config = load_config('./config.json')
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", temperature=0)

    output_file_path = config.get('output_file_path')
    if output_file_path:
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        with open(output_file_path, 'w') as output_file:
            json.dump(state['extracted_entities'], output_file, indent=4)
        
        return {"current_stage": "END"}
    else:
        raise ValueError("Output file path not found in the configuration.")
    

extracted_entities = {'name': 'Vishnu Sai Teja Nagabandi', 
                      'phone': '+918978044062', 
                      'email': 'vishnusaiteja.3004@gmail.com', 
                      'education': [{'institution': 'IIIT NAGPUR', 'degree': 'B Tech Computer Science', 'major': 'Computer Science', 'duration': 'Expected 2025', 'location': 'Nagpur, Maharashtra'},
                                    {'institution': 'SRI CHAITHANYA', 'degree': 'Senior Secondary Education', 'major': 'Overall Percentage: 98.2%', 'duration': 'Graduated 2021', 'location': 'Hyderabad, Telangana'}], 
                      'experience': [{'company': 'AIDASH', 'role': 'Data Science Intern', 'work_done': '* Implemented end-to-end asset geotagging pipeline using street view imagery, optimizing object detection, depth and height estimation.\\n    * Designed and implemented asynchronous processing and parallelization, significantly boosting pipeline efficiency and maximizing hardware resource utilization.\\n    * Fine-tuned detection models for specific assets, achieving faster processing times and improved accuracy in geolocating assets.', 'duration': 'April 2024 - Present'}, 
                                     {'company': 'VLIPPR', 'role': 'ML and Data Science Intern', 'work_done': '* Contributed to Vaanee, an audio model specializing in Indian languages.\\n    * Led efforts in the preprocessing of intricate audio data.\\n    * Proposed and implemented techniques for audio pre and post processing to enhance the accuracy of audio transcription.', 'duration': 'Nov 2023 - Feb 2024'}], 
                      'skills': 'Programming Languages\\n\\n* C++\\n* Python\\n* Java\\n* Basic Shell\\n* Basic Rust\\n* CSS\\n* JS\\n\\nFrameworks\\n\\n* LangChain\\n* PyTorch\\n* Basic Django\\n* MySQL\\n* Basic PHP\\n\\nLibraries\\n\\n* Numpy\\n* Pandas\\n* Matplotlib\\n* Sci-kit Learn\\n* nltk\\n* Basic fastai\\n\\nLANGUAGES\\n\\nProficient\\n\\n* English\\n* Hindi\\n* Telugu\\n\\nNovice\\n\\n* German', 
                      'certifications': ''}

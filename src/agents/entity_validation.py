from .state import ResumeState
from utils.utils import set_key
from utils.validators import validate_entities
from langchain_google_genai import ChatGoogleGenerativeAI


def entity_validation(state: ResumeState):
    set_key('./config.json', 'GOOGLE_API_KEY')
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", temperature=0)

    extracted_entities = state['extracted_entities']
    formatted_entities = {
        'name': extracted_entities['name'],
        'email': extracted_entities['email'],
        'phone': extracted_entities['phone'],
        'education': extracted_entities['education'],
        'experience': extracted_entities['experience'],
        'skills': extracted_entities['skills'],
        'certifications': extracted_entities['certifications']
    }

    validation_results = validate_entities(formatted_entities)
    print("\n\n", validation_results, "\n\n")
    # Remove the empty validation list
    validation_results = {k: v for k, v in validation_results.items() if v}
    
    return {"resume_text": state['resume_text'],
            "extracted_entities": state['extracted_entities'],
            "validated_entities": validation_results,
            "current_stage": "_END_"}
            

# extracted_data = {
#     'name': 'Vishnu Sai Teja Nagabandi',
#     'phone': '+91  8978044062',
#     'email': 'vishnusaiteja.3004@gmail.com',
#     'education': [{'institution': 'IIIT NAGPUR', 'degree': 'B Tech Computer Science', 'major': 'Computer Science', 'duration': 'Expected 2025', 'location': 'Nagpur, Maharashtra'}],
#     'experience': [{'company': 'AIDASH', 'role': 'Data Science Intern', 'work_done': '* Implemented end-to-end asset geotagging pipeline using street view imagery, optimizing object detection, depth and height estimation.\n    * Designed and implemented asynchronous processing and parallelization, significantly boosting pipeline efficiency and maximizing hardware resource utilization.\n    * Fine-tuned detection models for specific assets, achieving faster processing times and improved accuracy in geolocating assets.', 'duration': 'April 2024 - Present'}],
#     'skills': 'Programming Languages\n\n* C++\n* Python\n* Java\n* Basic Shell\n* Basic Rust\n* CSS\n* JS\n\nFrameworks\n\n* LangChain\n* PyTorch\n* Basic Django\n* MySQL\n* Basic PHP\n\nLibraries\n\n* Numpy\n* Pandas\n* Matplotlib\n* Sci-kit Learn\n* nltk\n* Basic fastai',
#     'certifications': ''
# }

# print(entity_validation({"extracted_entities" : extracted_data}))


    

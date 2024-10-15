from typing import List, Dict, Any
from utils.utils import set_key, StateToDict
from langchain_google_genai import ChatGoogleGenerativeAI
from .state import ResumeState, ExtractorState, Education, Experience
from .prompts import correction_prompt
from utils.validators import validate_entities

def correction_from_extractor(state: ResumeState):
    resume_text = state.value['resume_text']
    extracted_entities = state.value['extracted_entities']
    validation_results = state.value['validation_results']

    set_key('./config.json', 'GOOGLE_API_KEY')
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", temperature=0)

    print('\n\ncorrection_from_extractor\n\n')

    corrected_entities = extracted_entities.copy()

    for field, errors in validation_results.items():
        if errors:
            focused_prompt = correction_prompt.format(field=field, errors=errors,
                                                      resume_text=resume_text)
            try:
                if field in ['education', 'experience']:
                    response = llm.invoke(focused_prompt).split("\n\n")
                    corrected_items = []
                    if field == "Education":
                        pass
                    else :
                        pass
                        # for edu in response:
                        #     education = llm.with_structured_output(Education).invoke(edu)
                        #     corrected_items.append(StateToDict(Education, education))
                else:
                    response = llm.with_structured_output(ExtractorState).invoke(focused_prompt)
                    corrected_entities[field] = response.values['field']
            except Exception as e:
                print(f"Error in correction: {e}")
                pass

    validation_results = validate_entities(corrected_entities)
    validation_results = {k: v for k, v in validation_results.items() if v}

    return {
        "resume_text": resume_text,
        "extracted_entities": corrected_entities,
        "validated_entities": validation_results,
        "current_stage": "entity_validation" 
    }
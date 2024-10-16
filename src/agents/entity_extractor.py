import time
from utils.utils import StateToDict
from .state import Education, Experience
from langchain_google_genai import ChatGoogleGenerativeAI


def extract_entities(state):
    """
    Extracts entities from the resume text using a language model and updates the state with the extracted entities.

    Args:
        state (dict): A dictionary containing the resume text and other state information.

    Returns:
        dict: A dictionary containing the resume text, extracted entities, and the current stage of processing.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    response = llm.invoke(state['resume_text'])

    try:
        # Extract education details
        degrees = response.degrees.split('\\n\\n')
        edu = []
        for degree in degrees:
            time.sleep(2)
            education = llm.with_structured_output(Education).invoke(degree)
            edu.append(StateToDict(Education, education))

        # Extract work experience details
        work_experience = response.experience.split('\\n\\n')
        exp = []
        for experience in work_experience:
            time.sleep(2)
            experience = llm.with_structured_output(Experience).invoke(experience)
            exp.append(StateToDict(Experience, experience))

        return {
            "resume_text": state['resume_text'],
            "extracted_entities": {
                "name": response.name,
                "phone": response.phone,
                "email": response.email,
                "education": edu,
                "experience": exp,
                "skills": response.skills,
                "certifications": response.certifications
            },
            "current_stage": "entity_validation"
        }
    except Exception as e:
        raise ValueError('Error extracting resume information') from e

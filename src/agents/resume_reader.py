import os
from utils.utils import read_file, set_key
from .state import ResumeState
from langchain_google_genai import ChatGoogleGenerativeAI


def resume_reader(state: ResumeState):
    """
    Read the resume file and process the text using the language model ,for further processing

    Args:
        state (ResumeState): A langgraph state containing the file path of the resume and other state information.

    Returns:
        dict: A state containing the processed resume text and the current stage of processing.
    """
    set_key('./config.json', 'GOOGLE_API_KEY')
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

    resume_path = state['file_path']
    try:
        prompt = (
            "format the resume , Here is the resume: {resume}"
            "Note : Do not remove any details from the resume or add any details to the text"
        )
        if not resume_path:
            raise ValueError('No resume file path provided')
        resume_text = read_file(resume_path)
        response = llm.invoke(prompt.format(resume=resume_text))
        return {
            "resume_text": response.content,
            "current_stage": "entity_extraction"
        }
    except Exception as e:
        raise ValueError('Error reading resume file') from e
    

# if __name__ == "__main__":
#     ResumeState = {
#         'file_path': '/Users/vishnusaitejanagabandi/Desktop/PIBIT Parser 2/src/data/VishnuSaiTeja_2025CV.pdf',
#         'resume_text': None
#     }

#     # Call the resume reader function
#     resume_reader(ResumeState)

#     # Print the processed resume text
#     print("Processed Resume Text: ")
#     print(ResumeState['resume_text'])


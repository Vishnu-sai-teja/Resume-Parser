import os
from utils.utils import read_file, set_key
from .state import ResumeState
from langchain_google_genai import ChatGoogleGenerativeAI

def resume_reader(state: ResumeState):

    set_key('./config.json', 'GOOGLE_API_KEY')
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", temperature=0)

    resume_path = state['file_path']
    try:
        prompt = "Do not loose any information from the resume, format the resume details and filter out any stopwords \n\n Here is the resume : {resume}"
        if not resume_path:
            raise ValueError('No resume file path provided')
        resume_text = read_file(resume_path)
        response = llm.invoke(prompt.format(resume=resume_text))
        # print(response.content)
        return {"resume_text" : response.content,
                "current_stage": "entity_extraction"}
    except:
        raise ValueError('Error reading resume file')
    

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


from state import ResumeState, Education, Experience
from utils.utils import set_key
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI

# In development

def tempState(BaseModel):
    val : str

def phone_corrector(errors, llm, resume_text):
    prompt = ("Extract the phone number in the traditional format(country code + mobile numer) from the resume text : {resume_text}"
              "Here are the errors in the phone number : {errors}"
              "Note : Do not remove any details from the resume or add any details to the text"
              "Feel free to return a empty string if the phone number is not present in the resume")

    prompt = prompt.format(resume=resume_text, errors=errors)
    new_mobile_nuber = llm.with_structured_output(tempState).invoke(prompt)

    return new_mobile_nuber.val

def email_corrector(errors, llm, resume_text):
    prompt = ("Extract the email address from the resume text : {resume_text}"
              "Here are the errors in the email address : {errors}"
              "Note : Do not remove any details from the resume or add any details to the text"
              "Feel free to return a empty string if the email address is not present in the resume")

    prompt = prompt.format(resume=resume_text, errors=errors)
    new_email = llm.with_structured_output(tempState).invoke(prompt)

    return new_email.val

def name_corrector(errors, llm, resume_text):
    prompt = ("Extract the name from the resume text : {resume_text}"
              "Here are the errors in the name : {errors}"
              "Identify those values of states that doesnt comply with the state, and remove them"
              "Note : Do not remove any details from the resume or add any details to the text"
              "Feel free to return a empty string if the name is not present in the resume")

    prompt = prompt.format(resume=resume_text, errors=errors)
    new_name = llm.with_structured_output(Education).invoke(prompt)

    return new_name.val

def education_corrector(errors, llm, resume_text):
    prompt = ("Extract the education details from the resume text : {resume_text}"
              "Here are the errors in the education details : {errors}"
              "Note : Do not remove any details from the resume or add any details to the text"
              "Feel free to return a empty string if the education details are not present in the resume")

    prompt = prompt.format(resume=resume_text, errors=errors)
    new_education = llm.with_structured_output(Education).invoke(prompt)

    # return

def skill_corrector(errors, llm, resume_text):
    prompt = ("Extract the skills from the resume text : {resume_text}"
              "Here are the errors in the skills : {errors}"
              "Return all the skills as  a comma separated string"
              "Note : Do not remove any details from the resume or add any details to the text"
              "Feel free to return a empty string if the skills are not present in the resume")
    
    prompt = prompt.format(resume=resume_text, errors=errors)
    new_skills = llm.with_structured_output(tempState).invoke(prompt)

    return new_skills.val

def certifications_corrector(errors, llm, resume_text):
    prompt = ("Extract the certifications from the resume text : {resume_text}"
                "Here are the errors in the certifications : {errors}"
                "Return all the certifications as a comma separated string"
                "Note : Do not remove any details from the resume or add any details to the text"
                "Feel free to return a empty string if the certifications are not present in the resume"
    )

    prompt = prompt.format(resume=resume_text, errors=errors)
    new_certifications = llm.with_structured_output(tempState).invoke(prompt)
    return 



def entity_corrector(state: ResumeState):

    resume_text = state.value['resume_text']
    entities = state.value['extracted_entities']
    validated_entities = state.value['validated_entities']

    set_key('./config.json', 'GOOGLE_API_KEY')
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", temperature=0)

    # Lets divide the categories well
    if len(validated_entities['phone']) != 0 :
        phone_corrector(validated_entities['phone'], llm, resume_text)

    for key, value in validated_entities.items():
        if len(value) != 0:
            entities[key] = globals()[f"{key}_corrector"](value, llm, resume_text)

    return {
        "resume_text": resume_text,
        "extracted_entities": entities,
        "current_stage": "entity_validation",
        "validated_entities": {}
    }


if __name__ == "__main__":

    
    


# state = ResumeState({
#         'resume_text': 'Sample resume text 9440644063',
#         'extracted_entities': {
#             'name' : 'Vishnu',
#             'email' : 'visate.nags@@@gmail.com',
#             'phone': '1234565789022323',
#             'education': [{
#                 'institution': '',
#                 'degree': 'B.Tech',
#                 'major': 'Computer Science', 
#                 'duration': '2021-2025', 
#                 'location': 'Nagpur'
#             }],
#             'experience': [{
#                 'company': '', 
#                 'role': 'Data Science Intern', 
#                 'work_done': 'Implemented geotagging pipeline ', 
#                 'duration': 'April 2024'
#             }],
#             'skills': 'Python, Java, C++',
#             'certifications': 'AWS Certified Developer'
#         },
#         "validated_entitites":{
#             'phone' : ["The format of the phone number is incorrect"]
#         },
#         'current_stage': 'entity_validation'
#     })
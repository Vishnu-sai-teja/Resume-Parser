import operator
from typing import TypedDict, Dict, List, Any, Annotated
from pydantic import BaseModel


class ResumeState(TypedDict):
    """
    State of the graph workflow
    """
    file_path : str
    resume_text: str
    extracted_entities: Dict[str, Any]
    validated_entities: Dict[str, Any]
    current_stage: str
    feedback: Dict[str, str]
    errors: List[str]
    interrupt: bool

class Education(BaseModel):
    institution: str
    degree: str
    major: str
    duration: str
    location: str

class Experience(BaseModel):
    company: str
    role: str
    work_done: str
    duration: str

class ExperienceSubState(BaseModel):
    experiences :  List[str]

# class ExtractorState(BaseModel):
#     name : str
#     email : str
#     phone : str
#     # education : dict[str, str]
#     # experience : dict[str, str]
#     # skills : dict[str, str]
#     # certifications : dict[str, str]
#     education : str
#     # experience : List[Experience]
#     # experience: List[Experience] = Field(default_factory=list)
#     experience : str
#     skills : str
#     certifications : str

class ExtractorState(BaseModel):
    name: str = ""
    email: str = ""
    phone: str = ""
    education: str = ""
    experience: str = ""
    skills: str = ""
    certifications: str = ""
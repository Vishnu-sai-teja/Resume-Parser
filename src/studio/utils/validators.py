import re
from typing import List, Dict, Any

def validate_name(name: str) -> List[str]:
    errors = []
    if name:
        if len(name.split()) < 2:
            errors.append("Name should include both first and last name")
    return errors

def validate_email(email: str) -> List[str]:
    errors = []
    if email:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Invalid email format")
    return errors

# def validate_phone(phone: str) -> List[str]:
#     errors = []
#     if not phone:
#         errors.append("Phone number is missing")
#     elif phone.startswith('+'):
#         if not re.match(r'^\+\d{1,3} \d{10}$', phone):
#             errors.append("Invalid phone number format with country code")
#     elif not re.match(r'^\d{10}$', phone):
#         errors.append("Invalid phone number format without country code")
    
#     return errors

# def validate_phone(phone: str) -> List[str]:
#     errors = []
#     if phone:  # Only validate if phone is provided
#         if not re.match(r'^\+?\d{1,3}? ?\d{10}$|^\d{10}$', phone):
#             errors.append("Invalid phone number format")
#     return errors

import re

def validate_phone(phone: str) -> List[str]:
    errors = []
    if phone:
        phone = phone.replace(" ", "")
        if not re.match(r'^(\+\d{1,3})?[6-9]\d{9}$', phone):
            errors.append("Invalid phone number format")
    return errors

def validate_education(education: List[Dict[str, str]]) -> List[str]:
    errors = []
    if education:  # Only validate if education is provided
        for edu in education:
            if 'institution' not in edu or not edu['institution']:
                errors.append("Institution is missing in education")
            if 'degree' not in edu or not edu['degree']:
                errors.append("Degree is missing in education")
            if 'duration' not in edu or not edu['duration']:
                errors.append("Graduation date is missing in education")
    return errors

def validate_skills(skills: str) -> List[str]:
    errors = []
    if skills:  # Only validate if skills are provided
        if not skills.strip():
            errors.append("Skills cannot be empty")
    return errors

def validate_certifications(certifications: str) -> List[str]:
    errors = []
    if certifications:  # Only validate if certifications are provided
        if not certifications.strip():
            errors.append("Certifications cannot be empty")
    return errors

from typing import List, Dict
from datetime import datetime

def validate_experience(experience: List[Dict[str, str]]) -> List[str]:
    errors = []

    if not experience:
        return ["Work experience information is missing"]

    for exp in experience:
        company = exp.get('company')
        role = exp.get('role')
        duration = exp.get('duration')

        if not company:
            errors.append("Company name is missing in experience")
        if not role:
            errors.append("Job title is missing in experience")
        if not duration:
            errors.append("Employment duration is missing in experience")

        # Date validation of the employment duration
        # elif ' - ' in duration:
        #     start_date_str, end_date_str = duration.split(' - ')
        #     if end_date_str.lower() != 'present':
        #         start_date = datetime.strptime(start_date_str, "%B %Y")
        #         end_date = datetime.strptime(end_date_str, "%B %Y")
        #         if start_date > end_date:
        #             errors.append(f"Invalid date range in experience: {duration}")
        # else:
        #     errors.append(f"Invalid duration format: {duration}")

    return errors


# Merge all the validations 
def validate_entities(extracted_entities: Dict[str, Any]) -> Dict[str, List[str]]:
    validation_results = {}
    print(validate_email(extracted_entities.get('email', '')))
    print(validate_phone(extracted_entities.get('phone', '')))

    validation_results['name'] = validate_name(extracted_entities.get('name', ''))
    validation_results['email'] = validate_email(extracted_entities.get('email', ''))
    validation_results['phone'] = validate_phone(extracted_entities.get('phone', ''))
    validation_results['education'] = validate_education(extracted_entities.get('education', []))
    validation_results['experience'] = validate_experience(extracted_entities.get('experience', []))
    validation_results['skills'] = validate_skills(extracted_entities.get('skills', ''))
    validation_results['certifications'] = validate_certifications(extracted_entities.get('certifications', ''))

    print(validate_entities)

    return validation_results


# Example calls to test the validation
# print(validate_phone("9440644068"))          # Should return []
# print(validate_phone("+91 9440644068"))      # Should return []
# print(validate_phone("+919440644068"))        # Should return []

# extracted_entities=  {'name': 'AKASH GOEL',
#                         'phone': '93106312446',
#                         'email': 'akashg2494gmail.com', 
#                         'education': [
#                             {
#                                 'institution': 'Delhi Institute of Advanced Studies of IP University', 
#                                 'degree': 'Master of Business Administration', 
#                                 'major': 'Finance and Marketing',
#                                 'duration': '2014-2016', 'location': 'Delhi'
#                             }, 
#                             {
#                                 'institution': 'Ideal Institute of Management and Technology of IP University', 
#                                 'degree': 'Bachelor of Business Administration', 
#                                 'major': 'unknown', 
#                                 'duration': '2011-2014', 
#                                 'location': 'unknown'
#                             }, 
#                             {
#                                 'institution': 'Rishabh Public School', 
#                                 'degree': 'XII', 
#                                 'major': 'CBSE Board', 
#                                 'duration': '2011', 
#                                 'location': 'Mayur Vihar, New Delhi'
                            
#                             }, 
#                             {
#                                 'institution': 'Rishabh Public School', 
#                                 'degree': 'X', 
#                                 'major': 'CBSE Board', 
#                                 'duration': '2009', 'location': 'Mayur Vihar, New Delhi'}]}

# print(validate_entities(extracted_entities=extracted_entities))
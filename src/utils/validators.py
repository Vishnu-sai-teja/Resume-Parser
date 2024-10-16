import re
from typing import List, Dict, Any

def validate_name(name: str) -> List[str]:
    """
    Validates the name extracted from the resume.

    Args:
        name (str): The extracted name.

    Returns:
        List[str]: A list of validation errors for the name.
    """
    errors = []
    if name:
        if len(name.split()) < 2:
            errors.append("Name should include both first and last name")
    return errors

def validate_email(email: str) -> List[str]:
    """
    Validates the email extracted from the resume.

    Args:
        email (str): The extracted email.

    Returns:
        List[str]: A list of validation errors for the email.
    """
    errors = []
    if email:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Invalid email format")
    return errors

def validate_phone(phone: str) -> List[str]:
    """
    Validates the phone number extracted from the resume.

    Args:
        phone (str): The extracted phone number.

    Returns:
        List[str]: A list of validation errors for the phone number.
    """
    errors = []
    if phone:
        phone = phone.replace(" ", "")
        if not re.match(r'^(\+\d{1,3})?[6-9]\d{9}$', phone):
            errors.append("Invalid phone number format")
    return errors

def validate_education(education: List[Dict[str, str]]) -> List[str]:
    """
    Validates the education details extracted from the resume.

    Args:
        education (List[Dict[str, Any]]): A list of dictionaries containing education details.

    Returns:
        List[str]: A list of validation errors for the education details.
    """
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
    """
    Validates the skills extracted from the resume.

    Args:
        skills (str): The extracted skills.

    Returns:
        List[str]: A list of validation errors for the skills.
    """
    errors = []
    if skills:  # Only validate if skills are provided
        if not skills.strip():
            errors.append("Skills cannot be empty")
    return errors

def validate_certifications(certifications: str) -> List[str]:
    """
    Validates the certifications extracted from the resume.

    Args:
        certifications (str): The extracted certifications.

    Returns:
        List[str]: A list of validation errors for the certifications.
    """
    errors = []
    if certifications:  # Only validate if certifications are provided
        if not certifications.strip():
            errors.append("Certifications cannot be empty")
    return errors

from typing import List, Dict
from datetime import datetime

def validate_experience(experience: List[Dict[str, str]]) -> List[str]:
    """
    Validates the work experience details extracted from the resume.

    Args:
        experience (List[Dict[str, Any]]): A list of dictionaries containing work experience details.

    Returns:
        List[str]: A list of validation errors for the work experience details.
    """
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
    """
    Validates the extracted entities from the resume text.

    Args:
        extracted_entities (Dict[str, Any]): A dictionary containing the extracted entities.

    Returns:
        Dict[str, List[str]]: A dictionary containing validation errors for each entity.
    """
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


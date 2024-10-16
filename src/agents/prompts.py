# prompt_v1 = (
#     "Please extract the following information from the resume text provided and format it as specified:\n"
#     "Note: In the following entities, if any result is not present, feel free to return an empty string.\n"
#     "- **Name**: Full name of the candidate.\n"
#     "- **Email**: Email address should follow the rules of an email.\n"
#     "- **Phone**: Phone number format and remove spaces.\n"
#     "- **Education**: Give me a list of all degrees and institutions, separated by double new lines.\n"
#     "- **Experience**: Provide a string of work experiences, with each experience separated by double new lines. For each experience, provide:\n"
#     "- **Skills**: All skills, remove any irrelevant terms and return a readable list (e.g., Python, Machine Learning).\n"
#     "- **Certifications**: All certifications, remove any irrelevant terms and return a readable list (e.g., Certified Data Scientist from Data Science Institute).\n\n"
#     "From the following resume, if any result is not present, strictly feel free to return an empty string: {resume_text}"
# )

# prompt_v2 = (
#     "Please extract the following information from the resume text provided and format it as specified:\n"
#     "Note: In the following entities, if any result is not present, feel free to return an empty string.\n"
#     "- **Name**: Provide the full name of the candidate. If not present, return an empty string.\n"
#     "- **Email**: Provide the email address, ensuring it follows the standard email format. If not present, return an empty string.\n"
#     "- **Phone**: Provide the phone number, formatted correctly without spaces. If not present, return an empty string.\n"
#     "- **Education**: List all degrees and institutions, separated by double new lines. If not present, return an empty string.\n"
#     "- **Experience**: Provide a string of work experiences, with each experience separated by double new lines. If not present, return an empty string.\n"
#     "- **Skills**: List all skills, removing any irrelevant terms. If not present, return an empty string.\n"
#     "- **Certifications**: List all certifications, removing any irrelevant terms. If not present, return an empty string.\n\n"
#     "From the following resume, if any result is not present, return an empty string: {resume_text}"
# )

prompt = (
    "Please extract the following information from the resume text provided and format it as specified:\n"
    "Note: In the following entities, if any result is not present, feel free to return an empty string.\n"
    "- **Name**: Provide the full name of the candidate. If not present, return an empty string.\n"
    "- **Email**: Provide the email address, ensuring it follows the standard email format. If not present, return an empty string.\n"
    "- **Phone**: Provide the phone number, formatted correctly without spaces. If not present, return an empty string.\n"
    "- **Education**: List all degrees and institutions with the dates in the format 'Month Year', separated by double new lines. If not present, return an empty string.\n"
    "- **Experience**: Provide a string of work experiences, including the employment duration in the format 'Month Year - Month Year' (or 'Month Year - Present'), with each experience separated by double new lines. If not present, return an empty string.\n"
    "- **Skills**: List all skills, removing any irrelevant terms. If not present, return an empty string.\n"
    "- **Certifications**: List all certifications, removing any irrelevant terms. If not present, return an empty string.\n\n"
    "From the following resume, if any result is not present, return an empty string: {resume_text}"
)

correction_prompt = (
    "Please carefully re-evaluate and extract the **{field}** from the resume provided below.\n\n"
    "Pay special attention to the following issues that were identified during the previous extraction:\n"
    "- {errors}\n\n"
    "These issues may have led to inaccuracies or missing information, so it is crucial to address them during this extraction. "
    "Focus on providing a thorough and precise extraction of the requested field, ensuring that all relevant details are captured and corrected.\n\n"
    "### Resume Content:\n"
    "{resume_text}\n\n"
    "Thank you for your careful attention to these details."
)


experience_prompt = (
    "Note : In the follwing entities if any result is not present feel free to return empty string\n"
    "- Company: Name of the company\n"
    "  - Role: Job title or role\n"
    "  - Work Done: Brief description of responsibilities and achievements\n"
    "  - Duration: Time period of employment\n"
    "Extract all these details from the experience text below \n {experience_text}"
)

education_prompt = (
    "Note : In the follwing entities if any result is not present feel free to return empty string\n"
    "- Institution: Name of the educational institution\n"
    "  - Degree: Type of degree obtained (e.g., Bachelor's, Master's)\n"
    "  - Major: Major or field of study\n"
    "  - Duration: Time period of study (e.g., Expected Graduation Date)\n"
    "  - Location: City and state (or country) of the institution\n"
    "Extract all these details from the education text below:\n{education_text}"
)
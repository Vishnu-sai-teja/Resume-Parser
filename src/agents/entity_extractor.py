import time
from .state import ResumeState, Education, Experience, ExtractorState
from pydantic import BaseModel, Field
from utils.utils import set_key, StateToDict
from .prompts import prompt, education_prompt, experience_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Dict, List, Any


def entity_extractor(state: ResumeState):
    set_key('./config.json', 'GOOGLE_API_KEY')
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", temperature=0)

    try:
        
        response = llm.with_structured_output(ExtractorState).invoke(prompt.format(resume_text=state['resume_text']))
        # print("Structured response:", response)
        degrees = response.education.split('\\n\\n')
        # print(f"\n\n {degrees}   \n\n")
        edu = []
        for degree in degrees:
            time.sleep(2)
            education = llm.with_structured_output(Education).invoke(degree)
            edu.append(StateToDict(Education, education))

        # Get the experiience in a more structured format
        work_experience = response.experience.split('\\n\\n')
        exp = []
        for experience in work_experience:
            time.sleep(2)
            experience = llm.with_structured_output(Experience).invoke(experience)
            exp.append(StateToDict(Experience, experience))


        # print("\n\n", edu)
        # print("\n\n" , degrees)
        return {"resume_text" : state['resume_text'],
                "extracted_entities": {
                    "name": response.name,
                    "phone":response.phone,
                    "email": response.email,
                    "education": edu,
                    "experience": exp,
                    "skills": response.skills,
                    "certifications": response.certifications
                },
                "current_stage": "entity_validation"}
    except:
        raise ValueError('Error extracting resume information')

# if __name__ == "__main__":
#     state = {"resume_text": """## Vishnu Sai Teja Nagabandi

# **vishnusaiteja.3004@gmail.com | +91 89 78044062**

# **EDUCATION**

# **IIIT NAGPUR**
# * B Tech Computer Science
# * Expected 2025
# * Nagpur, Maharashtra
# * CGPA: 8.46 / 10.0
# * Major GPA: 9.33 / 10.0

# **SRI CHAITHANYA**
# * Senior Secondary Education
# * Graduated 2021
# * Hyderabad, Telangana
# * Overall Percentage: 98.2%

# **LINKS**

# * **GitHub:** Vishnu-sai-teja
# * **LinkedIn:** Vishnu SaiTejaNag
# * **X (Twitter):** @NagSate
# * **Kaggle:** Vishnu SaiTejaN

# **COURSEWORK**

# **UNDER GRADUATE**

# * Mathematics Data Science
# * Numerical Methods Probability
# * Discrete Mathematics Graph Theory
# * Application Programming
# * Object Oriented Programming
# * Computer Networks
# * Computer System Organization
# * Operating System
# * Theory Computation
# * Compilers
# * Database Management Systems
# * Data Structures
# * Cloud Computing Applied Sciences
# * Machine Learning

# **SKILLS**

# **Programming Languages**

# * C++
# * Python
# * Java
# * Basic Shell
# * Basic Rust
# * CSS
# * JS

# **Frameworks**

# * LangChain
# * PyTorch
# * Basic Django
# * MySQL
# * Basic PHP

# **Libraries**

# * Numpy
# * Pandas
# * Matplotlib
# * Sci-kit Learn
# * nltk
# * Basic fastai

# **LANGUAGES**

# **Proficient**

# * English
# * Hindi
# * Telugu

# **Novice**

# * German

# **EXPERIENCE**

# **AIDASH Data Science Intern**
# * April 2024 - Present | Bangalore, India
#     * Implemented end-to-end asset geotagging pipeline using street view imagery, optimizing object detection, depth and height estimation.
#     * Designed and implemented asynchronous processing and parallelization, significantly boosting pipeline efficiency and maximizing hardware resource utilization.
#     * Fine-tuned detection models for specific assets, achieving faster processing times and improved accuracy in geolocating assets.

# **VLIPPR ML and Data Science Intern**
# * Nov 2023 - Feb 2024 | New Delhi, India
#     * Contributed to Vaanee, an audio model specializing in Indian languages.
#     * Led efforts in the preprocessing of intricate audio data.
#     * Proposed and implemented techniques for audio pre and post processing to enhance the accuracy of audio transcription.

# **PROJECTS**

# **STAFFUSION**
# * PyTorch | Python
#     * Implemented an end-to-end stable diffusion pipeline for Text-to-image.
#     * Integrated UNet, CLIP, and Vision Transformers for the pipeline.
#     * Utilizing pretrained weights and implementing fine-tuning with adapters to enhance efficiency.
#     * Achieved a complete stable diffusion pipeline for high-quality image generation.
#     * GitHub Repository of Staffusion

# **CANCER DETECTION USING GANS**
# * Implemented using GANs
#     * Developed a Generative Adversarial Network (GAN) to enhance cancer detection dataset and accuracy from medical images.
#     * Achieved improved diagnostic performance through synthetic data generation and model training.

# **INDIAN LANGUAGE DETECTION**
# * Implemented on 2 lakh+ audio files
#     * Considered a dataset of major Indian languages with about 2 lakh+ audio files.
#     * Implemented Preprocessing and Segmentation to rule out outliers effectively.
#     * Achieved an accuracy of 88.6% on the language dataset.
#     * Kaggle Notebook on Language Detection

# **ACHIEVEMENTS AND CONTRIBUTIONS**

# * **Bank Customer Churn Prediction**
#     * Kaggle Ranking: 130/3000
#     * Predicted churn using the Bank Churn Dataset with 10,000+ datapoints and 14+ features. Applied CatBoost and hybrid models, achieving a score of 0.8952.
#     * Kaggle Notebook
# * **Tantrafiesta 23**
#     * Developed the Fiesta website and assisted in securing sponsors."""
#              }
#     result = resume_extractor(state)
#     print(result)
    

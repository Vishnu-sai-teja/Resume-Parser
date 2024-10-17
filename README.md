# Multi-Agent Resume Processor

## Project Overview

This project implements a multi-agent workflow for processing resumes using Large Language Models (LLMs). It automates the extraction of key information from multi-page resumes, validates the extracted data, and allows for human intervention and feedback at various stages of the process.

## Features

- Resume Reading: Processes multi-page resumes in various formats (PDF, DOCX)
- Entity Extraction: Extracts key information such as personal details, education, work experience, and skills
- Entity Validation: Validates extracted information for accuracy and completeness
- Human Feedback Loop: Allows for user intervention and feedback at each stage
- JSON Output: Compiles validated entities into a predefined JSON format
- Monitoring: Utilizes LangGraph and LangSmith for monitoring LLM calls

## Installation

1. Clone the repository:
   ```
   git clone [repository-url]
   cd [repository-name]
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

* Set the src as the root file 

To process a resume, run the following command:

```
python main.py --file_path /path/to/your/resume.pdf
```

## Human Feedback Loop

The system allows for human intervention at each stage of the process. When prompted:

1. Enter the state you want to modify, or type 'next' to proceed to the next stage.
2. If modifying a state, enter the new value when prompted.
3. Type 'quit' at any time to exit the process.

## Monitoring

This project uses LangGraph and LangSmith for monitoring LLM calls. To view the monitoring data:

1. [Instructions for accessing LangGraph monitoring]
2. [Instructions for accessing LangSmith monitoring]

## Project Structure

- `main.py`: Entry point of the application
- `agents/`:
  - `state.py`: Defines the ResumeState class
  - `resume_reader.py`: Contains the resume reading logic
  - `entity_extractor.py`: Implements entity extraction
  - `entity_validation.py`: Handles validation of extracted entities
  - `store_entities.py`: Manages storage of validated entities
  - `entity_corrector.py`: Implements correction logic for extracted entities

## Testing

Testing of all the agents have been implemented using the `pytest` library
- `tests` :
  - `test_resume_reader.py`  : Define unit tests for resume reader agent
  - `test_entity_extractor.py` : Define unit test cases for entity extraction agent
  - `test_entity_Validation.py` : Define unit test cases for the entity validation agent

## Assumptions and Design Decisions

- [List any important assumptions or design decisions made during development]

## Future Improvements

- Implement comprehensive unit tests for each component
- Implement a graphical user interface for easier interaction
- Enhance error handling and edge case management
- Improve scalability to handle a larger volume of resumes

## Contributing

## License

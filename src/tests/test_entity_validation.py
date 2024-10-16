import pytest
from unittest.mock import patch, MagicMock
from agents.entity_validation import entity_validation
from agents.state import ResumeState, ExtractorState, Education, Experience

@pytest.fixture
def mock_set_key():
    with patch('agents.entity_validation.set_key') as mock:
        yield mock
    
@pytest.fixture
def mock_chat_ggai():
    with patch('agents.entity_validation.ChatGoogleGenerativeAI') as mock:
        yield mock

@pytest.fixture
def mock_validity_entities():
    with patch('agents.entity_validation.validate_entities') as mock:
        yield mock
    

state = ResumeState({
        'resume_text': 'Sample resume text',
        'extracted_entities': {
            'name' : 'Vishnu Sai Teja',
            'email' : 'visate.nags@gmail.com',
            'phone': '12345657890',
            'education': [{
                'institution': 'IIIT Nagpur',
                'degree': 'B.Tech',
                'major': 'Computer Science', 
                'duration': '2021-2025', 
                'location': 'Nagpur'
            }],
            'experience': [{
                'company': 'AIDASH', 
                'role': 'Data Science Intern', 
                'work_done': 'Implemented geotagging pipeline ', 
                'duration': 'April 2024'
            }],
            'skills': 'Python, Java, C++',
            'certifications': 'AWS Certified Developer'
        },
        'current_stage': 'entity_validation'
    })

def test_entity_validation(mock_set_key, mock_chat_ggai, mock_validity_entities):
    mock_validation_results = {
            'name': [],
            'email': [],
            'phone': ['Invalid phone format'],
            'education': [],
            'experience': [],
            'skills': [],
            'certifications': []
        }

    mock_validity_entities.return_value = mock_validation_results
    result = entity_validation(state)

    mock_set_key.assert_called_once_with('./config.json', 'GOOGLE_API_KEY')
    mock_chat_ggai.assert_called_once_with(model="gemini-1.5-flash", temperature=0)
    mock_validity_entities.assert_called_once()

    assert result['current_stage'] == "_END_"
    assert 'validated_entities' in result
    assert result['validated_entities'] == {'phone': ['Invalid phone format']}
    assert result['resume_text'] == state['resume_text']
    assert result['extracted_entities'] == state['extracted_entities']

if __name__ == "__main__":
    pytest.main()

    
import pytest
from unittest.mock import patch, MagicMock
from agents.entity_extractor import entity_extractor
from agents.state import ResumeState, ExtractorState, Education, Experience

@pytest.fixture
def mock_chat_ggai():
    with patch('agents.entity_extractor.ChatGoogleGenerativeAI') as mock:
        yield mock

@pytest.fixture
def mock_state():
    return ResumeState({
        'resume_text': 'Sample resume text',
        'extracted_entities': {},
        'current_stage': 'entity_extraction'
    })

@pytest.fixture
def mock_extractor_response():
    return ExtractorState(
        name="Vishnu sai teja",
        email="visate@gmail.com",
        phone="1234567890",
        education="IIIT Nagpur\\n\\nChaithanya",
        experience="Company Alpha\\n\\nCompany Beta",
        skills="Python, Java",
        certifications="AWS Certified"
    )

@pytest.fixture
def mock_education_response():
    return Education(
        institution="IIIT Nagpur",
        degree="Bachelor's",
        major="Computer Science",
        duration="2016-2020",
        location="Example City"
    )

@pytest.fixture
def mock_experience_response():
    return Experience(
        company="Company Alpha",
        role="Software Engineer",
        work_done="Developed applications",
        duration="2020-2023"
    )

def test_entity_extractor_success(mock_chat_ggai, mock_state, mock_extractor_response, mock_education_response, mock_experience_response):
    mock_llm_instance = MagicMock()
    # What to reaturn each time invoke is called :-)
    mock_llm_instance.with_structured_output.return_value.invoke.side_effect = [
        mock_extractor_response,
        mock_education_response,
        mock_education_response,
        mock_experience_response,
        mock_experience_response
    ]
    mock_chat_ggai.return_value = mock_llm_instance

    result = entity_extractor(mock_state)

    assert result['current_stage'] == "entity_validation"
    assert 'extracted_entities' in result
    assert result['extracted_entities']['name'] == "Vishnu sai teja"
    assert len(result['extracted_entities']['education']) == 2
    assert len(result['extracted_entities']['experience']) == 2

def test_entity_extractor_empty_resume_text(mock_chat_ggai):
    state = ResumeState({
        'resume_text': '',
        'extracted_entities': {},
        'current_stage': 'entity_extraction'
    })

    with pytest.raises(ValueError, match="Error extracting resume information"):
        entity_extractor(state)

def test_entity_extractor_llm_error(mock_chat_ggai, mock_state):
    state = ResumeState({
        'resume_text': '',
        'extracted_entities': {},
        'current_stage': 'entity_extraction'
    })
    
    mock_llm_instance = MagicMock()
    mock_llm_instance.with_structured_output.invoke.side_effect = Exception("Testing phase")
    mock_chat_ggai.side_effect = mock_llm_instance

    with pytest.raises(ValueError, match="Error extracting resume information"):
        entity_extractor(state)

if __name__ == "__main__":
    pytest.main()
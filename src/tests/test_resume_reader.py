import pytest
from unittest.mock import patch, MagicMock
from agents.resume_reader import resume_reader
from agents.state import ResumeState

@pytest.fixture
def mock_read_file():
    with patch('agents.resume_reader.read_file') as mock:
        yield mock

@pytest.fixture
def mock_set_key():
    with patch('agents.resume_reader.set_key') as mock:
        yield mock

@pytest.fixture
def mock_chat_ggai():
    with patch('agents.resume_reader.ChatGoogleGenerativeAI') as mock:
        yield mock

@pytest.fixture
def mock_llm_response():
    mock_response = MagicMock()
    mock_response.content = "Formatted resume content"
    return mock_response

@pytest.fixture
def mock_state():
    return ResumeState({'file_path': 'dummy/path/to/resume.pdf'})

def test_resume_reader_file_read_error(mock_read_file, mock_set_key, mock_chat_ggai):
    mock_read_file.side_effect = Exception("File read error")
    
    state = ResumeState({'file_path': '/path/to/resume.pdf'})

    with pytest.raises(ValueError, match='Error reading resume file'):
        resume_reader(state)

def test_resume_reader_success(mock_chat_ggai, mock_read_file, mock_set_key, mock_state, mock_llm_response):
    mock_read_file.return_value = "Raw resume content"
    mock_llm_instance = MagicMock()
    mock_llm_instance.invoke.return_value = mock_llm_response
    mock_chat_ggai.return_value = mock_llm_instance

    result = resume_reader(mock_state)

    mock_set_key.assert_called_once_with('./config.json', 'GOOGLE_API_KEY')
    mock_read_file.assert_called_once_with('dummy/path/to/resume.pdf')
    mock_chat_ggai.assert_called_once_with(model="gemini-1.5-flash", temperature=0)
    mock_llm_instance.invoke.assert_called_once()
    
    assert result == {
        "resume_text": "Formatted resume content",
        "current_stage": "entity_extraction"
    }

def test_resume_reader_empty_path():
    state = ResumeState({'file_path': ''})

    with pytest.raises(ValueError, match="No resume file path provided"):
        resume_reader(state)

if __name__ == "__main__":
    pytest.main()

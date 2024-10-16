import pytest
from unittest.mock import patch, MagicMock
from agents.resume_reader import resume_reader
from agents.state import ResumeState

@pytest.fixture
def mock_state():
    return ResumeState({'file_path': './aman_resume.pdf', 'resume_text': None})

@pytest.fixture
def mock_llm_response():
    llm_response = MagicMock()
    llm_response.content = "This is mock llm response"
    return llm_response


@patch('agents.resume_reader.set_key')
@patch('agents.resume_reader.read_file')
@patch('agents.resume_reader.ChatGoogleGenerativeAI')
def test_resume_reader_sucess(mock_chat_ggai, mock_read_file, mock_set_key, mock_state, mock_llm_response):
    mock_read_file.return_value = "Raw resume content"
    mock_llm_instance = MagicMock()
    mock_llm_instance.invoke.return_value = "Hey there I am gemini"
    mock_chat_ggai.return_value = mock_llm_instance

    result = resume_reader(mock_state)

    # mock_set_key.assert_called_once_with('./config.json', 'AIzaSyClhzF2a6bIfx145Q_hg9VVBuGfCGNgYwU') 
    mock_read_file.assert_called_once_with('./aman_resume.pdf')
    mock_chat_ggai.assert_called_once_with(model="gemini-1.5-flash", temperature=0)
    mock_llm_instance.invoke.assert_called_once()

if __name__ == "__main__":
    test_resume_reader_sucess(mock_state, mock_llm_response)



import pytest
from unittest.mock import patch, MagicMock
from agents.resume_reader import resume_reader
from agents.state import ResumeState

@pytest.fixture
def mock_state():
    return ResumeState({'file_path': './aman_resume.pdf', 'resume_text': None})

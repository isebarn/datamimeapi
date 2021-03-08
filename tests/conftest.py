import pytest

from main import app as flask_app
import os

def pytest_generate_tests(metafunc):
  os.environ['DATABASE'] = "mongodb://admin:=2`MW8Xe*uKe@cpx-devtest-db.skan.ai:8805/"

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()
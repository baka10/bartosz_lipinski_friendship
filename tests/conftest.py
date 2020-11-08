import pytest

from app import create_app
from config import config


@pytest.yield_fixture
def app_client():
    app = create_app(config)
    ctx = app.test_request_context()
    ctx.push()

    def create_test_client():
        return app.test_client()

    client = create_test_client()

    yield client

    ctx.pop()

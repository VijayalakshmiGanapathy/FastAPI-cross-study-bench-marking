import os
import sys

from fastapi.testclient import TestClient

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from main import app


client = TestClient(app)
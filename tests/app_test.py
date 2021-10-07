import pytest
from gothonweb import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    pass
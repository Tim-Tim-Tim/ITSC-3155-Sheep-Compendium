# Import TestClient to simulate API requests
from fastapi.testclient import TestClient

# Import FastAPPI app instance from the controller module
from main import app

# Create a TestClient instance for the FastAPI app
client = TestClient(app)

# Define a test function for reading a specific sheep
def test_read_sheep():
    # Send a GET request to the endpoint "/sheep/1"
    response = client.get("/sheep/1")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response JSON matches the expected data
    assert response.json() == {
        # Expected JSON structure
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():
    return
# TODO: Prepare the new sheep data in a dictionary format.

# TODO: Send a POST request to the endpoint "/sheep" with the new sheep data.
# Arguments should be your endpoint and new sheep data.

# TODO: Assert that the response status code is 201 (Created)

# TODO: Assert that the response JSON matches the new sheep data

# TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
# include an assert statement to see if the new sheep data can be retrieved.
# Import TestClient to simulate API requests
from fastapi.testclient import TestClient

# Import FastAPPI app instance from the controller module
from main import app

# Import the artificial database to compare it to what is being stored in the fastAPI database
from main import db

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
    # Prepare the new sheep data in a dictionary format.
    new_sheep = {
        "id": 9,
        "name": "Right-most sheep",
        "breed": "babydoll",
        "sex": "ewe"
    }

    # Send a POST request to the endpoint "/sheep" with the new sheep data.
    # Arguments should be your endpoint and new sheep data.
    response = client.post("/sheep", json=new_sheep)

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # Assert that the response JSON matches the new sheep data
    assert response.json() == {
        # Expected JSON structure
        "id": 9,
        "name": "Right-most sheep",
        "breed": "babydoll",
        "sex": "ewe"
    }

    # Verifying that the sheep was actually added to the database by retrieving the new sheep by ID.
    # include an assert statement to see if the new sheep data can be retrieved.
    response = client.get("/sheep/9")
    assert response.status_code == 200
    assert response.json() == {
        "id": 9,
        "name": "Right-most sheep",
        "breed": "babydoll",
        "sex": "ewe"
    }

def test_delete_sheep():
    # Prepare new sheep data in a dictionary format.
    new_sheep = {
        "id": 10,
        "name": "Mr Deleto",
        "breed": "fake goat sheep",
        "sex": "ewe"
    }

    # Send a POST request to the endpoint "/sheep" with the new sheep data.
    # Arguments should be your endpoint and new sheep data.
    response = client.post("/sheep", json=new_sheep)

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # Assert that the response JSON matches the new sheep data
    assert response.json() == {
        # Expected JSON structure
        "id": 10,
        "name": "Mr Deleto",
        "breed": "fake goat sheep",
        "sex": "ewe"
    }

    # Verifying that the sheep was actually added to the database by retrieving the new sheep by ID.
    # include an assert statement to see if the new sheep data can be retrieved.
    response = client.get("/sheep/10")
    assert response.status_code == 200
    assert response.json() == {
        "id": 10,
        "name": "Mr Deleto",
        "breed": "fake goat sheep",
        "sex": "ewe"
    }

    # Verifying that the sheep was actually deleted from the database by retrieving the sheep by ID.
    # include an assert statement to see if the deleted sheep's data.
    response = client.delete("/sheep/10")
    assert response.status_code == 200
    assert response.json() == {
        "id": 10,
        "name": "Mr Deleto",
        "breed": "fake goat sheep",
        "sex": "ewe"
    }


def test_update_sheep():
    # Prepare new sheep data in a dictionary format.
    sheep = {
        "id": 11,
        "name": "Please update me",
        "breed": "Sleepy sheep",
        "sex": "ewe"
    }

    # Send a POST request to the endpoint "/sheep" with the new sheep data.
    # Arguments should be your endpoint and new sheep data.
    response = client.post("/sheep", json=sheep)

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # Assert that the response JSON matches the new sheep data
    assert response.json() == {
        # Expected JSON structure
        "id": 11,
        "name": "Please update me",
        "breed": "Sleepy sheep",
        "sex": "ewe"
    }

    # Verifying that the sheep was actually added to the database by retrieving the new sheep by ID.
    # include an assert statement to see if the new sheep data can be retrieved.
    response = client.get("/sheep/11")
    assert response.status_code == 200
    assert response.json() == {
        "id": 11,
        "name": "Please update me",
        "breed": "Sleepy sheep",
        "sex": "ewe"
    }

    # Updating sheep data
    # Verifying that the sheep was actually Updated in the database by retrieving the updated sheep by ID.
    # include an assert statement to see if sheep's data has been updated properly.
    new_sheep = {
        "id": 11,
        "name": "Mr Updato",
        "breed": "Dinosaur sheep",
        "sex": "ewe"
    }
    response = client.put("/sheep/11", json=new_sheep)
    assert response.status_code == 200
    assert response.json() == {
        "id": 11,
        "name": "Mr Updato",
        "breed": "Dinosaur sheep",
        "sex": "ewe"
    }

def test_read_all_sheep():
    # Send a GET request to the endpoint "/sheep/"
    response = client.get("/sheep/")
    assert response.status_code == 200
    sheep_list = response.json()
    # Iterate over sheep_list to make sure they match with the data in db
    for sheep in sheep_list:
        sheep_id = sheep['id']
        # Check if the sheep_id exists in db.data
        assert sheep_id in db.data
        db_sheep = db.data[sheep_id]
        db_sheep_dict = db_sheep.model_dump()  # Use model_dump() instead of dict()
        # Compare the dictionaries
        assert sheep == db_sheep_dict
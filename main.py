from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep


app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    # Check if the sheep ID exists
    if id in db.data:
        return db.get_sheep(id)
    # In case sheep ID does not exist
    else:
        raise HTTPException(status_code=404, detail="Sheep not found")


@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    # Check if the sheep ID already exists to avoid duplicates
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")

    # Add the new sheep to the database
    db.data[sheep.id] = sheep
    return sheep # Return the newly added sheep data



@app.delete("/sheep/{id}", response_model=Sheep, status_code=status.HTTP_200_OK)
def delete_sheep(id: int):
    # Check if the sheep ID exists
    if id in db.data:
        # Delete the sheep to the database
        sheep = db.data[id]
        del db.data[id]
        return sheep  # Return the deleted sheep data

    # In case sheep ID does not exist
    else:
        raise HTTPException(status_code=404, detail="Sheep not found")



@app.put("/sheep/{id}", response_model=Sheep, status_code=status.HTTP_200_OK)
def update_sheep(id: int, sheep: Sheep):
        # Check if the sheep ID exists
        if id in db.data:
            # Update the sheep to the database
            db.data[id] = sheep
            return sheep  # Return the updated sheep data

        # In case sheep ID does not exist
        else:
            raise HTTPException(status_code=404, detail="Sheep not found")


@app.get("/sheep/", response_model=list[Sheep])
def read_sheep():
    #Return the list of sheep stored in data
    return list(db.data.values())
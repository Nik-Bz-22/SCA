# Spy Cat Agency

## Installation
### 1. Clone the repository

```bash
git clone https://github.com/SCA.git
cd SCA

source -m venv .venv

pip install --requirment requirments.txt

python manage.py migrate

python manage.py createsuperuser (optional)

python manage.py runserver
```


## API Endpoints
### 1. Cats

    GET /api/spy_cats/ — Get a list of all cats.
    POST /api/spy_cats/ — Create a new cat.
    GET /api/spy_cats/{id}/ — Get information about a cat by its ID.
    PUT /api/spy_cats/{id}/ — Update a cat's information.
    DELETE /api/spy_cats/{id}/ — Delete a cat.

### 2. Targets

    GET /api/targets/ — Get a list of all targets.
    POST /api/targets/ — Create a new target.
    GET /api/targets/{id}/ — Get information about a target by its ID.
    PUT /api/targets/{id}/mark_complete/ - Mark target as complete
    
### 3. Missions
    GET /api/missions/ — Get a list of all missions.
    POST /api/missions/ — Create a new mission.
    GET /api/missions/{id}/ — Get information about a mission by its ID.
    DELETE /api/missions/{id}/ — Delete a mission.
    PUT /api/missions/{id}/mark_complete/ - Mark mission as complete
    PUT /api/missions/{id}/assign_cat/ - Assign cat to mission



## Postman collection
https://www.postman.com/mission-operator-7994535/818f8257-4c28-4bae-9e38-f1a045950b3b/collection/okg6p99/cat-crud

<br><br><br><br><br>

# Task Description:

### Overview

This task involves building a CRUD application. The goal is to create a system that showcases your understanding in building RESTful APIs, interacting with SQL-like databases, and integrating third-party services. The test assessment is expected to be done within 2 hours.

### Requirements

Spy Cat Agency (SCA) asked you to create a management application, so that it simplifies their spying work processes. SCA needs a system to manage their cats, missions they undertake, and targets they are assigned to.

From cats perspective, a mission consists of spying on targets and collecting data. One cat can only have one mission at a time, and a mission assumes a range of targets (minimum: 1, maximum: 3). While spying, cats should be able to share the collected data into the system by writing notes on a specific target. Cats will be updating their notes from time to time and eventually mark the target as complete. If the target is complete, notes should be frozen, i.e. cats should not be able to update them in any way. After completing all of the targets, the mission is marked as completed.

From the agency perspective, they regularly hire new spy cats and so should be able to add them to and visualize in the system. SCA should be able to create new missions and later assign them to cats that are available. Targets are created in place along with a mission, meaning that there will be no page to see/create all/individual targets.

**Backend Requirements:**

- **Spy Cats**
    - Ability to create a spy cat in the system
        - A cat is described as Name, Years of Experience, Breed, and Salary.
        - Breed must be validated, see General
    - Ability to remove spy cats from the system
    - Ability to update spy cats’ information (Salary)
    - Ability to list spy cats
    - Ability to get a single spy cat
- **Missions / Targets**
    - Ability to create a mission in the system along with targets in one single request
        - A mission contains information about Cat, Targets and Complete state
        - Each target is unique to a mission, so the endpoint should accept an object describing targets
        - A target is described as Name, Country, Notes and Complete state
    - Ability to delete a mission
        - A mission cannot be deleted if it is already assigned to a cat
    - Ability to update mission targets
        - Ability to mark it as completed
        - Ability to update Notes
            - Notes cannot be updated if either the target or the mission is completed
    - Ability to assign a cat to a mission
    - Ability to list missions
    - Ability to get a single mission
- **General**
    - Framework
        - Use any of: FastAPI, Django
    - Database
        - You can use any database
    - Validations
        - Make sure endpoints validate the request body and return an adequate status code if it’s not valid
        - Validate cat’s breed with [TheCatAPI](https://api.thecatapi.com/v1/breeds)
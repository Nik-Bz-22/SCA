# SCA

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
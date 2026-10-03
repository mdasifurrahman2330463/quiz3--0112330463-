# Quiz 3 - CRUD API + Testing

Student ID: 0112330463
Repository: quiz3-0112330463
Framework: FastAPI
Testing: pytest + FastAPI TestClient

## Install

python -m pip install -r requirements.txt

## Run the API

python -m uvicorn main:app --reload

Then open:
http://127.0.0.1:8000/docs

## Run tests

python -m pytest

## Required endpoints

GET /books
POST /books (201)
PUT /books/{id}
DELETE /books/{id}

Deleting a non-existing book returns 404.

## Required tests

test_create_book()
test_delete_book()

## Bonus tests

test_get_all_books()
test_update_book()

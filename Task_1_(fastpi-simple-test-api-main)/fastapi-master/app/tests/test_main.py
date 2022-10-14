from starlette.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Fast API in Python"}


def test_read_user():
    response = client.get("/user")
    assert response.status_code == 200
    assert response.json()[1] == { "id": 2, "name": "Leandro", "mail": "example_leandro@mail.com", "phone": "94435676" }

def test_read_questions():
    response = client.get("/question/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "position": 1, "question": "Which car model/category are you looking for?"}


def test_read_questions_n():
    response = client.get("/question/4")
    assert response.status_code == 400
    assert response.json() == {"detail": "Error"}


def test_read_alternatives():
    response = client.get("/alternatives/1")
    assert response.status_code == 200
    assert response.json()[1] == {"id": 2, "question_id": 1, "alternative": "utilitary"}


def test_read_alternatives_bad_request():
    response = client.get("/alternatives/4")
    assert response.status_code == 400
    assert response.json() == {"detail": "Question_id not found"}


def test_create_answer():
    response = client.post("/answer", json={"user_id": 1, "answers": [{"question_id": 4, "alternative_id": 11}]})
    assert response.status_code == 201
    assert response.json() == {"details": "Created"}


def test_read_result():
    response = client.get("/result/1")
    assert response.status_code == 200
    assert response.json() == [{"user": {"id": 1, "name": "Marcio", "mail": "example@mail.com", "phone": "98769878"}},
                               {"id": 2, "name": "Porsche Taycan", "fuel": "electric", "price": "high",
                                "category": "sporting", "link": ""},
                               {"id": 4, "name": "Vauxhall e-Corsa", "fuel": "electric", "price": "low",
                                "category": "compact", "link": ""}]


def test_read_result_invalid_user_id():
    response = client.get("/result/3")
    assert response.status_code == 200
    assert response.json() == [{"id": 2, "name": "Porsche Taycan", "fuel": "electric", "price": "high",
                                "category": "sporting", "link": ""},
                               {"id": 4, "name": "Vauxhall e-Corsa", "fuel": "electric", "price": "low",
                                "category": "compact", "link": ""}]

from fastapi.testclient import TestClient

from pydantic_dataclasses import app


client = TestClient(app)


def test_square():
    w, f = 10, 100
    response = client.post(
        "/square/",
        headers={"X-Token": "coneofsilence"},
        json={"w": w, "material": {"f": f}},
    )
    assert response.status_code == 200

    res = response.json()["res"]
    area = w * w
    assert res["area"] == area
    force_max = f / 1.5 * area
    assert res["force_max"] == force_max


def test_triangle():
    w, h, f = 10, 3, 100
    response = client.post(
        "/triangle/",
        headers={"X-Token": "coneofsilence"},
        json={"w": w, "h": h, "material": { "f": f}}
    )
    assert response.status_code == 200

    res = response.json()["res"]
    area = w * h * 0.5
    assert res["area"] == area
    force_max = f / 1.5 * area
    assert res["force_max"] == force_max


"""
MANUAL TESTS IN TERMINAL:
curl -X POST http://127.0.0.1:8000/square/ -H 'Content-Type: application/json' -d '{"w":10,"material":{"f":8}}'

curl -X POST http://127.0.0.1:8000/triangle/ -H 'Content-Type: application/json' -d '{"w":10,"h":8,"material":{"f":8}}'
"""

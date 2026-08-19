from fastapi.testclient import TestClient

from apps.api.app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_bazi_golden_chart_1990_05_15_noon_male():
    response = client.post(
        "/v1/bazi/chart",
        json={
            "solar_date": "1990-05-15",
            "birth_time": "12:00",
            "sex": "男",
            "birth_place": "北京",
        },
    )
    assert response.status_code == 200, response.text
    body = response.json()
    chart = body["chart"]
    pillars = chart["pillars"]

    assert pillars["year"][0] + pillars["year"][1] == "庚午"
    assert pillars["month"][0] + pillars["month"][1] == "辛巳"
    assert pillars["day"][0] + pillars["day"][1] == "庚辰"
    assert pillars["hour"][0] + pillars["hour"][1] == "壬午"
    assert chart["forward"] is True


def test_rejects_two_time_inputs():
    response = client.post(
        "/v1/bazi/chart",
        json={
            "solar_date": "1990-05-15",
            "birth_time": "12:00",
            "shichen": "午",
            "sex": "男",
        },
    )
    assert response.status_code == 422

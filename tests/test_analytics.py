from tests.conftest import client


def test_get_all_studies():
    response = client.get(
        "/api/v1/metrics/cross-study"
    )

    assert response.status_code == 200


def test_phase_filter():
    response = client.get(
        "/api/v1/metrics/cross-study?phase=Phase I"
    )

    assert response.status_code == 200


def test_invalid_phase():
    response = client.get(
        "/api/v1/metrics/cross-study?phase=Invalid"
    )

    assert response.status_code == 404

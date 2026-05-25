"""
Unit and API tests for analytics endpoints.

This module validates:
- endpoint accessibility
- phase filtering
- invalid phase handling
"""

from tests.conftest import client


def test_get_all_studies() -> None:
    """
    Test retrieval of all study metrics.

    Validates:
    - API accessibility
    - successful HTTP response
    """

    response = client.get(
        "/api/v1/metrics/cross-study"
    )

    assert response.status_code == 200

    data = response.json()

    assert "studies" in data
    assert "generated_at" in data


def test_phase_filter() -> None:
    """
    Test phase-based filtering.

    Validates:
    - query parameter handling
    - filtered API response
    """

    response = client.get(
        "/api/v1/metrics/cross-study?phase=Phase I"
    )

    assert response.status_code == 200

    data = response.json()

    for study in data["studies"]:
        assert study["phase"] == "Phase I"


def test_invalid_phase() -> None:
    """
    Test invalid phase exception handling.

    Validates:
    - HTTP 404 response
    - proper error message
    """

    response = client.get(
        "/api/v1/metrics/cross-study?phase=Invalid"
    )

    assert response.status_code == 404

    data = response.json()

    assert "detail" in data

def test_status_filter():

    response = client.get(
        "/api/v1/metrics/cross-study?status=Completed"
    )

    assert response.status_code == 200


def test_invalid_status():

    response = client.get(
        "/api/v1/metrics/cross-study?status=Invalid"
    )

    assert response.status_code == 404
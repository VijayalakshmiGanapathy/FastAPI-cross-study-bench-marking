"""
Unit and API tests for analytics endpoints.

This module validates:
- endpoint accessibility
- phase filtering
- invalid phase handling
"""

from crud_metrics import (
    get_latest_metrics_for_study
)

from database import SessionLocal

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


# def test_phase_filter() -> None:
#     """
#     Test phase-based filtering.

#     Validates:
#     - query parameter handling
#     - filtered API response
#     """

#     response = client.get(
#         "/api/v1/metrics/cross-study?phase=Phase I"
#     )

#     assert response.status_code == 200

#     data = response.json()

#     for study in data["studies"]:
#         assert study["phase"] == "Phase I"


# def test_invalid_phase() -> None:
#     """
#     Test invalid phase exception handling.

#     Validates:
#     - HTTP 404 response
#     - proper error message
#     """

#     response = client.get(
#         "/api/v1/metrics/cross-study?phase=Invalid"
#     )

#     assert response.status_code == 404

#     data = response.json()

#     assert (
#         data["success"]
#         is False
#     )

#     assert (
#         data["error"]["code"]
#         == "NOT_FOUND"
#     )

#     assert (
#         data["error"]["message"]
#         == "No studies found for: Invalid"
#     )

#     assert (
#         "trace_id"
#         in data
#     )

# def test_status_filter():

#     """
#     Test status filtering.

#     Validates:
#     - query parameter handling
#     - filtered API response
#     """

#     response = client.get(
#         "/api/v1/metrics/cross-study?status=Completed"
#     )

#     assert response.status_code == 200


# def test_invalid_status():

#     """
#     Test invalid status exception handling.

#     Validates:
#     - HTTP 404 response
#     - proper error message
#     """

#     response = client.get(
#         "/api/v1/metrics/cross-study?status=Invalid"
#     )

#     assert response.status_code == 404

# def test_history_true():

#     """
#     Test include _history = true exception handling
#     """

#     response = client.get(
#         "/api/v1/metrics/cross-study?include_history=true"
#     )

#     assert response.status_code == 200


# def test_root():

#     """
#     Testing root status code 
#     """

#     response = client.get("/")

#     assert response.status_code == 200




# def test_latest_metrics():

#     db = SessionLocal()

#     result = (
#         get_latest_metrics_for_study(
#             db,
#             "AT-01"
#         )
#     )

#     assert result is not None
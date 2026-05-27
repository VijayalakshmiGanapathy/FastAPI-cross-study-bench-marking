"""
Integration tests for FastAPI Cross-Study API.

Purpose:
Validate complete application flow including:
- API endpoint
- database interaction
- CRUD layer
- response schema
"""

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_cross_study_metrics_endpoint():
    """
    Test complete cross-study endpoint flow.

    Validates:
    - endpoint accessibility
    - HTTP status code
    - response structure
    """

    response = client.get(
        "/api/v1/metrics/cross-study"
    )

    assert response.status_code == 200

    data = response.json()

    assert "generated_at" in data
    assert "studies" in data


# def test_phase_filter_integration():
#     """
#     Test phase filtering integration.

#     Validates:
#     - query parameter handling
#     - filtered response generation
#     """

#     response = client.get(
#         "/api/v1/metrics/cross-study?phase=Phase III"
#     )

#     assert response.status_code == 200

#     data = response.json()

#     for study in data["studies"]:

#         assert (
#             study["phase"]
#             == "Phase III"
#         )


# def test_invalid_phase_integration():
#     """
#     Test invalid phase handling.

#     Validates:
#     - exception handling
#     - HTTP 404 response
#     """

#     response = client.get(
#         "/api/v1/metrics/cross-study?phase=InvalidPhase"
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
#         == "No studies found for: InvalidPhase"
#     )

#     assert "trace_id" in data


# def test_include_history_integration():
#     """
#     Test validation history retrieval.

#     Validates:
#     - include_history functionality
#     - nested response structure
#     """

#     response = client.get(
#         "/api/v1/metrics/cross-study?include_history=true"
#     )

#     assert response.status_code == 200

#     data = response.json()

#     assert "studies" in data

#     if data["studies"]:

#         assert (
#             "run_history"
#             in data["studies"][0]
#         )
# This is WiP

# import pytest
# from app import app
# from fastapi.testclient import TestClient


# @pytest.fixture(scope="module")
# def client():
#     client = TestClient(app)
#     client.base_url = "http://127.0.0.1:5000"
#     yield client


# def test_create_question(mocker, client):
#     # Define a mock dataset for testing
#     test_dataset = {
#         "train": [
#             {"line_text": "This is line 1", "speaker": "Jim"},
#             {"line_text": "This is line 2", "speaker": "Dwight"},
#             {"line_text": "This is line 3", "speaker": "Pam"},
#         ]
#     }

#     # Create a mock response object
#     mock_response = mocker.Mock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = {
#         "question": "Which character said the following line: 'This is line 1'?", "options": ["Jim", "Dwight", "Pam"]}

#     # Use the mock response object to replace the actual call to the API
#     mocker.patch("requests.post", return_value=mock_response)

#     # Make a request to the /quiz endpoint with the mock dataset
#     response = client.post('/', json={"train": test_dataset})

#     # assert that the response status code is 200 OK
#     assert response.status_code == 200

#     # assert that the question and answer options are what you expect
#     question_html = response.get_data(as_text=True)
#     assert "Which character said the following line: 'This is line 1'?" in question_html
#     assert "Jim" in question_html
#     assert "Dwight" in question_html
#     assert "Pam" in question_html
#     assert "Michael" not in question_html

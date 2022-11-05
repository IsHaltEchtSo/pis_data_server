"""
This file contains the functional tests for the routes.

These tests use GET methods to different URLs to check proper behavior
"""


class TestIndexView:
    def test_index_view_get(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/index' page is requested (GET)
        THEN check that the response is valid
        """
        response = test_client.get('/index')

        assert response.status_code == 200

    def test_index_view_links(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/index' page is requested (GET)
        THEN check that the links are in place
        """
        response = test_client.get('/index')

        assert b"Log In" in response.data
        assert b"Digitalize" in response.data
        assert b"Search" in response.data
        assert b"Modifications Checklist" in response.data
        assert b"History" in response.data
        assert b"Manual" in response.data


class TestLoginView:
    def test_login_view_get(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/login' page is requested (GET)
        THEN check that the response is valid
        """
        response = test_client.get('/login')

        assert response.status_code == 200

    def test_login_view_links(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/login' page is requested (GET)
        THEN check that the links are in place
        """
        response = test_client.get('/login')

        assert b"Log In" in response.data
        assert b"Email" in response.data
        assert b"Password" in response.data


class TestHistoryView:
    def test_history_view_get(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/history' page is requested (GET)
        THEN check that the response is valid
        """
        response = test_client.get('/history')

        assert response.status_code == 200

    def test_history_view_links(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/history' page is requested (GET)
        THEN check that the links are in place
        """
        response = test_client.get('/history')

        assert b"Some Content for the History" in response.data


class TestManualView:
    def test_manual_view_get(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/manual' page is requested (GET)
        THEN check that the response is valid
        """
        response = test_client.get('/manual')

        assert response.status_code == 200

    def test_manual_view_links(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/manual' page is requested (GET)
        THEN check that the links are in place
        """
        response = test_client.get('/manual')

        assert b"Some Content for the Manual" in response.data


class TestZettelSearchView:
    def test_zettel_search_view_get(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/zettel_search' page is requested (GET)
        THEN check that the response is valid
        """
        response = test_client.get('/zettel_search')

        assert response.status_code == 200

    def test_zettel_search_view_links(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/zettel_search' page is requested (GET)
        THEN check that the links are in place
        """
        response = test_client.get('/zettel_search')

        assert b"Zettel" in response.data
        

class TestZettelView:
    def test_zettel_view_get(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/zettel' page is requested (GET)
        THEN check that the response is valid
        """
        response = test_client.get('/zettel')

        assert response.status_code == 200
        
    def test_zettel_view_links(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/zettel' page is requested (GET)
        THEN check that the links are in place
        """
        response = test_client.get('/zettel')

        assert b"Edit" in response.data
        assert b"Delete" in response.data


class TestZettelEditView:
    def test_zettel_edit_view_get(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/zettel_edit' page is requested (GET)
        THEN check that the response is valid
        """
        response = test_client.get('/zettel_edit')

        assert response.status_code == 200

    def test_zettel_edit_view_links(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/zettel_edit' page is requested (GET)
        THEN check that the links are in place
        """
        response = test_client.get('/zettel_edit')

        assert b"Success" in response.data
        

class TestChecklistView:
    def test_checklist_view_get(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/checklist' page is requested (GET)
        THEN check that the response is valid
        """
        response = test_client.get('/checklist')

        assert response.status_code == 200

    def test_checklist_view_links(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/checklist' page is requested (GET)
        THEN check that the links are in place
        """
        response = test_client.get('/checklist')

        assert b"Some Content for the Checklist" in response.data
        

class TestDigitalizeZettelView:
    def test_digitalize_zettel_view_get(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/digitalize_zettel' page is requested (GET)
        THEN check that the response is valid
        """
        response = test_client.get('/digitalize_zettel')

        assert response.status_code == 200

    def test_digitalize_zettel_view_links(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/digitalize_zettel' page is requested (GET)
        THEN check that the links are in place
        """
        response = test_client.get('/digitalize_zettel')

        assert b"Label Zettel" in response.data


class TestLabelZettelView:
    def test_label_zettel_view_get(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/label_zettel' page is requested (GET)
        THEN check that the response is valid
        """
        response = test_client.get('/label_zettel')

        assert response.status_code == 200

    def test_label_zettel_view_links(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/label_zettel' page is requested (GET)
        THEN check that the links are in place
        """
        response = test_client.get('/label_zettel')

        assert b"Success" in response.data
        

class TestSuccessView:
    def test_success_view_get(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/success' page is requested (GET)
        THEN check that the response is valid
        """
        response = test_client.get('/success')

        assert response.status_code == 200
        
    def test_success_view_links(self, test_client):
        """
        GIVEN a Flask Testing Application
        WHEN the '/success' page is requested (GET)
        THEN check that the links are in place
        """
        response = test_client.get('/success')

        assert b"Home" in response.data
import json
from unittest import TestCase
from app import create_app
from db import db, Films

app = create_app('TEST')


class TestFilms(TestCase):
    def setUp(self) -> None:
        self.app_context = app.app_context()
        self.app_context.push()

        db.create_all()

    def tearDown(self) -> None:
        db.drop_all()
        db.session.commit()

    def test_films(self):
        resp = app.test_client().get('films')
        actual_resp = [{"id": 1, "name": "The Shawshank Redemption"}]
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json, actual_resp)

    def test_post_films(self):
        expected_result = [{"id": 1, "name": "The Shawshank Redenption"},
                           {"id": 2, "name": "Joker"}]
        data = json.dumps({"name": "Joker"})
        resp = app.test_client().post('/films', data=data, content_type="application/json")
        self.assertEqual(resp.json, expected_result)

    def test_update_films(self):
        expected_result = [{"id": 1, "name": "Avengers"}]
        data = json.dumps({"name": "Avengers"})
        resp = app.test_client().put('/films/1', data=data, content_type="application/json")

        self.assertEquals(resp.json, expected_result, 200)
        self.assertEquals(resp.json, expected_result)

    def test_delete_films(self):
        expected_result = []
        
        resp = app.test_client().delete('/films/1')


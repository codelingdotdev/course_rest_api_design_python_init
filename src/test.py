from django.test import TestCase
from ninja.testing import TestClient
from api.endpoints.barks import router as barks_router


class TestBarking(TestCase):
    def setUp(self):
        self.client = TestClient(router_or_app=barks_router)

    def test_web_home(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [
                {"id": 1, "message": "bark one!"},
                {"id": 2, "message": "bark two!"},
                {"id": 3, "message": "bark three!"},
            ],
            (
                "\n\nExpected response to be a list of barks like this:\n"
                "[{'id':1, 'message': 'bark one!'}, {'id':2, 'message': 'bark two!'}, {'id':3, 'message': 'bark three!'}]"
            ),
        )

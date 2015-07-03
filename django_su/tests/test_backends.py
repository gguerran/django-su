from django.contrib.auth import get_user_model
from django.test import TestCase


class TestSuBackend(TestCase):

    def setUp(self):
        super(TestSuBackend, self).setUp()
        from django_su.backends import SuBackend
        self.user = get_user_model().objects.create(username='testuser')
        self.backend = SuBackend()

    def test_authenticate_do_it(self):
        """Ensure authentication passes when su=True and user id is valid"""
        self.assertEqual(
            self.backend.authenticate(su=True, pk=self.user.pk),
            self.user
        )

    def test_authenticate_dont_do_it(self):
        """Ensure authentication fails when su=False and user id is valid"""
        self.assertEqual(
            self.backend.authenticate(su=False, pk=self.user.pk),
            None
        )

    def test_authenticate_id_none(self):
        """Ensure authentication fails when user_id is None"""
        self.assertEqual(
            self.backend.authenticate(su=True, pk=None),
            None
        )

    def test_authenticate_id_non_existent(self):
        """Ensure authentication fails when user_id doesn't exist"""
        self.assertEqual(
            self.backend.authenticate(su=True, pk=999),
            None
        )

    def test_authenticate_id_invalid(self):
        """Ensure authentication fails when user_id is invalid"""
        self.assertEqual(
            self.backend.authenticate(su=True, pk='abc'),
            None
        )

    def test_get_user_exists(self):
        """Ensure get_user returns the expected user"""
        self.assertEqual(
            self.backend.get_user(pk=self.user.pk),
            self.user
        )

    def test_get_user_does_not_exist(self):
        """Ensure get_user returns None if user is not found"""
        self.assertEqual(
            self.backend.get_user(pk=999),
            None
        )

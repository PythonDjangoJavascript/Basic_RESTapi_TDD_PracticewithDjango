from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):
    """Test admin page funcitons and page code"""

    def setUp(self):
        """It will be availabel in every test case"""

        self.client = Client()  # This will allow client access from anywhre
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@email.com",
            name="naem",
            password="password123"
        )

        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="user@email.com",
            name="Test User",
            password="TestUserPass"
        )

    def test_user_listed(self):
        """This method tests user list is available on admin page"""

        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_edit_page(self):
        """Test if user informationd admin edit page is working"""

        # This args return id and added at the end of the url
        # ie. /admin/core/user/(user id)
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_user_create_page(self):
        """Test user craet admin page  workds"""

        url = reverse("admin:core_user_add")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

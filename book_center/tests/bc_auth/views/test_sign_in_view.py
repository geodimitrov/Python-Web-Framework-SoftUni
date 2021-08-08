from tests.core.test_cases import BookCenterTestCase
from django.urls import reverse


class SignInViewTests(BookCenterTestCase):
    def test_sign_in_view_when_user_is_not_verified__expect_email_verification(self):
        expected_url = reverse('verify email additional', args=[self.user.id])
        response = self.client.post(reverse('sign in'), {
            'username': self.username,
            'password': self.user_password,
            }
        )

        self.assertRedirects(response, expected_url)

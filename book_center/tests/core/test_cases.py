from book_center.bc_profiles.models.discussions import BookCenterDiscussion, \
    BookCenterDiscussionComment
from book_center.bc_profiles.models.profiles import BookCenterUserProfile
from book_center.bc_auth.models import BookCenterUser
from book_center.bc_events.models import BookCenterEvent
from book_center.bc_blog.models import BookCenterBlogPostAuthor
from book_center.bc_contact.models import BookCenterContactFormModel
from django.test import TestCase, Client


class BookCenterTestCase(TestCase):
    username = 'geo55'
    user_email = 'geo@gdv.abv'
    user_password = 'KsijdyY^sd'

    def setUp(self):
        self.client = Client()
        self.user = BookCenterUser.objects.create_user(
            username=self.username,
            email=self.user_email,
            password=self.user_password,
            is_verified=False,
        )
        self.contact_form = BookCenterContactFormModel(
            subject='My subject',
            email='geo@yahoo.com',
            message='I want to tell you something',
        )
        self.blog_post_author = BookCenterBlogPostAuthor(
            first_name='Georgi',
            last_name='Di',
        )
        self.event = BookCenterEvent(
            title='White Fang',
            description='This is our book of the month',
            category='Cool Category',
        )
        self.discussion = BookCenterDiscussion(
            title='Just a discussion',
            description='This is our discussion',
            topic='Life',
        )
        self.discussion_comment = BookCenterDiscussionComment(
            comment='My comment'
        )
        self.profile = BookCenterUserProfile(
            first_name='Georgi',
            last_name='Di',
            bio='My short bio',
            city='Sofia',
        )
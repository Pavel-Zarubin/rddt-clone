from django.test import TestCase
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth.models import User


#Models

    #Post
class TestPost(TestCase):
    def create_post(self):
        author = User.objects.create_user('test_user')
        return Post.objects.create(title='test_title', content='test content', date_posted=timezone.now(), author=author)

    def test_post_creation(self):
        p = self.create_post()
        self.assertTrue(isinstance(p, Post))
        self.assertEqual(p.__str__(), p.title)

    def test_get_absolute_url(self):
        author = User.objects.create_user('test_user')
        post = Post.objects.create(title='test title', author=author, content='test content', date_posted=timezone.now())
        self.assertIsNotNone(post.get_absolute_url())


    #Comment
class TestComment(TestCase):
    def create_comment(self):
        author = User.objects.create_user('second_test_user')
        return Comment.objects.create(author=author, post_id=1, content='test_comment_content', date_posted=timezone.now())

    def test_comment_creation(self):
        c = self.create_comment()
        self.assertTrue(isinstance(c, Comment))
        self.assertEqual(c.__str__(), c.content)






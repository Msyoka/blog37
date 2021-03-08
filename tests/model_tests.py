import unittest
from app.models import User,Post,Comment,Subscriber
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'galaano')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('galaano'))

class PostTest(unittest.TestCase):
    def setUp(self):
        self.user_Galaano = User(id=1,username = 'galaano',password = 'galaano', email = 'sgalaano@gmail.com')
        self.new_post = Post(id=5,post='Blog Post for days',posted="2018-09-12")

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.id,5)
        self.assertEquals(self.new_post.post,'Blog Post for days')
        self.assertEquals(self.new_post.posted,"2018-09-12")

    def test_save_review(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)

    def test_get_review_by_id(self):
        self.new_posts.save_post()
        got_posts = Post.get_posts(12345)
        self.assertTrue(len(got_posts) == 1)
import unittest
from blog import BlogManagementSystem

class TestBlogManagementSystem(unittest.TestCase):
    def setUp(self):
        self.blog_system = BlogManagementSystem()
        self.blog_system.create_post("Python Basics", "This is an introduction to Python programming.", "John Doe", "Technology")
        self.blog_system.create_post("Web Development", "Creating websites with HTML, CSS, and JavaScript.", "Eva Brown", "Technology")
        #print('\n\nposts:\n',self.blog_system.posts)

    def test_create_post(self):
        self.assertEqual(len(self.blog_system.posts), 2)
    
    def test_edit_post(self):
        self.blog_system.edit_post(1, title="Updated Title", content="Updated Content", category="Updated Category")
        updated_post = self.blog_system.get_post_by_id(1)
        self.assertEqual(updated_post['title'], "Updated Title")
        self.assertEqual(updated_post['content'], "Updated Content")
        self.assertEqual(updated_post['category'], "Updated Category")

    def test_delete_post(self):
        self.blog_system.delete_post(1)
        self.assertEqual(len(self.blog_system.posts), 1)

    def test_categorize_post(self):
        self.blog_system.categorize_post(1, "Programming")
        categorized_post = self.blog_system.get_post_by_id(1)
        self.assertEqual(categorized_post['category'], "Programming")

    def test_search_posts_by_keyword(self):
        self.blog_system.create_post("Python Advanced", "Advanced Python programming topics.", "Alice Smith", "Technology")
        self.blog_system.create_post("Traveling to Rome", "Exploring the beautiful city of Rome.", "Bob Johnson", "Travel")
        results = self.blog_system.search_posts_by_keyword("Python")
        self.assertEqual(len(results), 2)

    def test_allow_comment(self):
        self.blog_system.allow_comment(1, "Jane", "Great post!")
        post = self.blog_system.get_post_by_id(1)
        #print('\npost:', post,'\n')
        self.assertEqual(len(post['comments']), 1)
    
    def test_manage_user_account(self):
        self.blog_system.manage_user_account("user1", "user1@example.com", "password123")
        self.assertTrue("user1" in self.blog_system.users)
    
    def test_schedule_post_publishing(self):
        self.blog_system.schedule_post_publishing(1, "2023-01-01 12:00:00")
        self.assertEqual(len(self.blog_system.scheduled_posts), 1)

    def test_track_post_views(self):
        self.blog_system.track_post_views(1)
        self.assertEqual(self.blog_system.post_views[1], 1)

    def test_get_most_viewed_posts(self):
        self.blog_system.create_post("Web Development", "Creating websites with HTML, CSS, and JavaScript.", "Eva Brown", "Technology")
        self.blog_system.track_post_views(1)
        self.blog_system.track_post_views(2)
        self.blog_system.track_post_views(3)
        most_viewed = self.blog_system.get_most_viewed_posts(2)
        self.assertEqual(len(most_viewed), 2)

if __name__ == '__main__':
    unittest.main()

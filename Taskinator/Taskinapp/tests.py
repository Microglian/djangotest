from django.test import TestCase
from django.urls import reverse
from .models import Task, User
import datetime

class TestTask(TestCase):
    def setUp(self):
        # Create test user
        user = User.objects.create(name="Tester")
        # Create testing task
        Task.objects.create(title="Test Task", body="Example Body Text", due_date="2012-12-12 12:12:12", author=user)
    
    # Test Task Creation
    def test_task_create(self):
        # Check test task has correct information
        self.assertEqual(Task.objects.get(id=1).title, "Test Task")
        self.assertEqual(Task.objects.get(id=1).body, "Example Body Text")
        test_date = datetime.datetime(2012, 12, 12, 12, 12, 12, tzinfo=datetime.timezone.utc)
        self.assertEqual(Task.objects.get(id=1).due_date, test_date)
        self.assertEqual(Task.objects.get(id=1).author, User.objects.get(id=1))
    
    # Test Task Read, covers list and details
    def test_task_read(self):
        # Get the task list view
        response = self.client.get(reverse("task_list"))
        # Check the task list view contains the task.
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
        self.assertContains(response, "Example Body Text")
        # Get the task details view
        response = self.client.get(reverse("task_details", kwargs={"pk": "1"}))
        # Check the task list view contains the task.
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
        self.assertContains(response, "Example Body Text")
    
    # Test Task Update
    def test_task_update(self):
        # Update the test task
        Task.objects.filter(id=1).update(title="Updated Task", body="Updated Body Text", due_date="2011-11-11 11:11:11")
        # Check task is updated.
        self.assertEqual(Task.objects.get(id=1).title, "Updated Task")
        self.assertEqual(Task.objects.get(id=1).body, "Updated Body Text")
        test_date = datetime.datetime(2011, 11, 11, 11, 11, 11, tzinfo=datetime.timezone.utc)
        self.assertEqual(Task.objects.get(id=1).due_date, test_date)
    
    # Test Task Delete
    def test_task_delete(self):
        # Delete the test task
        Task.objects.filter(id=1).delete()
        # Check that there are no more than 0 objects with ID 1.
        self.assertFalse(Task.objects.filter(id=1))
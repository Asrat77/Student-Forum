from django.test import TestCase
from base.models import Topic , Room, Message
from django.contrib.auth.models import User

class ModelTestCase(TestCase):

# For avoiding code repition we can use setUp mthod that can contain all our variables
# but since it reapeats functions it might create double databases we dont rly need
# so we can use cls synatx with @classmethod form to avoid database duplication


    @classmethod
    def setUpTestData(cls):
        #print("db test")
        testuser = User.objects.create_user(
            username='testuser', password='12345')
        testuser2 = User.objects.create_user(
            username='myuser', password='246810')
        cls.name = Room.objects.create(
            name="Django", description="New description")
        cls.name.participants.set([testuser.pk, testuser2.pk])


#Testing the string method inside the Topic method we have in models.py

#Given name of a topic, when i click on the topic , then display the chat room for that specific topic.
    def test_string_method(self):
        self.assertEqual(str(self.name), "Django")

#Testing the string method inside the Room method we have in models.py

#Given question label, when i click on the question , i want to see the description of the question label.
    def test_string_method_for_room(self):
        description = "Description format"
        self.assertEqual(str(self.name), "Django")
        self.assertEqual(str(description), "Description format")
    
#Testing for Many to Many field like participants in our case of show

#Given participants, when i send a message in a room then update the participant with the user sending the message.
    def test_room_like_participants(self):
        self.assertEqual(self.name.participants.count(), 2)
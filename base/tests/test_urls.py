from django.test import SimpleTestCase
from django.test import TestCase
from django.contrib.auth.models import User
from base.models import Room, Message
from django.urls import resolve, reverse
from base.views import home, loginpage, logoutUser, registerPage, room, userProfile, createRoom, updateRoom, deleteRoom, deleteMessage, updateUser, topicsPage


class TestUrls(SimpleTestCase):

    # Given login path, when i click on login then take me to login page

    def test_list_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginpage)

# Given logout path, when i click on logout then logout the user
    def test_list_url_is_resolved_logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

# Given home path, when i click on home then take me to login page
    def test_list_url_is_resolved_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

# Given create room button, when i click on that button then create my question label
    def test_list_url_is_resolved_create_room(self):
        url = reverse('create-room')
        self.assertEquals(resolve(url).func, createRoom)

# Given edit icon, when i click on the icon then update the user accordingly
    def test_list_url_is_resolved_update_user(self):
        url = reverse('update-user')
        self.assertEquals(resolve(url).func, updateUser)

# Given More button, when i click on the button then take me to topic page to browse topics
    def test_list_url_is_resolved_topics(self):
        url = reverse('topics')
        self.assertEquals(resolve(url).func, topicsPage)

    # Since the room, user profile, update room, delete rooom and delete function has primary key
    # and use ID we can not test by the above methods but we can test it accordingly

    # def test_list_url_is_resolved_room(self):
    #    url = reverse('room', args=[room.pk])
    #    self.assertEquals(resolve(url).func, room)
    #
    # def test_list_url_is_resolved_user_profile(self):
    #    url = reverse('user-profile')
    #    self.assertEquals(resolve(url).func, userProfile)

    # def test_list_url_is_resolved_update_room(self):
    #    url = reverse('update-room')
    #    self.assertEquals(resolve(url).func, updateRoom)

    # def test_list_url_is_resolved_delete_room(self):
    #    url = reverse('delete-room')
    #    self.assertEquals(resolve(url).func, deleteRoom)

    # def test_list_url_is_resolved_delete_message(self):
    #    url = reverse('delete-message')
    #    self.assertEquals(resolve(url).func, deleteMessage)

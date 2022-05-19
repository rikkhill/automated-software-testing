from unittest import TestCase

from sut.dog import Dog


class TestDog(TestCase):

    def setUp(self):
        self.dog = Dog()

    def test_dog_is_happier_after_playing(self):
        
        # Given...
        initial_happiness = self.dog.happiness

        # When...
        self.dog.play()

        # Then...
        self.assertGreater(self.dog.happiness, initial_happiness)
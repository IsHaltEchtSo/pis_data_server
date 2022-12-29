from auth_feature.models import User

class TestUser:
    def test_new_user(self):
        """
        GIVEN an User Model
        WHEN an User object is instantiated
        THEN check 'name' is defined correctly 
        """
        user = User(name='max mustermann', email='max.mustermann@gmail.com')
        assert user.name == 'max mustermann'
        assert user.email == 'max.mustermann@gmail.com'
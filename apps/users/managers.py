from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    """
    Manager class that allows the creation of a custom user
    """

    def _create_user(self, email, first_name, last_name, password, is_staff, is_superuser, **extra_fields):
        """
        Private method that handles the creation of a user in general
        """

        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        """
        Method that creates a user that is not a staff
        """
        return self._create_user(email, first_name, last_name, password, False, False, **extra_fields)
    

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        """
        Method that creates a superuser
        """
        return self._create_user(email, first_name, last_name, password, True, True, **extra_fields)
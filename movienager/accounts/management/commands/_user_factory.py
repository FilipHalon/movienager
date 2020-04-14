# import factory  

# from accounts.models import User

# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User

#     first_name = factory.Faker('first_name'),
#     last_name = factory.Faker('last_name'),
#     email = factory.Faker('email'),
#     username = factory.Faker('word'),
#     password = "fakepassword"

from faker import Faker

from accounts.models import User

fake = Faker()

def create_user():
    User.objects.create_user(
        email = fake.email(),
        username = fake.word(),
        password = 'fakepassword',
        first_name = fake.first_name(),
        last_name = fake.last_name()
    )

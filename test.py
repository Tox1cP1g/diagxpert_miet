from hello.models import CustomUser

user = CustomUser(login='testuser', password='testpassword')
user.save()
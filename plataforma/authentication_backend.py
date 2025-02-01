from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        
        try:
            # Intenta autenticar por correo
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            # Si falla, intenta por username
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None
        
        if user.check_password(password):
            return user
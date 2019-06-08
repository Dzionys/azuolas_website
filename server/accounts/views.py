from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

# class LoginView(APIView):
#     template_name = 'warehouse/login.html'

#     def post(self, request):
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('/warehouse')
#         else:
#             return redirect('/')

class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
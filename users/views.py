from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# def register(request):
#     form = UserCreationForm()
#     return render(request, 'users/regisration.html', {'form':form, 'title': 'Регистарция ползователя'})

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import User
from .serializers import LoginSerializer
from .serializers import RegistrationSerializer

class RegistrationAPIView(APIView):
    """
    Registers a new user.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Creates a new User object.
        Username, email, and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return HttpResponse('Authenticated successfully') 
        # return Response(
        #     {
        #         'token': serializer.data.get('token', None),
        #     },
        #     status=status.HTTP_201_CREATED,
        # )
    def get(self,request):
        return render(request, 'users/registration.html')  

from django.contrib.auth import authenticate, logout, login

class LoginAPIView(APIView):
    """
    Logs in an existing user.
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Checks is user exists.
        Email and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)


        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(username=email, password=password)
        login(request, user)

        
        return render(request, 'pages/main.html')  
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self,request):
        return render(request, 'users/login.html')


from .serializers import LogoutSerializer
from django.contrib.auth import logout
class LogoutAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LogoutSerializer
    def post(self, request):
        # serializer = self.serializer_class(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # return render(request, 'pages/main.html')  
        
        logout(request)
        # try:
        #     request.user.auth_token.delete()
        # except (AttributeError, ObjectDoesNotExist):
        #     pass
        # django_logout(request)
        return render(request, 'users/login.html')
    def get(self,request):
        logout(request)
        return render(request, 'users/login.html')



# from django.contrib.auth.decorators import login_required

# @login_required
# def dashboard(request):
#     return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    return render(request, 'users/login.html')
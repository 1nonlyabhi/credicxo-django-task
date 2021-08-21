from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.db.models import Q
from .serializers import GroupUserSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

# Sign Up API to register a normal user who doesn't belong to any group
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# Defined 3 user levels: 1. Super-admin, 2. Teacher, 3. Student (By using internal Django Groups)
# View to add/list groups' user

class UserAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = None

    # POST request to add the new user to the database
    # Student (Group no 3) is unable to add anyone to the database
    # Teacher (Group no 2) is able to add Students to the database
    # Super-admin (Group no 1) is able to add anyone to the database
    def post(self, request):
        try:
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name # requesting user's group name
                condition01 = (group == "Super-admin")
                condition02 = ((group == "Teacher") and (request.data['groups']==[3]))
                if condition01 or condition02:
                    user = request.data
                    # encrypting password with sha_256 algorithm
                    user['password'] = make_password(user['password'])
                    serializer = GroupUserSerializer(data=user)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    err_message = {'status': 401, 'err_message': "user can't add user to same level"}
                    return Response(status=status.HTTP_401_UNAUTHORIZED, data=err_message)
            else:
                err_message = {'status': 401, 'err_message': "user has no admin/super user role assigned."}
                return Response(status=status.HTTP_401_UNAUTHORIZED, data=err_message)
        except Exception as ex:
            return Response(ex.args, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

    # GET request to list users
    # Student (Group no 3) is able to list his information from the database
    # Teacher (Group no 2) is able to list Students' information from the database
    # Super-admin (Group no 1) is able to list anyone's information from the database
    def get(self, request):

        try:
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == "Super-admin":
                    users = User.objects.filter(Q(groups=1) | Q(groups=2) | Q(groups=3)) # Filter every user belongs to all three groups
                    serializer = GroupUserSerializer(users, many=True)
                elif group == "Teacher":
                    users = User.objects.filter(groups=3) # Filter user belogs to Students' group
                    serializer = GroupUserSerializer(users, many=True)
                elif group == "Student":
                    users = User.objects.get(id=request.user.id)
                    serializer = GroupUserSerializer(users)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)

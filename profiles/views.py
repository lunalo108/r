from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import render
from .models import Profile
# from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer


class ProfileRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    # renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            # We use the `select_related` method to avoid making unnecessary
            # database calls.
            profile = Profile.objects.select_related('user').get(
                user__username=request.data.get('username', None)
            )
        except Profile.DoesNotExist:
            raise

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def get(self,request):
    #     return render(request, 'profiles/edit_profile.html')  
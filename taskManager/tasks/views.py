import os  # Environment variable access
from dotenv import load_dotenv  # For loading .env variables
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .models import Task, Invite
from .serializers import TaskSerializer


load_dotenv()

def invite_user(request):
    if request.method == "POST" and request.user.is_superuser:
        email = request.POST.get('email')
        if not email:
            return render(request, 'invite.html', {'error': 'Email is required'})
        
        # Generate an invite token
        token = get_random_string(length=32)
        invite = Invite.objects.create(email=email, token=token, invited_by=request.user)
        
        # Send an email with the registration link
        registration_link = request.build_absolute_uri(reverse('register')) + f"?token={token}"
        message = Mail(
            # from_email="khanimran822002@gmail.com",
            from_email=os.environ.get("EMAIL_HOST_USER"),
            to_emails=email,
            subject='You are invited to join Task Manager',
            html_content=f'<strong>Use the below link for registering to task manager<br/>{registration_link}</strong>')
        try:
            sgapi = os.environ.get('EMAIL_API')
            sg = SendGridAPIClient(sgapi)
            # sg = SendGridAPIClient('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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
        return render(request, 'invite.html', {'success': 'Invitation sent!'})

    return render(request, 'invite.html')


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Task updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



def register_with_invite(request):
    token = request.GET.get('token')
    invite = get_object_or_404(Invite, token=token)

    if invite.is_expired():
        return render(request, 'expired_invite.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=invite.email, password=password)
        invite.delete()  # Delete the invite after successful registration
        return redirect('login')

    return render(request, 'register_with_invite.html', {'email': invite.email})

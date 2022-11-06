from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import constants as messages
from django.contrib.auth.hashers import check_password
from .models import Immobilier, Appart, Ville

User = get_user_model()


    



from django.shortcuts import render, redirect
from .forms import DiseaseForm,UserForm
import joblib
import pickle
from django.contrib import messages
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report,roc_auc_score
from sklearn.svm import SVC
import numpy as np
import pandas as pd
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from sklearn.model_selection import train_test_split
from django.contrib.auth.forms import UserCreationForm
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from .models import Comment
# Create your views here.

df_s = pd.read_csv('C:/Users/Utilisateur/Desktop/Dataset/input/Symptom-severity.csv')
df_s['Symptom']=df_s['Symptom'].str.replace('_',' ')
df_s['Symptom'].unique()
filename='./MLapp/PredictionModel.sav'
loaded_model = joblib.load(filename)

def predict(s1='vomiting',s2='vomiting',s3='vomiting',s4='vomiting',s5='vomiting',s6='vomiting',s7='vomiting'):
    l = [s1,s2,s3,s4,s5,s6,s7]
    print(l)
   
    
    x= np.array(df_s['Symptom'])
    y= np.array(df_s['weight'])
    for i in range(len(l)):
        for j in range(len(x)):
            if l[i]==x[j]:
                l[i]=y[j]
    res = [l]
    pred = loaded_model.predict(res)
    return pred[0]

def prediction(request):
   
    if request.method == 'POST':
        symptom1=request.POST.get('symptom1')
        symptom2=request.POST.get('symptom2')
        symptom3=request.POST.get('symptom3')
        symptom4=request.POST.get('symptom4')
        symptom5=request.POST.get('symptom4')
        symptom6=request.POST.get('symptom6')
        symptom7=request.POST.get('symptom7')
        print(symptom1,symptom2,symptom3,)
        pred = predict(symptom1, symptom2, symptom3,symptom4,symptom5,symptom6,symptom7)
        context={'prediction':pred}
        return render(request, 'MLapp/prediction.html',context)



def home(request):
    page='home'
    users=User.objects.all()
    pred=''
    form = DiseaseForm
    comments=Comment.objects.all()
    if request.method == 'POST':
        body=request.POST.get('body')
        comment=Comment.objects.create(
            user = request.user,
            body = body,
        )
        
        
    
        

    context={'form': form,'users':users,'comments':comments}
    return render(request, 'MLapp/Mhome.html',context)


def loginUser(request):
    form=UserCreationForm
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'User OR Password does not exist.')

    context={'form': form}
    return render(request, 'MLapp/signinUser.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form = UserCreationForm;
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:

            messages.error(request,"an error happened during registration")

    return render(request,"MLapp/signupUser.html",{'form': form})


def about(request):
    return render(request,"MLapp/about.html")



def contact(request):
    return render(request,"MLapp/contact.html")


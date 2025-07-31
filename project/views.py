from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Project
from .forms import ProjectForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request,'project/home.html')

@login_required
def currentprojects(request):
	projects = Project.objects.filter(user = request.user)
	return render(request,'project/currentprojects.html',{'projects':projects})

@login_required
def completeprojects(request):
	projects = Project.objects.filter(user = request.user, datecompleted__isnull = False).order_by('-datecompleted')
	return render(request,'project/completeprojects.html',{'projects':projects})


@login_required
def createproject(request):
	if request.method == 'GET':
		return render(request,'project/createproject.html',{'form':ProjectForm})
	else :
		form = ProjectForm(request.POST)
		newproject = form.save(commit = False)
		newproject.user = request.user
		newproject.save()
		return redirect('currentprojects')


def signupuser(request):
	if request.method == 'GET':
		return render(request,'project/signup.html',{'form':UserCreationForm()})
	else:
		if request.POST['password1'] == request.POST['password2']:
			user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
			user.save()
			login(request,user)
			return redirect('currentprojects')
		else :
			return render(request,'project/signup.html',{'form':UserCreationForm(),'error':'Passwords dont match'})



def loginuser(request):
	if request.method == 'GET':
		return render(request,'project/login.html',{'form':AuthenticationForm()})

	else:
		user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
		if user is None:
			return render(request,'project/login.html',{'form':AuthenticationForm(),'error':'Username or password wrong'})
		else :
			login(request,user)
			return redirect('currentprojects')

@login_required
def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')
	else :
		return redirect('currentprojects')

@login_required
def viewproject(request, project_pk):
	project = get_object_or_404(Project,pk = project_pk, user = request.user)
	if request.method == 'GET':
		form = ProjectForm(instance = project)
		return render(request,'project/viewproject.html',{'error':"Project with this id doesn't exist",'project':project,'form':form})
	else:
		form = ProjectForm(request.POST, instance=project)
		form.save()
		return redirect('currentprojects')

@login_required
def deleteproject(request, project_pk):
	project = get_object_or_404(Project, pk = project_pk, user = request.user)
	if request.method == 'GET':
		return redirect('viewproject')
	else:
		project.delete()
		return redirect('currentprojects')

@login_required
def completeproject(request, project_pk):
	project = get_object_or_404(Project, pk = project_pk, user = request.user)
	if request.method == 'POST':
		project.datecompleted = timezone.now()
		project.save()
		return redirect('currentprojects')
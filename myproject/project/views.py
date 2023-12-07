from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Aplication, Category
from .forms import RegisterUserForm, CreateAplForm


def index(request):
    counter = Aplication.objects.filter(status='new').all().count()
    done = Aplication.objects.filter(status='done').order_by('-date')[:4]
    return render(request, 'main/index.html', {'done': done, 'counter': counter})


class BBLoginView(LoginView):
    template_name = 'registration/login.html'


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

# def register(request):
#     from = RegisterUserForm()
#     return render(request, 'registration/register.html', {'form': form})


@login_required
def createapl(request):
    if request.method == 'POST':
        form = CreateAplForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = request.user.pk
            form.save()
            return redirect('profile')
    else:
        form = CreateAplForm(initial={'author': request.user})
    context = {'form': form}
    return render(request, 'main/create_aplication.html', context)


@login_required
def profile(request):
    return render(request, 'main/profile.html')


@login_required
def processingapl(request, id):
    apl = Aplication.objects.filter(id=id).get()
    if apl:
        apl.status = "received"
        apl.save()
    return redirect('apl_admin_render')

@login_required
def doneapl(request, id):
    apl = Aplication.objects.filter(id=id).get()
    if apl:
        apl.status = "done"
        apl.save()
    return redirect('apl_admin_done')




@login_required
def delete(request, id):
    apl = Aplication.objects.filter(id=id).get()
    if apl:
        apl.delete()
    return redirect('profile')



@login_required
def aplication_render(request):
    apl_items = request.user.aplication_set.all().order_by('-date')
    return render(request, 'main/profile.html', context={'apl_items': apl_items})

@login_required
def apl_admin_render(request):
    all = Aplication.objects.filter(status='new').all()
    return render(request, 'main/adapl.html', context={'all': all})


@login_required
def apl_admin_done(request):
    all = Aplication.objects.filter(status='received').all()
    return render(request, 'main/done_apl.html', context={'all': all})


def apl_filter(request, status):
    apl_items = request.user.aplication_set.all().filter(status=status).order_by('-date')
    return render(request, 'main/profile.html', context={'apl_items': apl_items, 'status': status})

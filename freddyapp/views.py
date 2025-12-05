from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from freddyapp.forms import AnimatronicForm
from freddyapp.models import Animatronic

# Create your views here.
def animatronic_list(request):
    animatronics = Animatronic.objects.all()
    return render(request, 'freddyapp/list.html', {'animatronics': animatronics})

@login_required
@permission_required('freddyapp.add_animatronic', raise_exception=True)
def animatronic_new(request):
    if request.method == 'POST':
        form = AnimatronicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animatronic_list')
    else:
        form = AnimatronicForm()
    return render(request, 'freddyapp/form.html', {'form': form})

@login_required
def animatronic_view(request, id):
    animatronic = get_object_or_404(Animatronic, pk=id)
    return render(request, 'freddyapp/view.html', {'animatronic': animatronic})

class AnimatronicUpdate(PermissionRequiredMixin, UpdateView):
    model = Animatronic
    form_class = AnimatronicForm
    template_name ='freddyapp/form.html'
    permission_required = 'freddyapp.change_animatronic'
    success_url = reverse_lazy('animatronic_list')

class AnimatronicDelete(PermissionRequiredMixin, DeleteView):
    model = Animatronic
    template_name = 'freddyapp/confirm_delete.html'
    permission_required = 'freddyapp.delete_animatronic'
    success_url = reverse_lazy('animatronic_list')

def newuser(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.groups.add(Group.objects.get(name='Client'))
        return redirect('login')
    return render(request, 'freddyapp/form.html', {'form': form})

def theme(request):
    url_anterior = request.META.get('HTTP_REFERER', '/')
    resp = redirect(url_anterior)
    resp.set_cookie('theme', 'dark')
    return resp

def clearcookies(request):
    url_anterior = request.META.get('HTTP_REFERER', '/')
    resp = redirect(url_anterior)
    resp.delete_cookie('theme')
    return resp
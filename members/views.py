from django.shortcuts import render,redirect, get_object_or_404
from .models import player
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from .serializers import PlayerSerializer

@login_required
def player_list(request):
    players = player.objects.all()
    return render(request, 'members/members_list.html', {'players':players})

@login_required
def player_create(request):
    if request.method == 'POST':
        name = request.POST['player_name']
        age = request.POST['player_age']
        number = request.POST['player_number']
        player.objects.create(player_name=name, player_age=age, player_number=number)
        return redirect('player_list')
    return render(request, 'members/member_form.html')

@login_required
def player_update(request, pk):
    player_obj = get_object_or_404(player,pk=pk)
    if request.method=='POST':
        player_obj.player_name = request.POST['player_name']
        player_obj.player_age = request.POST['player_age']
        player_obj.player_number = request.POST['player_number']
        player_obj.save()
        return redirect('player_list')
    return render(request, 'members/member_form.html',{'player':player_obj})

@login_required
def player_delete(request, pk):
    player_obj = get_object_or_404(player, pk=pk)
    player_obj.delete()
    return redirect('player_list')


def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form':form})


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = player.objects.all()
    serializer_class = PlayerSerializer
# Create your views here.

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionsRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from group.models import Group

# Create your views here.

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Group


class GroupDetail(generic.DetailView):
    model = Group


class ListGroups(generic.ListView):
    model = Group
 
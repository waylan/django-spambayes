from django.contrib import admin
from django.contrib.contenttypes import generic

from statusbayes.models import SpamStatus

class SpamStatusInline(generic.GenericTabularInline):
    model = SpamStatus

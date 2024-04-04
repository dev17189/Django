from django.contrib import admin
from htmlwebsite.models import *
# Register your models here.
 
admin.site.register(Contact)
admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(Vote)


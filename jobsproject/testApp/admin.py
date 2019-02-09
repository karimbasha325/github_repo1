from django.contrib import admin
from testApp.models import Hydjobs, Chennaijobs,Blorejobs,Kochijobs

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class ChennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class BlorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class KochijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(Hydjobs,HydjobsAdmin)
admin.site.register(Chennaijobs,ChennaijobsAdmin)
admin.site.register(Blorejobs,BlorejobsAdmin)
admin.site.register(Kochijobs,KochijobsAdmin)

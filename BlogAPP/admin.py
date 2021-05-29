from django.contrib import admin
from .models import Instruction,Comment,GoogleAdd,Category,User_Information
# Register your models here.

admin.site.register(Instruction)
admin.site.register(Comment)
admin.site.register(GoogleAdd)
admin.site.register(Category)
admin.site.register(User_Information)
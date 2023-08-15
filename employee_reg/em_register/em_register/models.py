from django.db import models
# from em_register import admin

# from em_register.admin import export_selected_to_excel


class em_register(models.Model):
    name=models.CharField(max_length=200,default='')
    email = models.CharField(max_length=255,default='')
    city=models.CharField(max_length=500,default='')
    number = models.CharField(max_length=100, default='')
    resume = models.FileField(upload_to='resumes/',default='')

# class em_registerAdmin(admin.ModelAdmin):
#     actions = [export_selected_to_excel]

# admin.site.register(em_register, em_registerAdmin)



   



    def __str__(self):
        return self.name 
    
from django.contrib import admin
from .models import em_register

admin.site.register(em_register)

# def export_selected_to_excel(modeladmin, request, queryset):
#     # Your code for exporting to Excel goes here
#     # Indent the block with your export logic

#   export_selected_to_excel.short_description = "Export selected items to Excel"
 

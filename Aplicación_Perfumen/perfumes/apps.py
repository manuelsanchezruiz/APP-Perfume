from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig
from django.contrib.admin.sites import AdminSite

class PerfumesConfig(AppConfig):
    name = 'perfumes'

    def ready(self):
        AdminSite.site_header = "Perfumes Admin"
        AdminSite.site_title = "Perfumes Admin Portal"
        AdminSite.index_title = "Welcome to Perfumes Admin"

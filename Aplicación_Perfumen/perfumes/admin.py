from django.contrib import admin
from .models import Usuario, Producto, Carrito

class MyAdminSite(admin.AdminSite):
    site_header = 'Perfumes Administration'
    site_title = 'Perfumes Admin'
    index_title = 'Admin'

    def each_context(self, request):
        context = super().each_context(request)
        context['admin_title'] = self.index_title
        return context

admin_site = MyAdminSite(name='myadmin')

admin_site.register(Usuario)
admin_site.register(Producto)
admin_site.register(Carrito)

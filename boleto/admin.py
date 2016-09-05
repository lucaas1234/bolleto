from django.contrib import admin

from .models import Cliente
from .models import Cedente
from .models import Sacado
from .models import Contrato
from .models import Prestacao


admin.site.register(Cliente)
admin.site.register(Cedente)
admin.site.register(Sacado)
admin.site.register(Contrato)
admin.site.register(Prestacao)

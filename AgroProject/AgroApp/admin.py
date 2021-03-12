from django.contrib import admin
from .models import User, Province, Region,Categoriya,Obyavleniya
from .models import Sostayanie,ChastnoLitso,Nalichie,Edinitsva
from .models import Dogovornaya,News
admin.site.register(User)
admin.site.register(Province)
admin.site.register(Region)
admin.site.register(Categoriya)
admin.site.register(Obyavleniya)
admin.site.register(Sostayanie)
admin.site.register(ChastnoLitso)
admin.site.register(Nalichie)
admin.site.register(Edinitsva)
admin.site.register(Dogovornaya)
admin.site.register(News)


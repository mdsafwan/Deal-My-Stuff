from django.contrib import admin
from advertisements.models import advertisement, category, electronic_gadget, vehicle, book, household_item

admin.site.register(advertisement)
admin.site.register(category)
admin.site.register(electronic_gadget)
admin.site.register(vehicle)
admin.site.register(book)
admin.site.register(household_item)
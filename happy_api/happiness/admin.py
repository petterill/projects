from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Country
from import_export import resources
from .models import Country


class CountryResource(resources.ModelResource):
    class Meta:
        model = Country


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    pass

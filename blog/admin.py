from django.contrib import admin
from .models import (
    PlantedTrees,
    MainPageStatic,
    AboutTrees,
    AllTreesCount,
    Project,
    Companies,
    UserTree
)

@admin.register(Companies)
class CompaniesListAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "companyWebSite", "logo"]

@admin.register(Project)
class ProjectListAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "required", "funded"]

@admin.register(PlantedTrees)
class PlantedTreesAdmin(admin.ModelAdmin):
    list_display = ["time", "count"]

@admin.register(MainPageStatic)
class MainPageStaticAdmin(admin.ModelAdmin):
    list_display = ["title", "count"]

@admin.register(AboutTrees)
class AboutTreesAdmin(admin.ModelAdmin):
    list_display = ["name", "nameLotin", "cost"]
    list_filter = ["name", "nameLotin"]
    search_fields = ["name"]

@admin.register(AllTreesCount)
class AllTreesAdmin(admin.ModelAdmin):
    list_display = ["count"]

@admin.register(UserTree)
class UserTreeAdmin(admin.ModelAdmin):
    list_display = ["treeId", "userId"]

from django.contrib import admin
from .models import *

class StatisticsInline(admin.TabularInline):
    model = Statistics
    extra = 1

class OfficeHoursInline(admin.TabularInline):
    model = OfficeHours
    extra = 1

class SocialNetworksInline(admin.TabularInline):
    model = SocialNetworks
    extra = 1

class PartnersInline(admin.TabularInline):
    model = Partners
    extra = 1

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address')
    inlines = [StatisticsInline, OfficeHoursInline, SocialNetworksInline, PartnersInline]



class StepDetailsInline(admin.TabularInline):
    model = StepDetails
    extra = 1

@admin.register(Steps)
class StepsAdmin(admin.ModelAdmin):
    inlines = [StepDetailsInline]

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('header', 'date')
    search_fields = ('header',)

class FAQInfoInline(admin.TabularInline):
    model = FAQInfo
    extra = 1

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    inlines = [FAQInfoInline]
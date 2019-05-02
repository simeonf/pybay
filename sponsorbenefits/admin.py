from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from ordered_model.admin import OrderedModelAdmin

from .models import (AddOnBenefitRow, AlaCarteBenefitRow, Benefit, BenefitApplies, ExplanationRow,
                     SponsorCategory, SponsorPackage, SponsorLevel)


@admin.register(AddOnBenefitRow)
class AddOnBenefitAdmin(OrderedModelAdmin):
    list_display = ('title', 'move_up_down_links')


@admin.register(AlaCarteBenefitRow)
class AlaCarteAdmin(OrderedModelAdmin):
    list_display = ('title', 'move_up_down_links')


@admin.register(SponsorPackage)
class SponsorPackageAdmin(OrderedModelAdmin):
    list_display = ('text', 'move_up_down_links')


@admin.register(SponsorCategory)
class SponsorCategoryAdmin(OrderedModelAdmin):
    list_display = ('text', 'move_up_down_links')


@admin.register(SponsorLevel)
class SponsorLevelAdmin(OrderedModelAdmin):
    list_display = ('category', 'text', 'move_up_down_links')

@admin.register(ExplanationRow)
class ExplanationRowAdmin(OrderedModelAdmin):
    list_display = ('title', 'move_up_down_links')


class BenefitAppliesInline(admin.TabularInline):
    model = BenefitApplies

@admin.register(Benefit)
class SponsorLevelAdmin(OrderedModelAdmin):
    list_display = ('package', 'text', 'move_up_down_links')
    inlines = [BenefitAppliesInline]

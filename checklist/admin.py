from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import *

# Register your models here.
# class AuditAdmin(admin.ModelAdmin):
#     search_fields = ('title',)
#     list_display = ('title',)
#     list_display_links = ('title',)

# admin.site.register(Checklist,AuditAdmin)
class LevelThreeInline(NestedStackedInline):
    model = Question
    extra = 1
    fk_name = 'level'


class LevelTwoInline(NestedStackedInline):
    model = Subsection
    extra = 1
    fk_name = 'level'
    inlines = [LevelThreeInline]

class LevelOneInline(NestedStackedInline):
    model = Section
    extra = 1
    fk_name = 'level'
    inlines = [LevelTwoInline]


class TopLevelAdmin(NestedModelAdmin):
    model = CheckList
    inlines = [LevelOneInline]


admin.site.register(CheckList, TopLevelAdmin)
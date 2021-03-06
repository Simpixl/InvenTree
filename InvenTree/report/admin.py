# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ReportSnippet, TestReport, ReportAsset


class ReportTemplateAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'template', 'filters', 'enabled', 'revision')


class ReportSnippetAdmin(admin.ModelAdmin):

    list_display = ('id', 'snippet', 'description')


class ReportAssetAdmin(admin.ModelAdmin):

    list_display = ('id', 'asset', 'description')


admin.site.register(ReportSnippet, ReportSnippetAdmin)
admin.site.register(TestReport, ReportTemplateAdmin)
admin.site.register(ReportAsset, ReportAssetAdmin)

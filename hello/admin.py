from django.contrib import admin
from .models import Entry, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """分类管理后台配置"""
    list_display = ('name', 'created_at', 'entry_count')
    search_fields = ('name', 'description')
    ordering = ('created_at',)
    
    def entry_count(self, obj):
        """显示每个分类下的词条数量"""
        return obj.entries.count()
    entry_count.short_description = '词条数量'


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    """词条管理后台配置"""
    list_display = ('title', 'category', 'created_at', 'updated_at', 'view_count')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    ordering = ('-updated_at',)
    fieldsets = (
        ('基本信息', {
            'fields': ('title', 'category')
        }),
        ('内容', {
            'fields': ('content',)
        }),
        ('统计信息', {
            'fields': ('view_count',),
            'classes': ('collapse',)
        }),
    )
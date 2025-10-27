from django.db import models
from django.utils import timezone


class Category(models.Model):
    """百科分类模型"""
    name = models.CharField(max_length=100, verbose_name='分类名称')
    description = models.TextField(blank=True, null=True, verbose_name='分类描述')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类管理'


class Entry(models.Model):
    """百科词条模型"""
    title = models.CharField(max_length=200, verbose_name='词条标题')
    content = models.TextField(verbose_name='词条内容')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='entries', verbose_name='所属分类')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    view_count = models.IntegerField(default=0, verbose_name='浏览次数')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '词条'
        verbose_name_plural = '词条管理'
        ordering = ['-updated_at']  # 默认按更新时间倒序排列
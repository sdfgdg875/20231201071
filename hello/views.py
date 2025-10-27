from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Entry, Category
from .forms import EntryForm, CategoryForm


def entry_list(request):
    """词条列表页面"""
    entries = Entry.objects.all()
    categories = Category.objects.all()
    
    # 按分类筛选
    category_id = request.GET.get('category')
    if category_id:
        entries = entries.filter(category_id=category_id)
    
    return render(request, 'hello/entry_list.html', {
        'entries': entries,
        'categories': categories,
        'selected_category': category_id
    })


def entry_detail(request, entry_id):
    """词条详情页面"""
    entry = get_object_or_404(Entry, pk=entry_id)
    # 增加浏览次数
    entry.view_count += 1
    entry.save()
    return render(request, 'hello/entry_detail.html', {'entry': entry})


def category_entries(request, category_id):
    """按分类查看词条"""
    category = get_object_or_404(Category, pk=category_id)
    entries = Entry.objects.filter(category=category)
    categories = Category.objects.all()
    
    return render(request, 'hello/entry_list.html', {
        'entries': entries,
        'categories': categories,
        'selected_category': category_id,
        'current_category': category
    })

@login_required
def entry_create(request):
    """创建词条"""
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('entry_detail', entry_id=entry.pk)
    else:
        form = EntryForm()
    return render(request, 'hello/entry_form.html', {'form': form, 'title': '创建新词条'})

@login_required
def entry_edit(request, entry_id):
    """编辑词条"""
    entry = get_object_or_404(Entry, pk=entry_id)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save()
            return redirect('entry_detail', entry_id=entry.pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'hello/entry_form.html', {'form': form, 'title': '编辑词条', 'entry': entry})

@login_required
def entry_delete(request, entry_id):
    """删除词条"""
    entry = get_object_or_404(Entry, pk=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render(request, 'hello/entry_confirm_delete.html', {'entry': entry})

@login_required
def category_create(request):
    """创建分类"""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
    else:
        form = CategoryForm()
    return render(request, 'hello/category_form.html', {'form': form, 'title': '创建新分类'})
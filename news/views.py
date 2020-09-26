from django.shortcuts import render
from .models import News


def index(request):
    if request.method == 'POST':
        if request.POST.get('update_news') == 'True':
            News.load_news_from_instagram()
    news = News.objects.all()
    if request.method == 'POST':
        if request.POST.get('sort_by_publish_date') == 'True':
            news = news.order_by('-publish_date')
    if request.method == 'GET':
        searched_word = request.GET.get('find_in_text')
        if searched_word is not None:
            news = news.filter(text__icontains=searched_word)
    template_path = 'news/index.html'
    context_dict = {
        'news': news,
        'update_news': False
    }
    return render(request, template_path, context_dict)

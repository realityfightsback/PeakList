from django.shortcuts import render
from django.http.response import HttpResponse
from models import Post

from django.template import RequestContext, loader
from mainApp.models import Category


def index(request):
    
#     categories = Category.objects.order_by('text')
#     
#     latest_question_list = Post.objects.order_by('-date')[:5]
    template = loader.get_template('mainApp/categories.html')
#     context = RequestContext(request, {
#         'latest_question_list': latest_question_list,
#     })
    return HttpResponse(template.render())
#     output = ', '.join([p.text for p in latest_question_list])
#     return HttpResponse(output)
# #     return HttpResponse('Hello world')

def detail(request, id):
    post = Post.objects.get(pk = id)
    return HttpResponse(post.text)

from django.http import HttpResponse
from django.shortcuts import render
from post_machin import models

# Create your views here.
def post_machin_view(requst):
    post_machins = models.PostMachin.objects.all()
    print(post_machins)
    return   HttpResponse(f"helo start meni post_machin{post_machins[1].city}")



def one_post_machin_view(requst, post_machin_id):
    one_post_machin = models.PostMachin.objects.get(id=post_machin_id)
    post_machin_lockes = models.Locker.objects.filter(post_machin =one_post_machin)
    one_locker = models.Locker.objects.get(pk=1)

    return HttpResponse(f"helo start one post_machin {post_machin_id} in {post_machin_lockes[0].size} one loker {one_locker.post_machin.adress}")

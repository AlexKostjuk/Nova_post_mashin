# from django.http import HttpResponse, request
from django.shortcuts import render
from post_machin import models

# Create your views here.
def post_machin_view(request):
    # user = request.user
    post_machines = models.PostMachin.objects.all()
    return render(request, 'post_machines.html', context={'post_machines': post_machines})


def one_post_machin_view(request, post_machin_id):
    # result = models.Parcel.objects.get(pk=parcel_id)
    user = request.user

    one_post_machin = models.PostMachin.objects.get(id=post_machin_id)
    post_machin_lockes = models.Locker.objects.filter(post_machin =one_post_machin)
    one_locker = models.Locker.objects.get(pk=1)
    return render(request, 'one_post_machin.html', context={'parcel': result})
    # return HttpResponse(f"helo start one post_machin {post_machin_id} in {post_machin_lockes[0].size} one loker {one_locker.post_machin.adress}")

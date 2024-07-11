from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_machin_view(requst):
    return HttpResponse("helo start meni post_machin")


def one_post_machin_view(requst, post_machin_id):
    return HttpResponse(f"helo start one post_machin {post_machin_id}")

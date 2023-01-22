from django.http import HttpResponse
from django.shortcuts import render
from microhr.models import Work
from logging import getLogger
from django.core import serializers

logger = getLogger(__name__)


def home(request):
    """HOME"""
    logger.debug("display home")
    works = Work.objects.all()
    context = {"works": works}
    return render(request, "home.html", context)


"""API用、求人全取得"""
def getWorks(request):
    works = serializers.serialize("json", Work.objects.all())
    return HttpResponse(works)


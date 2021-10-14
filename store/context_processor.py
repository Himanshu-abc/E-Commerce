# A contextv processor allow us to run code threough whole project

from .models import Category


def categories(request):
    return {
     'categories':Category.objects.all()
    }
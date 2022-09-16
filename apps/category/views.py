import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from apps.category.models import Category


# Category view creation

class CategoryView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id: int = 0):
        if id > 0:
            categories = list(Category.objects.filter(id=id).values())
            if len(categories) > 0:
                category = categories[0]
                data = {'message': "Success", 'categories': category}
            else:
                data = {'message': "Category no found ..."}
            return JsonResponse(data)
        else:
            categories = list(Category.objects.values())
            if len(categories) > 0:
                data = {'message': "Success", 'categories': categories}
            else:
                data = {'message': "Category no found ..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Category.objects.create(name_category=jd['name_category'], type_category=jd['type_category'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id: int = 0):
        jd = json.loads(request.body)
        categories = list(Category.objects.filter(id=id).values())
        if len(categories) > 0:
            categories = Category.objects.get(id=id)
            categories.name_category = jd['name_category']
            categories.type_category = jd['type_category']
            categories.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Category no found ..."}
        return JsonResponse(data)

    def delete(self, request, id):
        categories = list(Category.objects.filter(id=id).values())
        if len(categories) > 0:
            Category.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Category no found ..."}
        return JsonResponse(data)

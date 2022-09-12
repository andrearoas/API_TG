import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from apps.pest.models import Pest


class PestView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id: int = 0):
        if id > 0:
            pests = list(Pest.objects.filter(id=id).values())
            if len(pests) > 0:
                pest = pests[0]
                data = {'message': "Success", 'pests': pest}
            else:
                data = {'message': "Pest no found ..."}
            return JsonResponse(data)
        else:
            pests = list(Pest.objects.values())
            if len(pests) > 0:
                data = {'message': "Success", 'pests': pests}
            else:
                data = {'message': "Pests no found ..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Pest.objects.create(name_pest=jd['name_pest'], description_pest=jd['description_pest'],
                            photo_pest=jd['photo_pest'],
                            description_prevent=jd['description_prevent'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        pests = list(Pest.objects.filter(id=id).values())
        if len(pests) > 0:
            pests = Pest.objects.get(id=id)
            pests.name_pest = jd['name_pest']
            pests.description_pest = jd['description_pest']
            pests.photo_pest = jd['photo_pest']
            pests.description_prevent = jd['description_prevent']
            pests.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Pest no found ..."}
        return JsonResponse(data)

    def delete(self, request, id):
        pests = list(Pest.objects.filter(id=id).values())
        if len(pests) > 0:
            Pest.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Pest no found ..."}
        return JsonResponse(data)

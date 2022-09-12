import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from apps.neighbours.models import Neighbour


class NeighbourView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id: int = 0):
        if id > 0:
            neighbours = list(Neighbour.objects.filter(id=id).values())
            if len(neighbours) > 0:
                neigh = neighbours[0]
                data = {'message': "Success", 'neighbours': neigh}
            else:
                data = {'message': "Neighbour no found ..."}
            return JsonResponse(data)
        else:
            neighbours = list(Neighbour.objects.values())
            if len(neighbours) > 0:
                data = {'message': "Success", 'neighbours': neighbours}
            else:
                data = {'message': "Neighbours no found ..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Neighbour.objects.create(type_neighbour=jd['type_neighbour'], description_neigh=jd['description_neigh'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        neigh = list(Neighbour.objects.filter(id=id).values())
        if len(neigh) > 0:
            neigh = Neighbour.objects.get(id=id)
            neigh.type_neighbour = jd['type_neighbour']
            neigh.description_neigh = jd['description_neigh']
            neigh.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Neighbour no found ..."}
        return JsonResponse(data)

    def delete(self, request, id):
        neigh = list(Neighbour.objects.filter(id=id).values())
        if len(neigh) > 0:
            Neighbour.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Neighbour no found ..."}
        return JsonResponse(data)

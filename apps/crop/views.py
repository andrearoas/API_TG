import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from apps.crop.models import Crop


# Crop view creation.
class CropView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id: int = 0):
        if id > 0:
            crops = list(Crop.objects.filter(id=id).values())
            if len(crops) > 0:
                croops = crops[0]
                data = {'message': "Success", 'crops': croops}
            else:
                data = {'message': "Crop no found ..."}
            return JsonResponse(data)
        else:
            crops = list(Crop.objects.values())
            if len(crops) > 0:
                data = {'message': "Success", 'crops': crops}
            else:
                data = {'message': "Crop no found ..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Crop.objects.create(photo_crop=jd['photo_crop'],
                            name_crop=jd['name_crop'],
                            name_scie_crop=jd['name_scie_crop'],
                            description_crop=jd['description_crop'],
                            time_germination=jd['time_germination'],
                            time_harvest=jd['time_harvest'],
                            time_seeding=jd['time_seeding'],
                            time_sun_crop=jd['time_sun_crop'],
                            amount_water_crop=jd['amount_water_crop'],
                            distance_crops=jd['distance_crops'],
                            height_max_crop=jd['height_max_crop'],
                            type_container=jd['type_container'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id: int = 0):
        jd = json.loads(request.body)
        crops = list(Crop.objects.filter(id=id).values())
        if len(crops) > 0:
            crops = Crop.objects.get(id=id)
            crops.photo_crop = jd['photo_crop']
            crops.name_crop = jd['name_crop']
            crops.name_scie_crop = jd['name_scie_crop']
            crops.description_crop = jd['description_crop']
            crops.time_germination = jd['time_germination']
            crops.time_harvest = jd['time_harvest']
            crops.time_seeding = jd['time_seeding']
            crops.time_sun_crop = jd['time_sun_crop']
            crops.amount_water_crop = jd['amount_water_crop']
            crops.distance_crops = jd['distance_crops']
            crops.height_max_crop = jd['height_max_crop']
            crops.type_container = jd['type_container']
            crops.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Crop no found ..."}
        return JsonResponse(data)

    def delete(self, request, id):
        crops = list(Crop.objects.filter(id=id).values())
        if len(crops) > 0:
            Crop.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Crop no found ..."}
        return JsonResponse(data)

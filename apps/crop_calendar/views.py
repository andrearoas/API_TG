import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from apps.crop_calendar.models import CropCalendar


class CropCalendarView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id: int = 0):
        if id > 0:
            calendars = list(CropCalendar.objects.filter(id=id).values())
            if len(calendars) > 0:
                ccalendar = calendars[0]
                data = {'message': "Success", 'calendars': ccalendar}
            else:
                data = {'message': "Calendar no found ..."}
            return JsonResponse(data)
        else:
            calendars = list(CropCalendar.objects.values())
            if len(calendars) > 0:
                data = {'message': "Success", 'calendars': calendars}
            else:
                data = {'message': "Calendar no found ..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        CropCalendar.objects.create(crop_start_date=jd['crop_start_date'],
                                    crop_end_date=jd['crop_end_date'], )
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        calendars = list(CropCalendar.objects.filter(id=id).values())
        if len(calendars) > 0:
            calendars = CropCalendar.objects.get(id=id)
            calendars.crop_start_date = jd['crop_start_date']
            calendars.crop_end_date = jd['crop_end_date']
            calendars.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Calendar no found ..."}
        return JsonResponse(data)

    def delete(self, request, id):
        ccalendar = list(CropCalendar.objects.filter(id=id).values())
        if len(ccalendar) > 0:
            CropCalendar.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Calendar no found ..."}
        return JsonResponse(data)

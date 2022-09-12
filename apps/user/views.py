import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from apps.user.models import User


# User View creation

class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id: int = 0):
        if id > 0:
            users = list(User.objects.filter(id=id).values())
            if len(users) > 0:
                user = users[0]
                data = {'message': "Success", 'users': user}
            else:
                data = {'message': "User no found ..."}
            return JsonResponse(data)
        else:
            users = list(User.objects.values())
            if len(users) > 0:
                data = {'message': "Success", 'users': users}
            else:
                data = {'message': "Users no found ..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        User.objects.create(name_user=jd['name_user'], lastname_user=jd['lastname_user'],
                            email_user=jd['email_user'], password_user=jd['password_user'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            users = User.objects.get(id=id)
            users.name_user = jd['name_user']
            users.lastname_user = jd['lastname_user']
            users.email_user = jd['email_user']
            users.password_user = jd['password_user']
            users.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Users no found ..."}
        return JsonResponse(data)

    def delete(self, request, id):
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            User.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Users no found ..."}
        return JsonResponse(data)

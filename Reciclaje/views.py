from django.http import HttpResponse


def index(request):
    return HttpResponse("imaginense una pagina principal")

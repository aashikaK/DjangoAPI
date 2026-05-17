from django.http import HttpResponse,JsonResponse

def home_page(request):
    friends=[
        'aashika',
        'bina',
        'asmita'
    ]

    # return HttpResponse("This is home page.")
    return JsonResponse(friends,safe=False)
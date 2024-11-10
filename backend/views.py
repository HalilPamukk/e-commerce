from django.http import JsonResponse


def main_page(request):
    context = {
        "title": "This Is an E-Commerce Website",
        "content": "Welcome to the main page!",
    }
    return JsonResponse(context)
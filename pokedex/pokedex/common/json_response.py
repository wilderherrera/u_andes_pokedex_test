from django.http import JsonResponse as DjangoJsonResponse


class JsonResponse(DjangoJsonResponse):
    def __init__(self, data, safe=False, **kwargs):
        wrapped_data = {'data': data}
        super().__init__(data=wrapped_data, safe=safe, **kwargs)

from datetime import datetime


class LoggingMiddleware:
    """
    Ограничение по количеству запросов с одного IP в промежутке времени
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.time_now = datetime.now()

    def __call__(self, request):
        info = request.META.get('HTTP_USER_AGENT')
        print(info)
        response = self.get_response(request)

        return response

from datetime import datetime
from django.core.exceptions import PermissionDenied


class FilterIPMiddleware:
    """
    Ограничение по количеству запросов с одного IP в промежутке времени
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips = {}
        self.time_now = datetime.now()
        self.time_limit = 20
        self.request_limit = 5

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        self.check_time(ip)
        response = self.get_response(request)

        return response

    def check_time(self, ip):
        delta_time = datetime.now() - self.time_now
        if delta_time.seconds < self.time_limit:
            self.check_ip(ip)
        else:
            self.reset(ip)

    def check_ip(self, ip):
        if ip not in self.allowed_ips:
            self.allowed_ips[ip] = 1
        else:
            self.allowed_ips[ip] += 1
            if self.allowed_ips[ip] > self.request_limit:
                raise PermissionDenied

    def reset(self, ip):
        self.allowed_ips[ip] = 0
        self.time_now = datetime.now()

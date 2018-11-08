from django.http import HttpResponse
class MaintananceInfo(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response
    def process_exception(self, request, exception):
        return HttpResponse("This Website is under maintanance")

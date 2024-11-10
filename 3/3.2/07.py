class HandlerGET:
    def __init__(self, func):
        self.func = func

    @staticmethod
    def get(func, request):
        return f"GET: {func(request)}"

    def __call__(self, request):
        method = request.get("method", "GET")
        if method == "GET":
            return self.get(self.func, request)
        return None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


@HandlerGET
def index(request):
    return "главная страница сайта"


res = contact({"method": "GET", "url": "contact.html"})
print(res)

res = index({"method": "GET"})
print(res)

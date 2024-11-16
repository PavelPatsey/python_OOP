class Handler:
    def __init__(self, methods=("GET",)):
        self.methods = methods

    @staticmethod
    def get(func, request):
        return f"GET: {func(request)}"

    @staticmethod
    def post(func, request):
        return f"POST: {func(request)}"

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            method = request.get("method", "GET")
            if method in self.methods:
                return self.__getattribute__(method.lower())(func, request)
            return

        return wrapper


@Handler(methods=("GET", "POST"))
def contact(request):
    return "Сергей Балакирев"


print(contact({"method": "POST", "url": "contact.html"}))
assert contact({"method": "POST"}) == "POST: Сергей Балакирев"


@Handler()
def index(request):
    return "главная страница сайта"


print(index({"method": "GET"}))
assert index({"method": "GET"}) == "GET: главная страница сайта"


@Handler(methods=("POST",))
def index(request):
    return "главная страница сайта"


assert (
    index({"method": "GET"}) is None
), "декорированная функция вернула неверные данные"

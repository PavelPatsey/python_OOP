class RenderList:
    def __init__(self, type_list):
        self.type_list = "ol" if type_list == "ol" else "ul"

    def __call__(self, list_for_render):
        mapped = map(lambda x: f"<li>{x}</li>", list_for_render)
        return "\n".join((f"<{self.type_list}>", *mapped, f"</{self.type_list}>"))


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)

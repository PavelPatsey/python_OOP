class RenderList:
    def __init__(self, type_list):
        self.type_list = "ol" if type_list == "ol" else "ul"

    def __call__(self, list_for_render):
        result = f"<{self.type_list}>\n"
        result += "\n".join(f"<li>{item}</li>" for item in list_for_render)
        result += f"\n</{self.type_list}>"
        return result


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)

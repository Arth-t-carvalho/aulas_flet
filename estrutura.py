import flet as ft 
# importa a biblioteca flet e coloca um apelido nela ai sempre que eu chamar esse ft vai chamar o flet isso e um (alias)

def main(page: ft.Page):
    page.title = "meu primeiro app flet"
    page.bgcolor = "red"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text("bem vindo ao meu app"),
        ft.Text("Aqui você pode criar oque eu quiser"),
        

    )

ft.app(main) 

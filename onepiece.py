import flet as ft

def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(
            ft.Text("Eu sou o melhor espadachim do mundo.")
        )
    page.add(
        ft.Text("Olá, meu nome é Mihawk!"),
        ft.Image(
            src="/images/mihawk.webp",
            height=150,
        ),
        ft.Button(
            content=ft.Text("Clique aqui"),
            on_click=mostrar_mensagem
        )
    )
    
ft.run(main)

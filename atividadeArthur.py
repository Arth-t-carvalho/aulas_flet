import flet as ft

def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(
            ft.Text("me perdoe, Sasuke, esta é a última vez...")
        )
    page.add(
        ft.Text("Olá, meu nome é itachi uchiha"),
        ft.Image(
            src="/images/itachi.jpg",
            height=150,
        ),
        ft.Button(
            content=ft.Text("conclua sua vingaça"),
            on_click=mostrar_mensagem
        )
    )
    
ft.run(main)

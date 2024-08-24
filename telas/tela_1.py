import flet as ft


# vou utilizar essa função para criar o layout da pagina
def main(page: ft.Page):
    page.title = "Tela de login"
    tf_email = ft.TextField(label="Email")
    tf_senha = ft.TextField(label="Senha")
    btn_fazerlogin = ft.ElevatedButton(text="Login")

    # page.add tem que vir antes do update
    page.add(tf_email)
    page.add(tf_senha)
    page.add(btn_fazerlogin)

    # criando o evento
    # tem que criar o evento antes de chamar ele
    def enviarNome(e):
        print(tf_nome.value)

    btn_fazerlogin.on_click = enviarNome

    # toda vez que eu aletrar a minha pagina, EU DEVO DAR UM UPDATE!!!!!!
    page.update()


if __name__ == '__main__':
    ft.app(main)

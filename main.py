import flet as ft

def main(page: ft.Page):
    page.title = "basically a calculator"
    page.window_width = 320
    page.window_height = 480
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.GREY_50

    expression = ""

    display = ft.TextField(
        value="0",
        read_only=True,
        text_align="right",
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_GREY_100,
        focused_border_color=ft.Colors.BLUE_400,
        height=70,
        text_size=28
    )

    def update_display(val):
        display.value = val
        page.update()

    def button_click(e):
        nonlocal expression
        key = e.control.text

        if key == "C":
            expression = ""
        elif key == "⌫":
            expression = expression[:-1]
        elif key == "=":
            try:
                # Safely evaluate the mathematical expression
                expression = str(eval(expression))
            except Exception:
                expression = "Error"
        else:
            if expression == "Error":
                expression = ""
            expression += key

        update_display(expression if expression else "0")

    def make_button(text, color=ft.Colors.BLUE_GREY_700):
        return ft.Container(
            content=ft.TextButton(
                text=text,
                on_click=button_click,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.WHITE,
                    color=color,
                    padding=20,  # Replaced ft.Padding.all(20) with numeric padding value
                    text_style=ft.TextStyle(size=22, weight=ft.FontWeight.BOLD),
                ),
            ),
            expand=True,
            alignment=ft.alignment.center,
        )

    # Define the layout of buttons
    buttons = [
        ["C", "⌫", "%", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", ".", "=", ""]
    ]

    grid = ft.Column(
        [
            ft.Row([make_button(btn) for btn in row if btn], alignment="spaceEvenly")
            for row in buttons
        ],
        spacing=10,
        expand=True,
    )

    # Add an image at the top as the app icon/splash (ensure calculator.jpg exists in assets/)
    page.add(
        ft.Column(
            [
                ft.Image(src="calculator.jpg", height=120),
                ft.Container(display, padding=10),
                grid,
            ],
            spacing=10,
            alignment="center",
        )
    )

# Launch the app with the assets directory set
ft.app(
    target=main,
    assets_dir="assets",
    view=ft.AppView.WEB_BROWSER,
)

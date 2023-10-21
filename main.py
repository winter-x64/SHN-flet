import flet as ft


def main(page: ft.Page) -> None:
    page.title = "Welcome"
    page.vertical_alignment = "center"
    # page.horizontal_alignment = "center"

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
        )
        print(selected_files.value)
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    def close_dlg(e) -> None:
        dlg_modal.open = False
        page.update()

    def yes_dlg(e) -> None:
        dlg = ft.AlertDialog(
            title=ft.Text(value="Mails Send!"),
            on_dismiss=lambda e: print("Dialog dismissed!"),
        )
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want send the mails to you?"),
        actions=[
            ft.TextButton("Yes", on_click=yes_dlg),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg_modal(e) -> None:
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def on_dialog_result(e) -> None:
        pass

    def generate_certificate(e) -> None:
        pass

    # All the btn
    btn_generate = ft.ElevatedButton(
        text="Generate",
        icon=ft.icons.GENERATING_TOKENS_OUTLINED,
        color=ft.colors.GREEN,
        on_click=generate_certificate,
    )

    # uploads btn
    btn_upload_certificate = ft.ElevatedButton(
        text="Pick files",
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True),
    )

    # send mail btn
    btn_send_mail = ft.ElevatedButton(
        text="Send Email",
        icon=ft.icons.SEND_ROUNDED,
        color=ft.colors.BLUE,
        on_click=open_dlg_modal,
    )

    # test

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER,
                selected_icon=ft.icons.MENU_BOOK_OUTLINED,
                label="Menu",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.CONTROL_POINT_DUPLICATE_ROUNDED),
                label="Alignment",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    img = ft.Image(
        src=".\powershell_icon_132080.png" if selected_files.value else "",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    images = ft.Row(expand=1, wrap=False, scroll="always")

    # test
    page.overlay.extend([pick_files_dialog])

    page.add(
        ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value="Flet Pro"),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Row(
                    controls=[
                        btn_generate,
                        ft.Text(value="     "),
                        btn_send_mail,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        ft.Row(
            controls=[
                rail,
                ft.VerticalDivider(width=1),
                ft.Row(
                    controls=[
                        img,
                        btn_upload_certificate,
                        selected_files,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
        ),
    )


if __name__ == "__main__":
    ft.app(target=main)

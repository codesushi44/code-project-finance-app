import flet as ft

def main(page: ft.Page):
    name_input = ft.TextField(label="Asset Name (e.g. Maybank)")
    amount_input = ft.TextField(label="Amount", prefix_icon="RM ")
    
    def handle_save(e):
        print(f"Saving: {name_input.value} - {amount_input.value}")
        dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        title=ft.Text("Add New Asset"),
        content=ft.Column([name_input, amount_input], tight=True),
        actions=[ft.TextButton("Save", on_click=handle_save)]
    )

    page.overlay.append(dialog)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        on_click=lambda _: setattr(dialog, "open", True) or page.update()
    )

    page.add(ft.Text("Your Odyssey Assets will appear here."))

ft.run(main)
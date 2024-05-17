import reflex as rx

navbar_style = dict(
    position="fixed",
    width="100%",
    margin="1em",
    padding_right="10em",
    padding_left="10em",
    border=("1px", "1px", "1px", "1px", "black"),
)


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Mohit Singh", size="5", weight="bold", on_click=lambda: rx.redirect("/")
        ),
        rx.spacer(),
        rx.button(
            "Code",
            background_color="white",
            color="black",
            size="3",
            on_click=lambda: rx.redirect("code"),
        ),
        rx.button("Blog", background_color="white", color="black", size="3"),
        style=navbar_style,
    )

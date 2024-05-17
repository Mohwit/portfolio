import reflex as rx


def index() -> rx.Component:
    return rx.center(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Probably a Data Scientist.", size="8"),
            rx.text(
                "I am Mohit Singh, a software engineer from India. I occasionally work with organizations to help them build their dreams when I am not building mine.",
                size="4",
            ),
            rx.hstack(
                rx.button(
                    "</> code",
                    background_color="black",
                    on_click=lambda: rx.redirect("code"),
                ),
                rx.button(
                    rx.icon(tag="pen", size=18), " Blogs", background_color="black"
                ),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            margin_left="30%",
            margin_right="30%",
        ),
    )

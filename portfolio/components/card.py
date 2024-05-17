import reflex as rx


def code_card() -> rx.section:
    return rx.section(
        rx.text(
            "Markdoc - A language adventure",
            padding_bottom="4px",
            weight="bold",
            size="4",
        ),
        rx.hstack(
            rx.hstack(
                rx.icon(tag="calendar", size=15),
                rx.text("23-04-2024", size="2"),
                spacing="1",
                align="center",
            ),
            rx.hstack(
                rx.icon(tag="clock", size=15),
                rx.text("3 min", size="2"),
                spacing="1",
                align="center",
            ),
            rx.hstack(
                rx.icon(tag="book-text", size=15),
                rx.text("450 words", size="2"),
                spacing="1",
                align="center",
            ),
        ),
        rx.text(
            """
                    I used to build blog and websites with njk but due to limitations I faced, I switched to Next.
                    The markdown with front-matter is still my primary way to write text heavy content, 
                    the templates turned into JSX which allowed me to do a lot more.
                """
        ),
        padding="10px",
        on_click=lambda: rx.redirect("code/1"),
    )

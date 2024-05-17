import reflex as rx

from ..components.card import code_card
from ..components.navbar import navbar


def code_sections() -> rx.vstack:
    return rx.vstack(
        rx.desktop_only(
            rx.grid(
                rx.foreach(
                    rx.Var.range(12),
                    lambda i: code_card(),
                ),
                columns="3",
                spacing="4",
                width="100%",
                padding="32px",
            ),
            margin_top="32px",
        ),
        rx.tablet_only(
            rx.grid(
                rx.foreach(
                    rx.Var.range(12),
                    lambda i: code_card(),
                ),
                columns="2",
                spacing="4",
                width="100%",
                padding="32px",
            )
        ),
        rx.mobile_only(
            rx.grid(
                rx.foreach(
                    rx.Var.range(12),
                    lambda i: code_card(),
                ),
                columns="1",
                spacing="4",
                width="100%",
                padding="32px",
            ),
            margin_top="32px",
        ),
    )


def code() -> rx.box:
    return rx.box(navbar(), code_sections())

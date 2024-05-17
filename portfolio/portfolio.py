import reflex as rx

from rxconfig import config
from portfolio.pages.index import index
from portfolio.pages.codes_page import code


app = rx.App()
app.add_page(index(), route="/")
app.add_page(code(), route="code")

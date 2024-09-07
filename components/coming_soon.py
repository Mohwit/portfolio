from fasthtml.common import *

tailwindcss = Script(src="https://cdn.tailwindcss.com")
headers = (tailwindcss,)


def soon():
    return Html(
        *headers,
        Div(
            Div(
                Div(cls="w-16 h-1 bg-blue-500 mb-6 rounded-full"),
                H2("Coming Soon", cls="text-4xl font-bold mb-4 text-gray-800"),
                P(
                    "Exciting updates are on the way! Stay tuned!",
                    cls="text-lg text-gray-600 mb-8 max-w-md",
                ),  # updated message
            ),
            cls="flex items-center justify-center min-h-screen bg-gray-100 p-4",
        )
    )

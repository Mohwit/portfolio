from fasthtml.common import *

# from lucide_fasthtml import Lucide
from components.coming_soon import soon  # corrected the import path

tailwindcss = Script(src="https://cdn.tailwindcss.com")
headers = (tailwindcss,)

app = FastHTML()


@app.get("/")
def home():
    page = Html(
        *headers,
        Head(Title("Mohit Singh")),
        Body(
            Div(
                Div(
                    H1(
                        "Probably a Data Scientist.",
                        cls="text-4xl font-bold mb-4 text-left w-full max-w-2xl",
                    ),
                    P(
                        "I am a Data Scientist with a passion for turning data into actionable insights. "
                        "I collaborate with organizations to help them leverage data effectively",
                        cls="text-left mb-6 w-full max-w-2xl text-gray-600",
                    ),
                    Div(
                        Button(
                            "</> Code",
                            onclick="location.href='/code'",
                            cls="bg-black text-white px-4 py-2 rounded-md mr-2 hover:bg-gray-800 transition duration-300",
                        ),
                        Button(
                            "✑ Blogs",
                            onclick="location.href='/blogs'",
                            cls="bg-black text-white px-4 py-2 rounded-md hover:bg-gray-800 transition duration-300",
                        ),
                        cls="flex justify-ceneter w-full max-w-2xl space-x-4",
                    ),
                    cls="flex flex-col items-center justify-center max-w-4xl w-full mx-auto px-4",
                ),
                cls="flex items-center justify-center mr-8 ml-8 min-h-screen bg-white",
                id="main-content",
            ),
            Div(
                Button(
                    Span(cls="i-lucide-sun text-xl"),
                    cls="absolute top-4 right-4 p-2 rounded-full bg-gray-200 hover:bg-gray-300 transition duration-300",
                    id="theme-toggle",
                ),
                cls="",
            ),
        )
    )
    return page


@app.get("/code")
def code():
    page = soon()
    return page


@app.get("/blogs")
def blogs():
    page = soon()
    return page


serve()

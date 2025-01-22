from fasthtml.common import *
from fastapi.staticfiles import StaticFiles

app = FastHTML(hdrs=(Link(rel="stylesheet", href="styles.css"),))

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.route("/", methods=["GET"])
def home():
    return Html(
    Head(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Link(href='https://cdn.jsdelivr.net/npm/remixicon@4.5.0/fonts/remixicon.css', rel='stylesheet'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css'),
        Link(rel='stylesheet', href='/static/styles.css'),
        Title('Jam & Dan | Flower Shop'),
    ),
    Body(
        Nav(
            Div(
                Div(
                    A(
                        Img(src='/static/assets/mind.png', alt='logo', cls='logo-white'),
                        Img(src='/static/assets/mind.png', alt='logo', cls='logo-dark'),
                        href='#'
                    ),
                    cls='nav__logo'
                ),
                Div(
                    I(cls='ri-menu-3-line'),
                    id='menu-btn',
                    cls='nav__menu__btn'
                ),
                cls='nav__header'
            ),
            Ul(
                Li(
                    A('Home', href='#home')
                ),
                Li(
                    A('Menu', href='static_page/menu.html')
                ),
                Li(
                    A('Service', href='#service')
                ),
                Li(
                    A('Cart', href='#cart')
                ),
                id='nav-links',
                cls='nav__links'
            ),
            Div(
                Button(
                    I(cls='ri-search-line'),
                    cls='btn'
                ),
                Button(
                    I(cls='ri-shopping-bag-line'),
                    cls='btn'
                ),
                cls='nav__btns'
            )
        ),
        
        Footer(
            Div(
                Div(
                    A(
                        Img(src='/static/assets/windan.png', alt='logo'),
                        href='#',
                        cls='footer__logo'
                    ),
                    P('Experience fast delivery, easy pick-up, and a menu crafted to\r\n            satisfy every craving. Eat healthy, stay happy!'),
                    cls='footer__col'
                ),
                Div(
                    H4('Product'),
                    Ul(
                        Li(
                            A('Home', href='#')
                        ),
                        Li(
                            A('Products', href='#')
                        ),
                        Li(
                            A('About', href='#')
                        ),
                        Li(
                            A('Contact', href='#')
                        ),
                        Li(
                            A('FAQ', href='#')
                        ),
                        Li(
                            A('Releases', href='#')
                        ),
                        cls='footer__links'
                    ),
                    cls='footer__col'
                ),
                Div(
                    H4('Social'),
                    Ul(
                        Li(
                            A('Twitter', href='#')
                        ),
                        Li(
                            A('Facebook', href='#')
                        ),
                        Li(
                            A('Youtube', href='#')
                        ),
                        Li(
                            A('LinkedIn', href='#')
                        ),
                        cls='footer__links'
                    ),
                    cls='footer__col'
                ),
                Div(
                    H4('Legal'),
                    Ul(
                        Li(
                            A('Terms', href='#')
                        ),
                        Li(
                            A('Privacy', href='#')
                        ),
                        Li(
                            A('Cookies', href='#')
                        ),
                        Li(
                            A('Licenses', href='#')
                        ),
                        Li(
                            A('Settings', href='#')
                        ),
                        cls='footer__links'
                    ),
                    cls='footer__col'
                ),
                cls='section__container footer__container'
            ),
            Div('Copyright © 2024 Web Design Mastery. All rights reserved.', cls='footer__bar')
        ),
        Script(src='https://unpkg.com/scrollreveal'),
        Script(src='https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js'),
        Script(src='/static/main.js')
    ),
    lang='en'
)


serve()

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
        Title('Jam & Dan | Flower Shop')
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
                    A('Collection', href='#menu')
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
        Header(
            Div(
                Div(
                    Img(src='/static/assets/logs.png', alt='header'),
                    cls='image'
                ),
                Div(
                    Img(src='/static/assets/user-1.jpg', alt='user'),
                    P('It brings joy and artistry to every occasion with beautifully crafted flowers and effortless ordering!'),
                    cls='header__image__footer'
                ),
                cls='header__image'
            ),
            Div(
                Div(
                    Span(
                        Img(src='/static/assets/logs.png', alt='header')
                    ),
                    H2('Jam & Dan, Flower Shop'),
                    cls='header__top'
                ),
                H1(
                    'Forever in',
                    Span('Bloom,'),
                    'Bloom that last forever!'
                ),
                P('Enjoy affordable, artistic flowers that brighten any gift. Bring joy to your loved ones with our unique, lasting blooms!'),
                Div(
                    Button(
                        'Delivery',
                        Span(
                            I(cls='ri-arrow-right-line')
                        ),
                        cls='btn'
                    ),
                    Button('Pick Up', cls='btn'),
                    cls='header__btns'
                ),
                Div(
                    Div(
                        Img(src='/static/assets/header_content-1.jpg', alt='header__content'),
                        H4('Bud'),
                        cls='header__card'
                    ),
                    Div(
                        Img(src='/static/assets/header_content-2.jpg', alt='header__content'),
                        H4('Petal'),
                        cls='header__card'
                    ),
                    Div(
                        Img(src='/static/assets/header_content-1.jpg', alt='header__content'),
                        H4('Bouquet'),
                        cls='header__card'
                    ),
                    cls='header__flex'
                ),
                cls='header__content'
            ),
            id='home',
            cls='section__container header__container'
        ),
        Section(
            H2(
                'Our Popular',
                Span('Dishes'),
                cls='section__header'
            ),
            Div(
                Div(
                    Img(src='/static/assets/menu-1.jpg', alt='menu'),
                    H4('Kala Bhuna'),
                    P('A rich and flavorful slow-cooked beef dish, infused with aromatic\r\n            spices for a traditional taste.'),
                    Div(
                        H3('$50.99'),
                        Button('Add To Cart', cls='btn'),
                        cls='menu__card__footer'
                    ),
                    cls='menu__card'
                ),
                Div(
                    Img(src='/static/assets/menu-2.jpg', alt='menu'),
                    H4('Handi Mutton'),
                    P('Tender mutton simmered to perfection in pot with blend of spices for\r\n            an authentic and hearty meal.'),
                    Div(
                        H3('$75.49'),
                        Button('Add To Cart', cls='btn'),
                        cls='menu__card__footer'
                    ),
                    cls='menu__card'
                ),
                Div(
                    Img(src='/static/assets/menu-3.jpg', alt='menu'),
                    H4('Egg Curry'),
                    P('A classic dish featuring boiled eggs in a spiced tomato and onion\r\n            gravy, perfect with rice or bread.'),
                    Div(
                        H3('$30.99'),
                        Button('Add To Cart', cls='btn'),
                        cls='menu__card__footer'
                    ),
                    cls='menu__card'
                ),
                cls='menu__grid'
            ),
            Div(
                Button(
                    'See All Dishes',
                    Span(
                        I(cls='ri-arrow-right-line')
                    ),
                    cls='btn'
                ),
                cls='menu__btn'
            ),
            id='menu',
            cls='section__container menu__container'
        ),
        Section(
            Div(
                H2(
                    'How Does It',
                    Span('Works'),
                    cls='section__header'
                ),
                Div(
                    Div(
                        Div(
                            Img(src='/static/assets/service-1.png', alt='service')
                        ),
                        H4('Chose Your Meals'),
                        P('Browse through our delicious menu filled with a variety of dishes\r\n              and select your favorites effortlessly to satisfy your cravings.'),
                        A(
                            'Read More',
                            Span(
                                I(cls='ri-arrow-right-line')
                            ),
                            href='#'
                        ),
                        cls='service__card'
                    ),
                    Div(
                        Div(
                            Img(src='/static/assets/service-2.png', alt='service')
                        ),
                        H4('Track Your Order'),
                        P('Keep an eye on your meal with real-time updates from the kitchen\r\n              to your location, ensuring a seamless and transparent experience.'),
                        A(
                            'Read More',
                            Span(
                                I(cls='ri-arrow-right-line')
                            ),
                            href='#'
                        ),
                        cls='service__card'
                    ),
                    Div(
                        Div(
                            Img(src='/static/assets/service-3.png', alt='service')
                        ),
                        H4('Chose Your Meals'),
                        P('Experience ultimate convenience with easy pick-up options or\r\n              doorstep delivery, bringing your favorite meals straight to you.'),
                        A(
                            'Read More',
                            Span(
                                I(cls='ri-arrow-right-line')
                            ),
                            href='#'
                        ),
                        cls='service__card'
                    ),
                    cls='service__grid'
                ),
                cls='section__container service__container'
            ),
            id='service',
            cls='service'
        ),
        Section(
            Div(
                Div(
                    Img(src='/static/assets/banner.jpg', alt='banner'),
                    cls='banner__image'
                ),
                Div(
                    H2(
                        'Eat Healthy, Stay',
                        Span('Healthy'),
                        cls='section__header'
                    ),
                    P('At Food Plaza, we believe that good food is the foundation of a\r\n            healthy life. Our meals are crafted with fresh ingredients and\r\n            balanced nutrition, helping you maintain a healthy lifestyle while\r\n            enjoying delicious flavors.'),
                    Div(
                        Button(
                            'Read More',
                            Span(
                                I(cls='ri-arrow-right-line')
                            ),
                            cls='btn'
                        ),
                        cls='banner__btn'
                    ),
                    cls='banner__content'
                ),
                cls='section__container banner__container'
            ),
            id='cart',
            cls='banner'
        ),
        Section(
            Div(
                Img(src='/static/assets/customer.png', alt='customer'),
                cls='customer__image'
            ),
            Div(
                H2(
                    'Customers',
                    Span('Reaction'),
                    cls='section__header'
                ),
                Div(
                    Div(
                        Div(
                            Div(
                                Div(
                                    Div('Verified Purchase'),
                                    Span('23 Oct 2024'),
                                    cls='customer__card__header'
                                ),
                                P('This is my go-to choice for healthy meals on busy days. I\r\n                  appreciate how they balance flavor with nutrition, making it\r\n                  easy to stick to my healthy eating goals while still enjoying\r\n                  delicious food.'),
                                Div(
                                    Img(src='/static/assets/customer-1.jpg', alt='customer'),
                                    Div(
                                        H4('Sarah Johnson'),
                                        H5('Nutritionist'),
                                        Div(
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            Span(
                                                I(cls='ri-star-half-fill')
                                            ),
                                            cls='customer__rating'
                                        )
                                    ),
                                    cls='customer__card__footer'
                                ),
                                cls='customer__card'
                            ),
                            cls='swiper-slide'
                        ),
                        Div(
                            Div(
                                Div(
                                    Div('Verified Purchase'),
                                    Span('15 Nov 2024'),
                                    cls='customer__card__header'
                                ),
                                P("I love the convenience and variety that they offers. The\r\n                  real-time order tracking is such a thoughtful feature—it\r\n                  ensures I never have to wonder about my meal's status."),
                                Div(
                                    Img(src='/static/assets/customer-2.jpg', alt='customer'),
                                    Div(
                                        H4('Rajesh Patel'),
                                        H5('Software Engineer'),
                                        Div(
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            cls='customer__rating'
                                        )
                                    ),
                                    cls='customer__card__footer'
                                ),
                                cls='customer__card'
                            ),
                            cls='swiper-slide'
                        ),
                        Div(
                            Div(
                                Div(
                                    Div('Verified Purchase'),
                                    Span('23 Nov 2024'),
                                    cls='customer__card__header'
                                ),
                                P("The dishes are not only flavorful but also packed with\r\n                  nutrients, which is essential for my active lifestyle. It's a\r\n                  fantastic option for anyone who values healthy eating!"),
                                Div(
                                    Img(src='/static/assets/customer-3.jpg', alt='customer'),
                                    Div(
                                        H4('Emily Brown'),
                                        H5('Fitness Trainer'),
                                        Div(
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            Span(
                                                I(cls='ri-star-fill')
                                            ),
                                            Span(
                                                I(cls='ri-star-half-fill')
                                            ),
                                            cls='customer__rating'
                                        )
                                    ),
                                    cls='customer__card__footer'
                                ),
                                cls='customer__card'
                            ),
                            cls='swiper-slide'
                        ),
                        cls='swiper-wrapper'
                    ),
                    Div(
                        Button(
                            I(cls='ri-arrow-left-line'),
                            cls='btn swiper-prev'
                        ),
                        Button(
                            I(cls='ri-arrow-right-line'),
                            cls='btn swiper-next'
                        ),
                        cls='customer__swiper__controls'
                    ),
                    cls='swiper'
                ),
                cls='customer__content'
            ),
            cls='section__container customer__container'
        ),
        Footer(
            Div(
                Div(
                    A(
                        Img(src='/static/assets/Mindara.png', alt='logo'),
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
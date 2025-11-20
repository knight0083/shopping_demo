# The demo app doesn't have a search bar; instead we validate product visibility on home
from pages.home_page import HomePage

def test_products_visible_on_home(browser, base_url):
    home = HomePage(browser, base_url).open_home()
    items = home.list_products()
    assert len(items) >= 1
    assert "Laptop" in items[0].text
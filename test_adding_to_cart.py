def test_adding_to_cart(page):
    all_products = page.locator("a[href='/products']")
    all_products.click()
    page.wait_for_url("https://automationexercise.com/products")
    assert page.url == "https://automationexercise.com/products"

    buy_kids_dress = page.locator("a[data-product-id='22']").first
    buy_kids_dress.click()

    added_notice = page.locator(".modal-header:has-text('Added!')")
    added_notice.wait_for(state="visible")
    assert added_notice.is_visible()
    view_cart = page.locator("a[href='/view_cart'] > u")
    view_cart.click()
    page.wait_for_url("https://automationexercise.com/view_cart")
    assert page.url == "https://automationexercise.com/view_cart"

    cart_details = page.locator("a[href='/product_details/22']")
    assert cart_details.is_visible()

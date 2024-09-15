def test_the_dress_category(page):
    women_category = page.locator("a:has-text('Women')")
    women_category.wait_for(state="visible")
    women_category.click()
    sub_category = page.locator("a[href='/category_products/1']")
    sub_category.click()
    page.wait_for_url("https://automationexercise.com/category_products/1")
    assert page.url == "https://automationexercise.com/category_products/1"

    add_to_cart = page.locator("a:has-text('Add to cart')").count()
    assert add_to_cart > 0
    
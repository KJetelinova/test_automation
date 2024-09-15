def test_sign_up_new_user(page_cleanup):
    sign_up_page = page_cleanup.locator("a[href='/login']")
    sign_up_page.click()
    page_cleanup.wait_for_url("https://automationexercise.com/login")
    assert page_cleanup.url == "https://automationexercise.com/login"

    page_cleanup.fill("input[type='text']", "Kate")
    page_cleanup.fill("input[data-qa='signup-email']", "kate@fakemail.com")
    sign_up_button = page_cleanup.locator("button[type='submit']:has-text('Signup')")
    sign_up_button.click()
    page_cleanup.wait_for_url("https://automationexercise.com/signup")
    assert page_cleanup.url == "https://automationexercise.com/signup"

    page_cleanup.fill("#password", "THISismyPassw0rd")
    page_cleanup.fill("#first_name", "Kate")
    page_cleanup.fill("#last_name", "Bird")
    page_cleanup.fill("#address1", "Tree Ave. 33")
    page_cleanup.get_by_label("country").select_option("Australia")
    page_cleanup.fill("#state", "New South Wales")
    page_cleanup.fill("#city", "Sydney")
    page_cleanup.fill("#zipcode", "2055")
    page_cleanup.fill("#mobile_number", "0411 234 567")
    create_account = page_cleanup.locator("button[data-qa='create-account']")
    create_account.click()
    page_cleanup.wait_for_url("https://automationexercise.com/account_created")
    assert page_cleanup.url == "https://automationexercise.com/account_created"
    success = page_cleanup.locator("h2:has-text('Account Created!')")
    assert success.is_visible()

    continue_button = page_cleanup.locator("a[data-qa='continue-button']")
    continue_button.click()
    page_cleanup.wait_for_url("https://automationexercise.com/")
    assert page_cleanup.url == "https://automationexercise.com/"
    logged_in = page_cleanup.locator("a:has-text('Logged in as')")
    assert logged_in.is_visible()
    logout = page_cleanup.locator("a[href='/logout']")
    assert logout.is_visible()

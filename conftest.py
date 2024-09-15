import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://automationexercise.com/")
        accept_cookies = page.locator("button.fc-button.fc-cta-consent.fc-primary-button")
        if accept_cookies.is_visible():
            accept_cookies.click()
        else:
            print("No need to accept cookies this time")
        yield page
        page.close()
        browser.close()


@pytest.fixture(scope='function')
def page_cleanup(page):
    yield page
    delete_user = page.locator("a[href='/delete_account']")
    if delete_user.is_visible():
        delete_user.click()
        page.wait_for_url("https://automationexercise.com/delete_account")

        deleted_account = page.locator("h2:has-text('Account Deleted!')")
        expect(deleted_account).to_be_visible()
        continue_button = page.locator("a[data-qa='continue-button']")
        continue_button.click()
        page.wait_for_url("https://automationexercise.com/")

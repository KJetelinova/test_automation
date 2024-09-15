def test_contact_form(page):
    contact_form = page.locator("a[href='/contact_us']")
    contact_form.click()
    page.wait_for_url("https://automationexercise.com/contact_us")
    assert page.url == "https://automationexercise.com/contact_us"

    page.fill("input[data-qa='name']", "Kate")
    page.fill("input[data-qa='email']", "kate@fakemail.com")
    page.fill("input[data-qa='subject']", "New Dress")
    page.fill("#message",
              "Hello, would it be possible to stock up the dress (or a similar ones) that I am sending you in the "
              "attachment?\nThank you, Kate")
    upload_file = page.locator("input[type='file']")
    upload_file.set_input_files('new_dress.jpg')
    send_it = page.locator("input[data-qa='submit-button']")
    page.on("dialog", lambda dialog: dialog.accept())
    send_it.click()
    success = page.locator("div.status.alert.alert-success:has-text('Success! Your details have been submitted "
                           "successfully.')")
    assert success.is_visible()

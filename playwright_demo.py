from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=r"C:\Users\chakr\AppData\Local\Chromium\Application\chrome.exe")
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the website you want to retrieve the DOM from
    page.goto('https://google.co.in')

    # Get the DOM content
    dom = page.content()

    # Output the DOM content
    print(dom)

    # Close the browser
    browser.close()

from playwright.sync_api import Playwright, sync_playwright, expect


def amazon_1st_item(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    page.get_by_placeholder("Search Amazon.in").fill("notebook")
    page.get_by_placeholder("Search Amazon.in").press("Enter")
    page.locator(".puis-card-container > div").first.get_by_role("link").first.click()
    page.wait_for_timeout(8000)
    # ---------------------


def amazon_2nd_item(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    page.get_by_placeholder("Search Amazon.in").fill("notebook")
    page.get_by_placeholder("Search Amazon.in").press("Enter")
    page.locator(
        "div:nth-child(8) > .sg-col-inner > .s-widget-container > div > div > span > .puis-card-container"
    ).click()
    page.wait_for_timeout(8000)
    # --------------------------


def amazon_3rd_item(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    page.get_by_placeholder("Search Amazon.in").fill("notebook")
    page.get_by_placeholder("Search Amazon.in").press("Enter")
    page.locator(
        "div:nth-child(9) > .sg-col-inner > .s-widget-container > div > div > span > .puis-card-container"
    ).click()
    page.wait_for_timeout(8000)
    # ------------------------------


def amazon_4th_item(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    page.get_by_placeholder("Search Amazon.in").fill("notebook")
    page.get_by_placeholder("Search Amazon.in").press("Enter")
    page.locator(
        "div:nth-child(10) > .sg-col-inner > .s-widget-container > div > div > span > .puis-card-container"
    ).click()
    page.wait_for_timeout(8000)
    # -----------------------


def amazon_1st_item_with_price_filter(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    page.get_by_placeholder("Search Amazon.in").fill("lamp")
    page.get_by_placeholder("Search Amazon.in").press("Enter")
    page.get_by_role("link", name="Under ₹").click()
    page.locator(".a-section > div:nth-child(2) > div:nth-child(2)").first.click()
    page.wait_for_timeout(10000)
    # ---------------------


def amazon_1st_item_with_price_range(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    page.get_by_placeholder("Search Amazon.in").fill("lamp")
    page.get_by_placeholder("Search Amazon.in").press("Enter")
    page.get_by_placeholder("Min").click()
    page.get_by_placeholder("Min").fill("1000")
    page.get_by_placeholder("Max").click()
    page.get_by_placeholder("Max").fill("2000")
    page.get_by_label("Price", exact=True).get_by_label("Go").click()
    page.locator(".a-section > div:nth-child(2) > div").first.click()
    page.wait_for_timeout(10000)

    # ---------------------


def amazon_1st_item_with_brand_filter(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    page.get_by_placeholder("Search Amazon.in").fill("lamp")
    page.get_by_placeholder("Search Amazon.in").press("Enter")
    page.get_by_role("link", name="Homesake", exact=True).click()
    page.locator(".a-section > div:nth-child(2) > div").first.click()

    page.wait_for_timeout(10000)
    # ---------------------


def amazon_add_to_cart(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    page.get_by_placeholder("Search Amazon.in").fill("notebook")
    page.get_by_placeholder("Search Amazon.in").press("Enter")
    with page.expect_popup() as page1_info:
        page.locator(".puis-card-container > div").first.get_by_role(
            "link"
        ).first.click()
    page1 = page1_info.value
    page1.get_by_label("Add to Cart").click()
    page.wait_for_timeout(10000)


def amazon_color_selection(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    page.get_by_placeholder("Search Amazon.in").fill("t-shirts for men")
    page.get_by_placeholder("Search Amazon.in").press("Enter")
    with page.expect_popup() as page1_info:
        page.locator(".puis-card-container > div").first.get_by_role(
            "link"
        ).first.click()
    page1 = page1_info.value
    page1.get_by_role("button", name="Wine").click()
    page1.get_by_title("Add to Shopping Cart").click()

    page.wait_for_timeout(10000)
    # ---------------------


with sync_playwright() as playwright:
    amazon_2nd_item(playwright)

"""
import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://whatsmyuseragent.org")
        print(await page.title())

        try:
            while True:
                # Keep the browser open until the user presses Escape
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            # Handle the cancellation when the user presses Escape
            pass
        finally:
            await browser.close()


asyncio.run(main())"""

""" amazon case 1: Amazon 1st item notebook selection
import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.amazon.in/")
    await page.get_by_placeholder("Search Amazon.in").fill("notebook")
    await page.get_by_placeholder("Search Amazon.in").press("Enter")
    await page.locator(".puis-card-container > div").first.get_by_role(
        "link"
    ).first.click()

    # ---------------------
    await asyncio.sleep(10)
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())"""

"""# amazon case 2: amazon order 2nd item
import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.amazon.in/")
    await page.get_by_placeholder("Search Amazon.in").fill("lamp")
    await page.get_by_placeholder("Search Amazon.in").press("Enter")
    async with page.expect_popup() as page1_info:
        await page.locator(
            "div:nth-child(8) > .sg-col-inner > .s-widget-container > div > div > span > .puis-card-container"
        ).click()
    page1 = await page1_info.value

    # ---------------------
    await asyncio.sleep(100)


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())"""

"""# amazon case 3:amazon order third item

import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.amazon.in/")
    await page.get_by_placeholder("Search Amazon.in").fill("lamp")
    await page.get_by_placeholder("Search Amazon.in").press("Enter")
    async with page.expect_popup() as page1_info:
        await page.locator(
            "div:nth-child(9) > .sg-col-inner > .s-widget-container > div > div > span > .puis-card-container"
        ).click()
    page1 = await page1_info.value

    # ---------------------
    await asyncio.sleep(100)


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())"""

"""# amazon case 4: ordering fourth item
import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.amazon.in/")
    await page.get_by_placeholder("Search Amazon.in").fill("lamp")
    await page.get_by_placeholder("Search Amazon.in").press("Enter")
    async with page.expect_popup() as page1_info:
        await page.locator(
            "div:nth-child(10) > .sg-col-inner > .s-widget-container > div > div > span > .puis-card-container"
        ).click()
    page1 = await page1_info.value

    # ---------------------
    await asyncio.sleep(60)


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())"""


"""# youtube case 1: play the first video in youtube by searching for cars

import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.youtube.com/")
    await page.get_by_placeholder("Search").fill("cars")
    await page.get_by_role("button", name="Search", exact=True).click()
    await page.locator("ytd-video-renderer").first.get_by_role("link").first.click()

    # ---------------------
    await asyncio.sleep(100)


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())"""

# youtube case 2: open youtube search for cars and play the first video from "people also watch section"

"""import asyncio
from playwright.async_api import Playwright, async_playwright, expect


async def runyoutube(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.youtube.com/")
    await page.get_by_placeholder("Search").fill("cars")
    await page.get_by_role("button", name="Search", exact=True).click()

    # Wait for the search results to load
    await page.wait_for_selector("ytd-video-renderer")

    # Click on the second video in the search results
    await page.locator("ytd-video-renderer:nth-child(1)").click()

    # ---------------------
    await asyncio.sleep(60)


async def main() -> None:
    async with async_playwright() as playwright:
        await runyoutube(playwright)


asyncio.run(main())"""

# spotify case 1: open spotify and play song "life"
"""
import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://open.spotify.com/?")
    await page.get_by_test_id("root").get_by_label("Search").click()
    await page.get_by_test_id("search-input").fill("hall of fame by script")
    await page.get_by_test_id("search-input").press("Enter")
    await page.get_by_role("checkbox", name="Songs").click()
    await page.locator(
        'div[role="row"][aria-rowindex="2"] div[data-testid="tracklist-row"]'
    ).click()
    await page.wait_for_selector(
        'div[role="row"][aria-rowindex="2"] div[data-testid="tracklist-row"]'
    )

    # Click on the first track in the search results
    await page.locator(
        'div[role="row"][aria-rowindex="2"] div[data-testid="tracklist-row"]'
    ).click()

    await page.get_by_test_id("play-button").click()
    # ---------------------
    await asyncio.sleep(40)


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
"""
# This test is meant to be a simple end-to-end integration test for Spotify Web API. It opens up Spotify and searches for Hall Of Fame by Script (a song)

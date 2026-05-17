from playwright.sync_api import sync_playwright
import re
import json

BASE = "https://www.anytimefitness.co.jp"

def get_slugs(page):
    page.goto(BASE + "/shop/")
    page.wait_for_timeout(3000)

    html = page.content()

    slugs = re.findall(r"/shop/([a-z0-9\-]+)/", html)
    return list(set(slugs))


def scrape_shop(page, slug):
    url = f"{BASE}/shop/{slug}/"
    page.goto(url)
    page.wait_for_timeout(1500)

    html = page.content()

    price = re.search(r"¥\s?[0-9,]+", html)
    address = re.search(r"〒\d{3}-\d{4}.*?東京都.*?(?=<)", html)

    return {
        "slug": slug,
        "url": url,
        "price": price.group(0) if price else None,
        "address": address.group(0) if address else None
    }


def run():
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        slugs = get_slugs(page)

        print("shops:", len(slugs))

        for i, slug in enumerate(slugs):
            try:
                data = scrape_shop(page, slug)
                results.append(data)
                print(i, slug)
            except Exception as e:
                print("error:", slug, e)

        browser.close()

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    run()

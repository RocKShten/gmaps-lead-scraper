import csv
from playwright.sync_api import sync_playwright

data = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.google.com/maps")

    page.wait_for_selector("input.UGojuc")

    page.fill("input.UGojuc", "Кофейни Алматы")
    page.press("input.UGojuc", "Enter")

    
    page.wait_for_selector("a.hfpxzc")
    
    for _ in range(5):
        cards = page.query_selector_all("a.hfpxzc")

        if not cards:
            break

        last_card = cards[-1]
        last_card.scroll_into_view_if_needed()

        page.wait_for_timeout(3000)
    final_cards = page.query_selector_all("a.hfpxzc")
    for card in final_cards:
            card.click()
            page.wait_for_timeout(1500)


            title = card.get_attribute("aria-label")
            adress = page.query_selector('button[data-item-id="address"]')
            number = page.query_selector('button[data-item-id^="phone:tel"]')
            if adress:
                adress_text = adress.inner_text().strip()
            else:
                adress_text = "Адрес не найден"
            if number:
                number_text = number.inner_text().strip()
            else:
                number_text = "Номер не найден"

            card_link = page.url
            if title and card_link:
                data.append([title, card_link, adress_text, number_text])


    browser.close()


with open("leads.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Название","Ссылка","Адрес","Номер телефона"])
    for title, card_link, adress_text, number_text in data:
        writer.writerow([title, card_link, adress_text, number_text])
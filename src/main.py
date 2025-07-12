import sys
from botasaurus.browser import browser, Driver

@browser
def scrape_heading_task(driver: Driver, url):
    driver.get(url)

    heading = driver.get_text("h1")

    return {
        "heading" : heading
    }

scrape_heading_task("https://zapimoveis.com.br")

from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from tools.models import Tool, Category

class Command(BaseCommand):
    help = "Import tools from aixploria list page (demo)"

    def handle(self, *args, **options):
        url = "https://www.aixploria.com/en/"  # example; adapt for pages you scrape
        resp = requests.get(url, headers={"User-Agent":"aixclone-bot/1.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        cards = soup.select(".item-card")  # <-- update selector to real site
        for c in cards:
            name = c.select_one(".card-title").get_text(strip=True)
            link = c.select_one("a")['href']
            desc = c.select_one(".card-desc").get_text(strip=True) if c.select_one(".card-desc") else ""
            cat_name = c.select_one(".cat-name").get_text(strip=True) if c.select_one(".cat-name") else "Uncategorized"
            cat, _ = Category.objects.get_or_create(name=cat_name)
            if not Tool.objects.filter(website=link).exists():
                t = Tool.objects.create(name=name, website=link, short_description=desc, category=cat, external_id=link)
                self.stdout.write(self.style.SUCCESS(f"Imported {name}"))
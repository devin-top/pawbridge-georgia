import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
PAGES=("index.html","mission.html","services.html","project.html","faq.html","privacy.html","work.html","thanks.html","404.html")

class Tags(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.forms=[]; self.fields=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag in ("a","link") and d.get("href"): self.links.append(d["href"])
        if tag in ("script","img") and d.get("src"): self.links.append(d["src"])
        if tag=="form": self.forms.append(d)
        if tag in ("input","select","textarea") and d.get("name"): self.fields.append(d["name"])

class SiteTests(unittest.TestCase):
    def test_pages_and_assets(self):
        for name in PAGES: self.assertTrue((ROOT/name).is_file(),name)
        for page in PAGES:
            tags=Tags(); tags.feed((ROOT/page).read_text(encoding="utf-8"))
            for url in tags.links:
                if url.startswith(("#","mailto:","tel:","https:","http:")): continue
                p=urlparse(url).path
                if not p or p=="/": continue
                asset=ROOT/p.lstrip("/") if p.startswith("/") else ROOT/p
                self.assertTrue(asset.is_file(), f"{page} -> {url}")
    def test_netlify_form_markup(self):
        tags=Tags(); tags.feed((ROOT/"index.html").read_text(encoding="utf-8"))
        self.assertEqual(len(tags.forms),1)
        form=tags.forms[0]
        for key,val in (("name","pawbridge-inquiries"),("method","POST"),("data-netlify","true"),("action","/thanks.html")):
            self.assertEqual(form.get(key),val)
        for field in ("form-name","name","email","type","message","bot-field"):
            self.assertIn(field,tags.fields)
    def test_404_and_response_handling(self):
        self.assertIn("Page not found",(ROOT/"404.html").read_text())
        js=(ROOT/"assets/js/contact.js").read_text()
        self.assertIn("response.ok",js)
        self.assertIn("application/x-www-form-urlencoded",js)

if __name__=="__main__":unittest.main()

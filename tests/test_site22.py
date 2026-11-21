import unittest
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ("website-concept.svg", "campaign-concept.svg", "social-concept.svg")
PAGES = ("index.html", "mission.html", "services.html", "project.html",
         "faq.html", "privacy.html", "404.html", "thanks.html", "work.html")

class Inspector(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]; self.images=[]; self.forms=[]
    def handle_starttag(self,tag,attrs):
        attributes=dict(attrs)
        if tag=="a": self.refs.append(attributes.get("href",""))
        if tag=="img": self.images.append(attributes)
        if tag=="form": self.forms.append(attributes)

class PortfolioTests(unittest.TestCase):
    def test_portfolio_and_art(self):
        for asset in ASSETS:
            source=(ROOT/"assets/concepts"/asset).read_text(encoding="utf-8")
            self.assertIn("<svg",source)
            self.assertIn("</svg>",source)
        for path in ("index.html","work.html"):
            html=(ROOT/path).read_text(encoding="utf-8")
            parser=Inspector(); parser.feed(html)
            self.assertIn("illustrative concepts",html.lower()) if path=="index.html" else self.assertIn("self-initiated samples",html.lower())
            self.assertEqual(sum("concepts/" in image.get("src","") for image in parser.images),3)
            for image in parser.images: self.assertTrue(image.get("alt"),path)
            for category in ("website","campaign","social"):
                self.assertIn(f'data-category="{category}"',html)
                self.assertIn(f'data-filter="{category}"',html)
    def test_navigation_and_sitemap(self):
        for page in PAGES:
            html=(ROOT/page).read_text(encoding="utf-8")
            self.assertIn('href="/work.html"',html)
        self.assertIn("work.html",(ROOT/"sitemap.xml").read_text(encoding="utf-8"))
    def test_existing_form_contract(self):
        html=(ROOT/"index.html").read_text(encoding="utf-8")
        self.assertIn('name="pawbridge-inquiries"',html)
        self.assertIn('action="/thanks.html"',html)
        self.assertIn('data-netlify="true"',html)
        self.assertIn('src="/assets/js/contact.js"',html)

if __name__=="__main__":
    unittest.main()

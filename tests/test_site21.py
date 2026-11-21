import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ("index.html", "mission.html", "services.html", "project.html",
         "faq.html", "privacy.html", "work.html", "thanks.html", "404.html")
STYLES = ("tokens.css", "site.css", "pages.css", "theme.css")

class Inspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.nav = []
        self.images = []
        self.forms = []
        self._in_nav = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"): self.ids.append(attrs["id"])
        if tag == "nav": self.nav.append(attrs.get("aria-label", ""))
        if tag in ("a", "link") and attrs.get("href"): self.links.append(attrs["href"])
        if tag == "img": self.images.append(attrs)
        if tag == "form": self.forms.append(attrs)

class Site21Tests(unittest.TestCase):
    def test_shared_shell_and_navigation(self):
        for page in PAGES:
            with self.subTest(page=page):
                html = (ROOT/page).read_text(encoding="utf-8")
                parsed = Inspector(); parsed.feed(html)
                self.assertIn("Main navigation", parsed.nav)
                self.assertIn("Mobile navigation", parsed.nav)
                self.assertIn("Footer navigation", parsed.nav)
                self.assertIn("main", parsed.ids)
                self.assertIn("mobile-nav", parsed.ids)
                self.assertIn("#main", parsed.links)
                self.assertIn("/mission.html", parsed.links)
                self.assertIn("/services.html", parsed.links)
                self.assertIn("/project.html", parsed.links)
                self.assertIn("/faq.html", parsed.links)
                self.assertIn("/privacy.html", parsed.links)
                self.assertIn("/#contact", parsed.links)
                for style in STYLES:
                    self.assertIn("/assets/css/"+style, parsed.links)
                self.assertIn("/assets/js/site.js", html)
                self.assertEqual(len(parsed.ids), len(set(parsed.ids)), "Repeated IDs in "+page)

    def test_form_preserved(self):
        html = (ROOT/"index.html").read_text(encoding="utf-8")
        parsed = Inspector(); parsed.feed(html)
        self.assertEqual(len(parsed.forms), 1)
        form = parsed.forms[0]
        self.assertEqual(form.get("name"), "pawbridge-inquiries")
        self.assertEqual(form.get("method"), "POST")
        self.assertEqual(form.get("data-netlify"), "true")
        self.assertEqual(form.get("action"), "/thanks.html")
        self.assertIn('name="bot-field"', html)
        self.assertIn('name="form-name" value="pawbridge-inquiries"', html)
        self.assertIn('/assets/js/contact.js', html)
        self.assertIn('neostorys@gmail.com', html)

    def test_accessible_components(self):
        html=(ROOT/"index.html").read_text(encoding="utf-8")
        parsed=Inspector(); parsed.feed(html)
        self.assertIn("assets/hero-botanical.svg", html)
        for img in parsed.images:
            self.assertTrue(img.get("alt"), "Images require alt")
        self.assertIn('aria-live="polite"',html)
        self.assertIn('aria-pressed=', html)

    def test_css_layers_and_tokens(self):
        for style in STYLES:
            self.assertTrue((ROOT/"assets/css"/style).is_file())
        tokens=(ROOT/"assets/css/tokens.css").read_text(encoding="utf-8")
        self.assertIn(":root",tokens)
        for value in ("--ink","--cream","--paper","--muted","--brand-accent"):
            self.assertIn(value,tokens)
        for style in ("site.css","pages.css","theme.css"):
            css=(ROOT/"assets/css"/style).read_text(encoding="utf-8")
            self.assertNotIn(":root{",css)
            self.assertNotIn(":root {",css)
        js=(ROOT/"assets/js/site.js").read_text(encoding="utf-8")
        self.assertIn('if (menuToggle && mobileNav)',js)
        self.assertIn('if (year)',js)

def luminance(hexcode):
    channels = [int(hexcode[x:x+2],16)/255 for x in (1,3,5)]
    channels = [c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4 for c in channels]
    return sum(x*y for x,y in zip(channels,(0.2126,0.7152,0.0722)))

class ContrastTests(unittest.TestCase):
    def test_base_body_contrast(self):
        tokens=(ROOT/"assets/css/tokens.css").read_text(encoding="utf-8")
        values=dict(re.findall(r"(--[\w-]+):\s*(#[0-9a-fA-F]{6})",tokens))
        for bg in ("--cream","--paper"):
            for fg in ("--ink","--ink2","--muted"):
                one,two=sorted([luminance(values[bg]),luminance(values[fg])])
                ratio=(two+0.05)/(one+0.05)
                self.assertGreaterEqual(ratio,4.5,(bg,fg,ratio))

if __name__=="__main__":
    unittest.main()

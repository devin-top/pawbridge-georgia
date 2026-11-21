# PawBridge — Design for Second Chances 🐾

**Independent early-stage animal rescue support project based in Georgia.**

PawBridge helps animal shelters and rescue groups improve their visibility through accessible websites, adoption campaigns, and AI-assisted creative content. The project is currently a public **static website prototype**, with a proposed roadmap toward a fuller shelter-support platform.

- **Live website:** https://pawbridge-georgia.netlify.app/
- **Source code:** https://github.com/devin-top/pawbridge-georgia
- **Contact:** neostorys@gmail.com

## Why PawBridge?

Rescue organizations often have limited time and resources to tell the stories of animals looking for homes. PawBridge explores how practical web design, accessible communication, and carefully reviewed AI assistance can help these organizations reach more potential adopters and supporters.

## What works today

- Responsive, English-language landing page
- Information about the mission and creative services
- Clearly labeled sample campaign and website concepts (not real adoption listings)
- Public contact email
- Contact form markup, client-side failure handling, a custom thank-you page, and a custom 404 page
- Hosting on Netlify

**Note:** Form submissions and email notifications must be enabled and tested in the Netlify project dashboard before they are treated as operational.

## Tech stack — current

- HTML5, modular CSS, vanilla JavaScript
- Local SVG illustrations and assets
- Netlify static hosting and Netlify Forms integration markup
- GitHub for source control

## Roadmap — proposed, not yet implemented

1. Migrate the frontend to React/Next.js with TypeScript.
2. Create a PostgreSQL data model for shelters and adoptable animals.
3. Add authentication and role-based access for participating shelters.
4. Build animal listings and a shelter management dashboard.
5. Add adoption inquiry management and privacy safeguards.
6. Integrate human-reviewed AI assistance for descriptions and outreach campaigns.
7. Pilot the platform with interested rescue organizations after partnerships are confirmed.

For more detail, see [ARCHITECTURE.md](ARCHITECTURE.md) and [ROADMAP.md](ROADMAP.md).

## Running the current prototype locally

Clone the repository:

```bash
git clone https://github.com/devin-top/pawbridge-georgia.git
cd pawbridge-georgia
```

For correct absolute asset URLs, serve it locally:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

The site includes additional pages: Mission, Services, Project, FAQ and Privacy. CSS and JavaScript live in `assets/css` and `assets/js`. The static site does not need a build step. Netlify Forms submission handling only works when the site is deployed to a correctly configured Netlify project.

## How Devin could help

This project is an appropriate starting point for incremental engineering tasks: restructuring the frontend, adding a database and tests, developing a secure dashboard, and creating an accessible, maintainable deployment process. The goal is to keep humans responsible for animal profile accuracy, privacy, and final publication of AI-generated materials.

## Project status and transparency

PawBridge is an **independent early-stage initiative**, not a claim of an officially registered nonprofit or established shelter network. Visual concepts shown on the website are examples and do not represent confirmed partnerships, completed adoptions, or measured impact.

## Contact

For collaboration inquiries: **neostorys@gmail.com**

## Deployment and form verification

See [Netlify deployment instructions](docs/DEPLOYMENT.md). If the contact form fails, follow [Netlify form troubleshooting](docs/FORM-TROUBLESHOOTING.md). A published thank-you page is not proof that Netlify stored a form submission.

## Quality checks

Run `python3 -m unittest discover -s tests -v` to check core pages, paths and HTML form structure. GitHub Actions runs the same checks on each pull request.

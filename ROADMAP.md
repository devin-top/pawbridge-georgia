# PawBridge — Development Roadmap

This roadmap is a plan for future development, not a list of completed features.

## Completed: prototype

- [x] Design initial brand and landing page.
- [x] Create responsive static pages and example creative concepts.
- [x] Publish source code to a public GitHub repository.
- [x] Publish the static site to Netlify.
- [x] Add public contact email and form markup to GitHub source.

## Immediate verification

- [x] Deploy GitHub `main` to Netlify production.
- [x] Verify `neostorys@gmail.com` is visible on the live website.
- [x] Verify Netlify Forms detects `pawbridge-inquiries`.
- [x] Submit a test message and confirm it appears in Netlify Forms.
- [ ] Verify new-message email notifications reach the intended inbox; submission capture was confirmed separately.
- [x] Set GitHub repository description and homepage URL.

## PawBridge 2.1: design system

- [x] Add common site-wide navigation and footer design.
- [x] Centralize accessible color tokens and split CSS into logical layers.
- [x] Add regression checks for all eight pages and the unchanged contact form.
- [ ] Manually verify mobile menus and contrast in a deployed browser.
- [ ] Verify form capture and email notifications after deployment.

## Phase 1: frontend engineering

- [ ] Refactor static files into maintainable React / Next.js components.
- [ ] Introduce TypeScript, formatting and linting.
- [ ] Add automated accessibility and mobile navigation checks.
- [x] Add CI checks on pull requests.

## Phase 2: shelter and animal directory

- [ ] Define data schema and authorization rules.
- [ ] Add a mock animal directory with clearly labeled sample data.
- [ ] Build a private dashboard for shelter-managed animal profiles.
- [ ] Introduce image upload, review and publishing workflow.

## Phase 3: adoption inquiry workflow

- [ ] Design consent, data minimization and retention policies.
- [ ] Implement inquiry routing and staff notifications.
- [ ] Test access restrictions and audit logging.

## Phase 4: AI-assisted creative support

- [ ] Draft adoption descriptions and multilingual campaign copy.
- [ ] Require human review before publication.
- [ ] Add content-safety and factual accuracy checks.

## Phase 5: pilot and evaluation

- [ ] Find interested organizations and confirm participation.
- [ ] Collect feedback, fix usability issues, document lessons learned.
- [ ] Measure agreed outcomes without inventing adoption counts or partners.

## PawBridge 2.2: portfolio and visual storytelling

- [x] Create a separate concept portfolio page and show three distinct creative directions.
- [x] Add reusable original SVG concept artwork and relevant imagery to selected secondary pages.
- [x] Keep sample work transparent and explicitly labeled.
- [ ] Confirm production Netlify deployment and browser view on desktop and mobile.
- [ ] Validate form capture after deployment (the form's code is unchanged).

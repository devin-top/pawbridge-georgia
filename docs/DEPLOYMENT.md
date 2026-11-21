# Deploy PawBridge to Netlify

Production URL: https://pawbridge-georgia.netlify.app/

## Preferred: connect the existing Netlify site to this GitHub repository
1. Open the EXISTING Netlify app `pawbridge-georgia` (do not create another site).
2. In site settings / build and deploy, connect `devin-top/pawbridge-georgia` as its Git repository if supported. Choose branch `main`, no build command, publish directory `.`.
3. If the site uses manual file-drop deployments, uploading to GitHub alone will NOT change the live website. Alternatively use a manual deploy from a downloaded repository folder.
4. In Netlify's Forms area, enable form detection if available. Netlify's new AI app editor may display Forms as "Not in use yet"; this is not proof it is enabled.
5. Redeploy AFTER enabling detection so Netlify scans the static HTML.
6. In Forms, confirm the form `pawbridge-inquiries` is registered.
7. Send a realistic test inquiry on the deployed website and verify it appears in verified submissions (check spam also).
8. Configure submission notification email to `neostorys@gmail.com` separately.
9. Open /thanks.html, /404-test, /privacy.html and the other pages. The thank-you page opening alone does NOT prove a form submission.

Official docs:
https://docs.netlify.com/manage/forms/setup/
https://docs.netlify.com/manage/forms/troubleshooting-tips/

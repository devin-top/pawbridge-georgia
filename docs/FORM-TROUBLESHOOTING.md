# Netlify Forms troubleshooting

The original site showed Netlify's generic 404 after contact form submission. That screenshot alone does not isolate whether form detection was disabled, a POST failed, or the success route was missing.

1. Verify /thanks.html is published.
2. Verify the deployed static index.html includes a form with name="pawbridge-inquiries", method="POST", data-netlify="true", and matching named inputs.
3. Enable form detection for the existing Netlify site, then redeploy.
4. Verify the form appears under Netlify Forms and test it with a real submission.
5. Look under Verified and Spam submissions; configure email notifications separately.
6. If AJAX POST returns an unsuccessful HTTP code, the user now sees an inline error and can write to neostorys@gmail.com instead.
7. If using manual deploys, GitHub updates alone do not change the live site.

Source: https://docs.netlify.com/manage/forms/setup/

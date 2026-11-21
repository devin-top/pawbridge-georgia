"use strict";
// Progressive enhancement: the HTML POST form remains available without JavaScript.
// This handler prevents an unhandled 404 from being shown after a failed AJAX request.
(() => {
  const form = document.getElementById("inquiry-form");
  if (!form) return;
  const status = document.getElementById("form-feedback");
  const submit = document.getElementById("form-submit");
  const label = submit.innerHTML;
  form.addEventListener("submit", async (event) => {
    if (!form.checkValidity()) return;
    event.preventDefault();
    status.classList.remove("form-error");
    status.textContent = "";
    submit.disabled = true;
    submit.textContent = "Sending…";
    form.setAttribute("aria-busy","true");
    try {
      const response = await fetch("/", {
        method: "POST",
        headers: {"Content-Type": "application/x-www-form-urlencoded"},
        body: new URLSearchParams(new FormData(form)).toString()
      });
      if (!response.ok) throw new Error("Submission returned HTTP " + response.status);
      window.location.assign("/thanks.html");
    } catch (error) {
      console.error("PawBridge contact form error:", error);
      status.classList.add("form-error");
      status.textContent = "Your message could not be sent. Please try again or email neostorys@gmail.com directly.";
      submit.disabled = false;
      submit.innerHTML = label;
      form.removeAttribute("aria-busy");
    }
  });
})();

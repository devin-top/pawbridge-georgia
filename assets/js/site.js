"use strict";
(() => {
  const menuToggle = document.querySelector(".menu-toggle");
  const mobileNav = document.getElementById("mobile-nav");
  if (menuToggle && mobileNav) {
    const closeMenu = (restoreFocus = false) => {
      const wasOpen = mobileNav.classList.contains("open");
      mobileNav.classList.remove("open");
      menuToggle.setAttribute("aria-expanded", "false");
      menuToggle.setAttribute("aria-label", "Open menu");
      if (restoreFocus && wasOpen) menuToggle.focus();
    };
    menuToggle.addEventListener("click", () => {
      const isOpen = mobileNav.classList.toggle("open");
      menuToggle.setAttribute("aria-expanded", String(isOpen));
      menuToggle.setAttribute("aria-label", isOpen ? "Close menu" : "Open menu");
    });
    mobileNav.querySelectorAll("a").forEach(link => link.addEventListener("click", () => closeMenu()));
    document.addEventListener("keydown", event => {
      if (event.key === "Escape") closeMenu(true);
    });
    document.addEventListener("click", event => {
      if (!event.target.closest(".header")) closeMenu();
    });
    window.addEventListener("resize", () => {
      if (window.innerWidth > 850) closeMenu();
    });
  }

  const filters = [...document.querySelectorAll(".filter")];
  const items = [...document.querySelectorAll(".work-item")];
  filters.forEach(button => button.addEventListener("click", () => {
    const filter = button.dataset.filter;
    filters.forEach(candidate => {
      const selected = candidate === button;
      candidate.classList.toggle("active", selected);
      candidate.setAttribute("aria-pressed", String(selected));
    });
    items.forEach(item => {
      item.hidden = filter !== "all" && item.dataset.category !== filter;
    });
  }));

  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();

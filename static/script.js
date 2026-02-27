console.log("Hello from JS");

const lightTheme = "/static/lightmode.css";
const darkTheme = "/static/darkmode.css";
const darkPic = "/static/images/cloud_dark.png";
const lightPic = "/static/images/cloud_light.png";

/* ── Runs immediately (script is in <head>) ──────────────
   Fixes the theme link before the browser paints — no flash. */
(function () {
  const saved = localStorage.getItem("theme");
  if (saved && saved.includes("darkmode.css")) {
    const link = document.getElementById("theme-style");
    if (link) link.setAttribute("href", darkTheme);
  }
})();

/* ── Apply a theme and sync all UI ───────────────────── */
function applyTheme(dark) {
  const themeLink = document.getElementById("theme-style");
  const image = document.getElementById("wordcloud");
  const track = document.getElementById("toggle-track");
  const label = document.getElementById("toggle-label");

  if (dark) {
    themeLink.setAttribute("href", darkTheme);
    if (image) image.setAttribute("src", darkPic);
    if (track) track.classList.add("active");
    if (label) label.textContent = "Dark";
    localStorage.setItem("theme", darkTheme);
  } else {
    themeLink.setAttribute("href", lightTheme);
    if (image) image.setAttribute("src", lightPic);
    if (track) track.classList.remove("active");
    if (label) label.textContent = "Light";
    localStorage.setItem("theme", lightTheme);
  }
}

/* ── Once DOM is ready: sync UI state + scroll-hide ─── */
document.addEventListener("DOMContentLoaded", function () {
  // Sync toggle switch UI to match whatever theme is active
  const savedTheme = localStorage.getItem("theme");
  const isDark = savedTheme ? savedTheme.includes("darkmode.css") : false;
  applyTheme(isDark);

  // Header is always visible
});

/* ── Toggle called by the switch ─────────────────────── */
function toggleTheme() {
  const themeLink = document.getElementById("theme-style");
  const currentlyDark = themeLink.getAttribute("href").includes("darkmode.css");
  applyTheme(!currentlyDark);
}

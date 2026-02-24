console.log("Hello from JS");

const lightTheme = "/static/lightmode.css";
const darkTheme = "/static/darkmode.css";

function toggleTheme() {
  const themeLink = document.getElementById("theme-style");

  if (themeLink.getAttribute("href").includes("lightmode.css")) {
    themeLink.setAttribute("href", darkTheme);
  } else {
    themeLink.setAttribute("href", lightTheme);
  }
}

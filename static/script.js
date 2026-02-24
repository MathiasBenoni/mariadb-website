console.log("Hello from JS");

const lightTheme = "/static/lightmode.css";
const darkTheme = "/static/darkmode.css";
const darkPic = "/static/images/cloud_dark.png";
const lightPic = "/static/images/cloud_light.png";

document.addEventListener("DOMContentLoaded", function () {
  const themeLink = document.getElementById("theme-style");
  const image = document.getElementById("wordcloud");

  const savedTheme = localStorage.getItem("theme");

  if (savedTheme) {
    themeLink.setAttribute("href", savedTheme);

    if (savedTheme.includes("darkmode.css")) {
      image.setAttribute("src", darkPic);
    } else {
      image.setAttribute("src", lightPic);
    }
  }
});

function toggleTheme() {
  const themeLink = document.getElementById("theme-style");
  const image = document.getElementById("wordcloud");

  if (themeLink.getAttribute("href").includes("lightmode.css")) {
    localStorage.setItem("theme", darkTheme);
    themeLink.setAttribute("href", darkTheme);
    image.setAttribute("src", darkPic);
  } else {
    localStorage.setItem("theme", lightTheme);
    themeLink.setAttribute("href", lightTheme);
    image.setAttribute("src", lightPic);
  }
}

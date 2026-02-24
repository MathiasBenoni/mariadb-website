console.log("Hello from JS");

const lightTheme = "/static/lightmode.css";
const darkTheme = "/static/darkmode.css";
const darkPic = "/static/images/cloud_dark.png";
const lightPic = "/static/images/cloud_light.png";

const image = document.getElementById("wordcloud");

console.log(image);

function toggleTheme() {
  const themeLink = document.getElementById("theme-style");

  if (themeLink.getAttribute("href").includes("lightmode.css")) {
    themeLink.setAttribute("href", darkTheme);
    image.setAttribute("src", darkPic);
  } else {
    themeLink.setAttribute("href", lightTheme);
    image.setAttribute("src", lightPic);
  }
}

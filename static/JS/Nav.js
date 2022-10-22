document.addEventListener("DOMContentLoaded", function (event) {
  const showNavbar = (toggleId, navId, bodyId, headerId) => {
    const toggle = document.getElementById(toggleId),
      nav = document.getElementById(navId),
      bodypd = document.getElementById(bodyId),
      headerpd = document.getElementById(headerId);

    // Validate that all variables exist
    if (toggle && nav && bodypd && headerpd) {
      toggle.addEventListener("click", () => {
        // show navbar
        nav.classList.toggle("show");
        // change icon
        toggle.classList.toggle("bx-x");
        // add padding to body
        bodypd.classList.toggle("body-pd");
        // add padding to header
        headerpd.classList.toggle("body-pd");
      });
    }
  };

  showNavbar("header-toggle", "nav-bar", "body-pd", "header");

  // Your code to run since DOM is loaded and ready
});

// const body
const body = document.querySelector("body");
// const html
const html = document.querySelector("html");
// const id nav-bar
const navbar = document.querySelector("#nav-bar");
Overflow = () => {
  // If navbar classList doesn't contain show
  console.log(!navbar.classList.contains("show"));
  if (!navbar.classList.contains("show")) {
    // If screen width is greater than 768px
    if (window.innerWidth <= 768) {
      html.style.overflow = "hidden";
      body.style.overflow = "hidden";
    }
  }
  else {
    html.style.overflow = "auto";
    body.style.overflow = "auto";
  }
};

WebsiteModeToggle = () => {
  const ModeIcon = document.querySelector(".header_img");

  body.classList.toggle("dark");
  if (ModeIcon.classList.contains("bx-sun")) {
    
    ModeIcon.classList.remove("bx-sun");
    ModeIcon.classList.add("bx-moon");
    ModeIcon.style.color = "white";
  }
  else {
    ModeIcon.classList.remove("bx-moon");
    ModeIcon.classList.add("bx-sun");
    ModeIcon.removeAttribute("style");
  }
}

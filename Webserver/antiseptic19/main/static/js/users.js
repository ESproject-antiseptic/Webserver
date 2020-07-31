const toggleBtn = document.querySelector(".nav-item dropdown");
const menu = document.querySelector(".dropdown_menu");

toggleBtn.addEventListener("click", () => {
  menu.classList.toggle("active");
});

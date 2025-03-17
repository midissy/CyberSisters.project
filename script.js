document.addEventListener("DOMContentLoaded", function () {
  const menuButton = document.querySelector(".header_right--mobile img");
  const menuList = document.querySelector(".header_right--mobile--list");

  menuButton.addEventListener("click", function (event) {
    menuList.style.transform = "translateX(0)";
    event.stopPropagation();
  });

  document.addEventListener("click", function (event) {
    if (
      !menuList.contains(event.target) &&
      !menuButton.contains(event.target)
    ) {
      menuList.style.transform = "translateX(100%)";
    }
  });
});

var nb = document.getElementById("nb");
var sticky = nb.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    nb.classList.add("scroll");
  } else {
    nb.classList.remove("scroll");
  }
}

window.onscroll = function () {
  myFunction();
};

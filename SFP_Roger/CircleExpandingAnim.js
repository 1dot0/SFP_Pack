
const circle = document.querySelector('.circle');
const max = 1500;
const min = 500;

// circle expands and change page
circle.addEventListener('click', function() {
  circle.style.width = "200vw";
  circle.style.height = "400vh";
  setTimeout(function() {
    window.location.href = "data.html";
  }, 150);
});

// eye closes
setInterval(
  () => {
    setTimeout(
      () => {
        circle.style.height = "0px"
        oval.style.height = "0px"
        setTimeout(
          () => {  
            circle.style.height = "150px"
            oval.style.height = "500px"
          },
          500
        );
      },
      2000
    );
  },
  20000
)

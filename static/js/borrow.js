$("#menu-toggle").click(function (e) {
  e.preventDefault();
  $("#wrapper").toggleClass("toggled");
});


// var checkboxes = document.querySelectorAll("input[type=checkbox][name=pricebox]");
// let final = []
// checkboxes.forEach(function(checkbox) {
//   checkbox.addEventListener('change', function() {
//     final = Array.from(checkboxes).filter(i => i.checked).map(i => i.value)
//     console.log(final)
//   })
// });

widg = document.getElementById('drager');
div = document.getElementById('widgets');


widg.addEventListener('click',(e)=>{
    e.preventDefault();
    if (div.style.display === "none") {
        div.style.display = "block";
        console.group('1');
      } else {
        div.style.display = "none";
      }
    
})

$(document).click(function() {
    div.style.display = "none";
});
$(widg).click(function(e) {
    e.stopPropagation(); // This is the preferred method.
    return false;        // This should not be used unless you do not want
                         // any click events registering inside the div
});


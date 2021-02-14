// change navbar color on condition
$(document).ready(function() {
    $("#nav-btn").click(function() {
        var value = $("#nav-btn").attr("aria-expanded");
        if (value == "false") {
            $(".navbar").addClass("navbar-color");
        } else {
            $(".navbar").removeClass("navbar-color");
        }
    });
});


// search button function
function serchBtn() {
    alert("Serch Button Function Executed");
}

// add nav bottom border on scroll
$(document).ready(function() {
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll >= 5) {
            $(".navbar").addClass("nav-shadow");
        } else {
            $(".navbar").removeClass("nav-shadow");
        }
    });
});
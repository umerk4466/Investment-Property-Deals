// Navbar

// add slide fade affact on navbar's dropdown menu
$(document).ready(function() {
    $('.dropdown-toggle').click(function() {
        $(this).next('.dropdown-menu').slideToggle("fast");
    });
});
// close dropdown menu if click outside of dropdown
$(document).on("click", function(event) {
    // var $trigger = $(".dropdown-toggle");
    // if ($trigger !== event.target && !$trigger.has(event.target).length) {
    $(".dropdown-menu").slideUp("fast");
    // }
});
$( document ).ready(function() {
    $('#id_min_price option:first').text('Min Price');
    $('#id_max_price option:first').text('Max Price');
    $('#id_min_bedroom option:first').text('Min Beds');
    $('#id_max_bedroom option:first').text('Max Beds');
});

function toggle_visibility(id) {
    var e = document.getElementById(id);
    if($(e.target).hasClass("hide-filter"))
        alert("s");
    //    e.addClass('display-filter');
    else
       e.style.display = 'block';
 }

// $('#filter-btn').click(function() {
//     $('#custom-modal').slideToggle("fast", function() {
//         // Animation complete.
//         // $('.filter-btn').css("background-color", "white");
//       });
// });

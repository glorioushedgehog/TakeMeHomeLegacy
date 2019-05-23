$(document).ready(function () {
    $('select').formSelect();
    $('.tabs').tabs();
    document.getElementById("image_search_loading_animation").style.display = "none";
    document.getElementById("image_search_loading_text").style.display = "none";
    $("#image_search_form").submit(showImageSearchLoadingAnimation);
});

function showImageSearchLoadingAnimation() {
    document.getElementById("image_search_loading_animation").style.display = "block";
    document.getElementById("image_search_loading_text").style.display = "block";
}

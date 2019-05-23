$(document).ready(function () {
    $("#prepare-for-fr-button").click(prepareForFacialRecognition);
});

function prepareForFacialRecognition() {
    $("#before-clicking-button").toggle(false);
    $("#after-clicking-button").toggle(true);
    const url = '/prepare_for_facial_recognition';
    $.ajax({
        method: 'GET',
        url: url,
    }).catch(function (error) {
        console.log(error);
    });
}

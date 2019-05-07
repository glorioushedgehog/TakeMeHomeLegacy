$(document).ready(function () {
    $('.modal').modal();
    document.getElementById("search_error").style.display = "none";
    const inference_task_id = document.getElementsByName("inference_task_id")[0].value.trim();
    if (inference_task_id !== "") {
        console.log("found inference task id: " + inference_task_id);
        getInferenceProgress(inference_task_id)
    } else {
        console.log("no inference task id found");
    }
});

function getImageSearchResults(inference_task_id) {
    const searchResultsSelector = $("#search_results");
    const url = inference_task_id + '/search_results';
    $.ajax({
        method: 'GET',
        url: url,
    }).catch(function (error) {
        console.log(error);
    }).then(function (returnHTML) {
        if (returnHTML === undefined) {
            console.log("no html was returned");
        } else {
            document.getElementById("progress_info").style.display = "none";
            searchResultsSelector.html(returnHTML);
        }
    });
}

function checkForInferenceCompletion(inference_task_id) {
    const url = inference_task_id + '/inference_complete';
    $.ajax({
        method: 'GET',
        url: url,
    }).catch(function (error) {
        console.log(error);
    }).then(function (returnJson) {
        if (returnJson['done']) {
            console.log('done with the things');
            getImageSearchResults(inference_task_id);
        } else if (returnJson['error']) {
            document.getElementById("progress_info").style.display = "none";
            document.getElementById("search_error").style.display = "block";
        } else {
            getInferenceProgress(inference_task_id);
        }
    });
}

function getInferenceProgress(inference_task_id) {
    const progressInfoSelector = $("#progress_info");
    const url = inference_task_id + '/inference_progress';
    $.ajax({
        method: 'GET',
        url: url,
    }).catch(function (error) {
        console.log(error);
    }).then(function (returnHTML) {
        if (returnHTML === undefined) {
            console.log("no html was returned");
        } else {
            progressInfoSelector.html(returnHTML);
        }
        // wait a little, then call checkForInferenceCompletion again
        const millisecondsToWait = 500;
        setTimeout(function () {
            checkForInferenceCompletion(inference_task_id)
        }, millisecondsToWait);
    });
}

function getPersonDetails(personPrimaryKey, selector) {
    // get html to display in the details modal
    const url = personPrimaryKey + '/person_details';
    $.ajax({
        method: 'GET',
        url: url,
    }).catch(function (error) {
        console.log(error);
    }).then(function (returnHTML) {
        if (returnHTML === undefined) {
            //document.getElementById("failed_search").hidden = false
        } else {
            // loading animation would be deactivated here
            selector.html(returnHTML);
        }
    });
}

function openModal(personPrimaryKey) {
    console.log("opening modal");
    const modalElement = $("#details_modal");
    const instance = M.Modal.getInstance(modalElement);
    instance.open();
    const personDetails = $("#person_details");
    personDetails.html("");
    // loading animation would be activated here
    getPersonDetails(personPrimaryKey, personDetails);
}

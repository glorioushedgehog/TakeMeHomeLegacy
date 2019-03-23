$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('select').formSelect();
    $('.tabs').tabs();
    // document.getElementById("image_search_loading_animation").style.display = "none";
    // document.getElementById("image_search_loading_text").style.display = "none";
    document.getElementById("search_error").style.display = "none";
    const inference_task_id = document.getElementsByName("inference_task_id")[0].value.trim();
    if (inference_task_id !== "") {
        console.log("found inference task id: " + inference_task_id);
        getInferenceProgress(inference_task_id)
    } else {
        console.log("could not find this things!");
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
        }else if(returnJson['error']){
            document.getElementById("progress_info").style.display = "none";
            document.getElementById("search_error").style.display = "block";
        }else{
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

function showImageSearchLoadingAnimation() {
    document.getElementById("image_search_loading_animation").style.display = "block";
    document.getElementById("image_search_loading_text").style.display = "block";
}

function resetVals() {
    $("#dob_year").val("");
    $("#height").val("");
    $("#weight").val("");
    $("#zip").val("");
    $("#first_name").val("");
    $("#last_name").val("");
    $("#home_city").val("");
    $("#name_to_call_me").val("");
    $("#search_results").html("");
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
    const modalElement = $("#details_modal");
    const instance = M.Modal.getInstance(modalElement);
    instance.open();
    const personDetails = $("#person_details");
    personDetails.html("");
    // loading animation would be activated here
    getPersonDetails(personPrimaryKey, personDetails);
}

function getSearchQuery() {
    const dob_yearStr = $("#dob_year").val();
    const heightStr = $("#height").val();
    const weightStr = $("#weight").val();
    const lastNameStr = $("#last_name").val();
    const firstNameStr = $("#first_name").val();
    const nameToCallMeStr = $("#name_to_call_me").val();
    const homeCity = $("#home_city").val();

    const homeStateOptionBox = document.getElementById("state");
    const homeState = homeStateOptionBox.options[homeStateOptionBox.selectedIndex].value;

    const homeZip = $("#zip").val();

    const raceOptionBox = document.getElementById("race");
    const race = raceOptionBox.options[raceOptionBox.selectedIndex].value;

    // Check that any input is neither empty nor non-numeric.
    if (isNaN(dob_yearStr) || isNaN(weightStr) || isNaN(heightStr) || isNaN(homeZip)) {
        alert("Please, enter only numbers for DOB (year), height, zip, and weight.");
        return
    }

    const dobYear = parseInt(dob_yearStr, 10);
    let height = parseInt(heightStr, 10);
    let weight = parseInt(weightStr, 10);


    const heightUnitBox = document.getElementById("height_unit");
    const heightUnit = heightUnitBox.options[heightUnitBox.selectedIndex].value;

    const weightUnitBox = document.getElementById("weight_unit");
    const weightUnit = weightUnitBox.options[weightUnitBox.selectedIndex].value;

    if (heightUnit === "2") { // If the height unit is 'cms', convert it to 'inches' since the database requires 'inches'.
        height = cmsToInches(height)
    }

    if (weightUnit === "2") { // If the height unit is 'kgs', convert it to 'lbs' since the database requires 'lbs'.
        weight = kgsToLbs(weight)
    }

    const sexOptionBox = document.getElementById("sex");
    const selectedSex = sexOptionBox.options[sexOptionBox.selectedIndex].value;
    const sex = selectedSex === "1" ? "M" : "F";

    const eyeColorBox = document.getElementById("eye_color");
    const eyeColor = eyeColorBox.options[eyeColorBox.selectedIndex].value;

    const hairColorBox = document.getElementById("hair_color");
    const hairColor = hairColorBox.options[hairColorBox.selectedIndex].value;

    const braceletId = $("#braclet_id").val();

    const recordTypeBox = document.getElementById("record_type");
    const recordType = recordTypeBox.options[recordTypeBox.selectedIndex].value;

    const organizationBox = document.getElementById("organization");
    const organization = organizationBox.options[organizationBox.selectedIndex].value;

    // Construct Search Query after all checks pass.
    const query = {
        "dob_year": dobYear,
        "height": height,
        "weight": weight,
        "sex": sex,
        "hair": hairColor,
        "eyes": eyeColor,
        "race": race,
        "last_name": lastNameStr,
        "first_name": firstNameStr,
        "name_to_call_me": nameToCallMeStr,
        "bracelet_id": braceletId,
        "record_type": recordType,
        "organization": organization,
        "home_city": homeCity,
        "home_state": homeState,
        "home_zip": homeZip,
    };

    console.log(query);

    const url = '/search_by_demographics';
    const token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    $.ajax({
        method: 'POST',
        url: url,
        data: JSON.stringify(query),
        headers: {
            'X-CSRFToken': token,
            'Content-length': query.length,
            'Content-type': 'application/json'
        }
    }).catch(function (error) {
        console.log(error);
    }).then(function (returnHTML) {
        if (returnHTML === undefined) {
            document.getElementById("failed_search").hidden = false
        } else {
            document.getElementById("search_results").hidden = false;
            document.getElementById("search_results").innerHTML = returnHTML;
        }
    })
}

function cmsToInches(cms) {
    return cms / 2.54
}

function kgsToLbs(kgs) {
    return kgs * 2.204
}

function resetViews() {
    document.getElementById("search_results").hidden = true;
    document.getElementById("failed_search").hidden = true
}

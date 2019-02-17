$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('select').material_select();
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, options);
});

function resetVals() {
    document.getElementById("dob_year").value = "";
    document.getElementById("height").value = "";
    document.getElementById("weight").value = "";
}

function getSearchQuery() {
    const dob_yearStr = document.getElementById("dob_year").value
    const heightStr = document.getElementById("height").value;
    const weightStr = document.getElementById("weight").value;
    const lastNameStr = document.getElementById("last_name").value;
    const firstNameStr = document.getElementById("first_name").value;
    const nameToCallMeStr = document.getElementById("name_to_call_me").value;
    const homeCity = document.getElementById("home_city").value;

    var homeStateOptionBox = document.getElementById("state");
    var selectedState = homeStateOptionBox.options[homeStateOptionBox.selectedIndex].value;
    const homeState = selectedState;

    const homeZip = document.getElementById("zip").value;

    var raceOptionBox = document.getElementById("race");
    var selectedRace = raceOptionBox.options[raceOptionBox.selectedIndex].value;
    const race = selectedRace;

    // Check that any input is niether empty nor non-numeric.
    if (isNaN(dob_yearStr) || isNaN(weightStr) || isNaN(heightStr) || isNaN(homeZip)) {
        alert("Please, enter only numbers for DOB (year), height, zip, and weight.");
        return
    }

    const dobYear = parseInt(dob_yearStr, 10);
    var height = parseInt(heightStr, 10);
    var weight = parseInt(weightStr, 10);


    var heightUnitBox = document.getElementById("height_unit");
    var heightUnit = heightUnitBox.options[heightUnitBox.selectedIndex].value;

    var weightUnitBox = document.getElementById("weight_unit");
    var weightUnit = weightUnitBox.options[weightUnitBox.selectedIndex].value;

    if (heightUnit === "2") { // If the height unit is 'cms', convert it to 'inches' since the database requires 'inches'.
        height = cmsToInches(height)
    }

    if (weightUnit === "2") { // If the height unit is 'kgs', convert it to 'lbs' since the database requires 'lbs'.
        weight = kgsToLbs(weight)
    }

    var sexOptionBox = document.getElementById("sex");
    var selectedSex = sexOptionBox.options[sexOptionBox.selectedIndex].value;
    const sex = selectedSex === "1" ? "M" : "F";

    var eyeColorBox = document.getElementById("eye_color");
    var selectedEyeColor = eyeColorBox.options[eyeColorBox.selectedIndex].value;
    const eyeColor = selectedEyeColor === "1" ? "Brown" : "Black";

    var hairColorBox = document.getElementById("hair_color");
    var selectedHairColor = hairColorBox.options[hairColorBox.selectedIndex].value;
    const hairColor = selectedHairColor === "1" ? "Brown" : "Black";


    // Construct Search Query after all checks pass.
    const query = {
        "dob_year": dobYear,
        "weight": weight,
        "height": height,
        "sex": sex,
        "eyeColor": eyeColor,
        "hairColor": hairColor,
        "lastName": lastNameStr,
        "firstName": firstNameStr,
        "homeCity": homeCity,
        "homeState": homeState,
        "nameToCallMe": nameToCallMeStr,
        "race": race
    };

    console.log(query);

    const url = 'http://127.0.0.1:8000/search_by_demographics';
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
    }).catch(function(error) {
        
    }).then(function (returnHTML) {
        document.getElementById("search_form").hidden = true;
        document.getElementById("search_results").hidden = false;
        document.getElementById("search_results").innerHTML = returnHTML;
    })
}


function cmsToInches(cms) {
    return cms / 2.54
}

function kgsToLbs(kgs) {
    return kgs * 2.204
}

function inchesToCms(inches) {
    return inches * 2.54
}

function resetViews() {
    document.getElementById("search_form").hidden = false;
    document.getElementById("search_results").hidden = true;
    document.getElementById("search_title").innerHTML = "Search";
}

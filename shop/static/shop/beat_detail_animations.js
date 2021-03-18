const usage_terms_show = document.getElementsByClassName('usage-terms-show-container');
const usage_terms_hide = document.getElementsByClassName('usage-terms-hide-container');


function showUsageTerms(i) {
    var license_properties, license_properties_display;
    license_properties = document.getElementsByClassName('license-properties');
    license_properties[i].style.display = "grid";
    usage_terms_show[i].style.display = "none";
    usage_terms_hide[i].style.display = "block";
}

function hideUsageTerms(i) {
    var license_properties, license_properties_display;
    license_properties = document.getElementsByClassName('license-properties');
    license_properties[i].style.display = "none";
    usage_terms_show[i].style.display = "block";
    usage_terms_hide[i].style.display = "none";
}
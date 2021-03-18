// show beats that fit search
function searchBeats() {
  // Declare variables
  var input, filter, section, div, a, i, txtValue, search_description;

  search_description = document.getElementById('search_beats_description');
  search_description.style.display = "none";

  input = document.getElementById('search_beats');
  filter = input.value.toUpperCase().replace(/\s/g,'');  //!!CHECK WHETHER REPLACE PART IS VALID!!
  article = document.getElementById('beats');
  div = article.getElementsByClassName('beat');
  console.log("Div length" + div.length)

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < div.length; i++) {
    beat_title = div[i].getElementsByClassName("beat-keywords")[0];
    txtValue = beat_title.textContent.replace(/\s/g,'') || beat_title.innerText.replace(/\s/g,'');
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      div[i].style.display = "";
    } else {
      div[i].style.display = "none";
    }
  }
}


//Link to detail view of beat
const beat = document.getElementsByClassName('beat');
for (i = 0; i < beat.length; i++) {
  const beat_title = document.getElementsByClassName('beat-title')[i].innerHTML.replace(/ /g, "_");
  beat[i].addEventListener('click', () => {
     beat_string = "/beats/beat-detail/" + beat_title;
     window.location.href = beat_string;
  });
}


const page_link = document.getElementsByClassName('page-link');
for (i = 0; i < page_link.length; i++) {
  const page_link_title = document.getElementsByClassName('page-link-title')[i].innerHTML.replace(/ /g, "_");
  page_link[i].addEventListener('click', () => {
     beat_string = "/beats/" + page_link_title;
     window.location.href = beat_string;
  });
}
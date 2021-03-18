const menuBtn = document.querySelector('.menu-btn');
const pagelinks = document.getElementById('pagelinks');
const navBar = document.getElementById('navbar')
let menuOpen = false;
menuBtn.addEventListener('click', () => {
  if(!menuOpen) {
    menuBtn.classList.add('open');
    menuOpen = true;
    navBar.style.height = "260px";
    pagelinks.style.display = "block";
  } else {
    menuBtn.classList.remove('open');
    menuOpen = false;
    navBar.style.height = "46";
  }
});


// Add cookies for cart

var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var beatId = this.dataset.beat
        var licenseTitle = this.dataset.license
		var action = this.dataset.action
		console.log('beatId:', beatId, 'licenseTitle:', licenseTitle, 'Action:', action)

		addCookieItem(beatId, licenseTitle, action)
	})
}

function addCookieItem(beatId, licenseTitle, action){
	console.log('Adding cookies')

	if (action == 'add'){
        cart[beatId] = {'quantity':1, 'license': licenseTitle}
	}

	if (action == 'remove'){
		cart[beatId]['quantity'] -= 1

		if (cart[beatId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[beatId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

	location.reload()
}

function addCookieTransactionId(transactionId){
    transactionIdCookie = {'transactionId': transactionId}
	console.log('transactionIdCookie:', transactionIdCookie)
	document.cookie ='transactionIdCookie=' + JSON.stringify(transactionIdCookie) + ";domain=;path=/"
    location.reload()
    window.location.href = "/create_license_pdf/"
}

function paypalErrorMessage(){
    var errorContainer = document.getElementById('error-container');
    errorContainer.style.display = "block";
}






// make words which have //...// around them bold
boldText()

function boldText(){
    var x, i
    // only execute when desired item exists
    if (document.getElementsByClassName("content")){
      var strings = document.getElementsByClassName("content");
      for (x = 0; x < strings.length; x++){
        var string = strings[x].innerHTML;
        var splitstring = string.split("//");
        document.getElementsByClassName("content")[x].innerHTML = splitstring[0];
        for (i = 1; i < splitstring.length; i++) {
           // document.getElementById("beginners_guide_content").innerHTML += splitstring[i];
            if (i % 2 == 0){
                document.getElementsByClassName("content")[x].innerHTML += splitstring[i];
            }
            else {
                document.getElementsByClassName("content")[x].innerHTML += splitstring[i].bold();
          }
        }
    }
  }
}


//turn words with --...@link@-- around them into a link that leads to the link between @...@
linkText()

function linkText(){
    var x, i
    // only execute when desired item exists
    if (document.getElementsByClassName("content")){
      var strings = document.getElementsByClassName("content");
      for (x = 0; x < strings.length; x++){
        var string = strings[x].innerHTML;
        var splitstring = string.split("--");
        document.getElementsByClassName("content")[x].innerHTML = splitstring[0];
        for (i = 1; i < splitstring.length; i++) {
           // document.getElementById("beginners_guide_content").innerHTML += splitstring[i];
            if (i % 2 == 0){
                document.getElementsByClassName("content")[x].innerHTML += splitstring[i];
            }
            else {
                var processed_string = splitstring[i].split("@");
                document.getElementsByClassName("content")[x].innerHTML += processed_string[0].link(processed_string[1]);
          }
        }
    }
  }
}



//turn words with --...@link@-- around them into a link that leads to the link between @...@
nextLine()

function nextLine(){
    var x, i
    // only execute when desired item exists
    if (document.getElementsByClassName("content")){
      var strings = document.getElementsByClassName("content");
      for (x = 0; x < strings.length; x++){
        var string = strings[x].innerHTML;
        var splitstring = string.split("==");
        document.getElementsByClassName("content")[x].innerHTML = splitstring[0]
        document.getElementsByClassName("content")[x].innerHTML += "<br>"
        for (i = 1; i < splitstring.length; i++) {
         document.getElementsByClassName("content")[x].innerHTML += splitstring[i]
         document.getElementsByClassName("content")[x].innerHTML += "<br>"
            }
        }
    }
}
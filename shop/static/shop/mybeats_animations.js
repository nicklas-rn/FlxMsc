function addCookieTransactionIdMyBeats(){
    var transactionId;
    transactionId = document.getElementById('transactionId-input').value;
    transactionIdCookie = {'transactionId': transactionId}
	console.log('transactionIdCookie:', transactionIdCookie)
	document.cookie ='transactionIdCookie=' + JSON.stringify(transactionIdCookie) + ";domain=;path=/"
    location.reload()
    window.location.href = "/summary/"
}
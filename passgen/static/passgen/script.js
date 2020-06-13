// With JQuery
$('#length').slider({
	formatter: function(value) {
		return 'Current value: ' + value;
	}
});

function myFunction() {
	url = "/newpassword/?length=6&uppercase=on&numbers=on&special=on"
	var x = new XMLHttpRequest();
	x.open("GET", url, true);
	x.send(null)
	document.getElementById("password").innerHTML = x.responseText;
}

// $('#pass_btn').get("/newpassword/?length=6&uppercase=on&numbers=on&special=on", function (data) {
// 	var msg = data;
// 	alert(msg);
// });

// function myFunction() {
// 	const axios = require('axios');
// 	// Make a request
// 	axios({
// 		method: 'get',
// 		url: 'http://127.0.0.1:8080/newpassword',
// 		params: {
// 			length: "6",
// 			uppercase: "on",
// 			numbers: "on",
// 			special: "on"
// 		}
// 	})
// 		.then(function (response) {
// 			// handle success
// 			console.log(response);
// 		})
// 		.catch(function (error) {
// 			// handle error
// 			console.log(error);
// 		})
// 		.then(function () {
// 			// always executed
// 		});
// }

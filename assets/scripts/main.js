
window.onload = function () {
	eel.describe_token("computer")(display_results);
};

function display_results(token) {
	document.getElementById('description').innerHTML = "freq: "+token["freq"]+" weight: "+token["weight"] ;
}

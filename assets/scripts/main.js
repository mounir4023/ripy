

new Vue({ 
	el: '#app', 
	data: {
		tab: 1,
		isActive: true,
	},
	methods: {
		select_tab: function(selected) {
			this.tab = selected; 
		},
	},
});



/*
eel.describe_token("computer")(display_results);
function display_results(token) {
	document.getElementById('description').innerHTML = "freq: "+token["freq"]+" weight: "+token["weight"] ;
}
*/

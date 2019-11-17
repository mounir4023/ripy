
var app = new Vue({ 
	el: '#app', 
	data: {
		tab: 1,
		isActive: true,
		docs: [ ],
	},
	methods: {
		select_tab: function(selected) {
			this.tab = selected; 
		},
		update_docs: function(return_data) {
			this.docs = return_data;
		}
	},
	mounted: function() {
		eel.get_all_docs()(this.update_docs) 
	}, 
});



/*
eel.describe_token("computer")(display_results);
function display_results(token) {
	document.getElementById('description').innerHTML = "freq: "+token["freq"]+" weight: "+token["weight"] ;
}
*/


var app = new Vue({ 
	el: '#app', 
	data: {
		tab: 1,
		isActive: true,
		docs: [ ],
		token: "",
		description: [ ],
	},
	methods: {
		select_tab: function(selected) {
			this.tab = selected; 
		},
		describe_token: function(){
			eel.describe_token(this.token)(this.update_description)
		},
		clear_token: function() {
			this.token = "";
			this.description = [ ];
		},
		normalize_length: function(doc) {
			return doc.padEnd(12," ");
		},
		// eel callbacks
		update_docs: function(return_data) {
			this.docs = return_data;
		},
		update_description: function(return_data) {
			this.description = return_data;
		},
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


var app = new Vue({ 
	el: '#app', 
	data: {
		tab: 1,
		isActive: true,
		docs: [ ],
		token: "",
		description: [ ],
		tbh: 0,
	},
	computed : {
		tb_height: function() { if (this.isMounted) console.log(this.$refs.tb.computedHeight); return 0; },
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
		// eel callbacks
		update_docs: function(return_data) {
			this.docs = return_data;
		},
		update_description: function(return_data) {
			this.description = return_data;
		},
	},
	mounted: function() {
		this.isMounted = true;
	}, 
});



/*
eel.describe_token("computer")(display_results);
function display_results(token) {
	document.getElementById('description').innerHTML = "freq: "+token["freq"]+" weight: "+token["weight"] ;
}
*/

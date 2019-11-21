
var app = new Vue({ 
	el: '#app', 
	data: {
		tab: 1,
		isActive: true,
		docs: [ ],
		token: "",
		boolquery: "",
		vectquery: "",
		description: [ ],
		booldesc: [ ],
		vectdesc: [ ],
		tbh: 64,
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
		process_boolean: function(){
			eel.process_boolean(this.normalize_bq())(this.update_booldesc)
		},
		clear_token: function() {
			this.token = "";
			this.description = [ ];
		},
		clear_b_query: function() {
			this.boolquery = "";
			this.booldesc = [ ];
		},
		normalize_bq: function() { 
			q = this.boolquery.replace(" or "," + ");
			q = q.replace(" and "," * ");
			if (q.substr(0,4) == "not ")
				q = " " + q
			q = q.replace(" not "," ! ");
			return q;
		},
		// eel callbacks
		update_docs: function(return_data) {
			this.docs = return_data;
		},
		update_description: function(return_data) {
			this.description = return_data;
		},
		update_booldesc: function(return_data) {
			this.booldesc = return_data;
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

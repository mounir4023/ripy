
//document.documentElement.style.overflow = 'hidden';

var app = new Vue({
	el: '#app',
	data: {
		tab: 1,
		tbh: 64,
		isActive: true,
		docdialog: false,
		doctext: "",
		doc: "",
		docs: [ ],
		token: "",
		boolquery: "",
		vectquery: "",
		description: [ ],
		booldesc: [ ],
		vectdesc: [ ],
		vectpages: 1,
		vectpage: 1,
		pagesize: 8,
		vectmode: "IP",
	},
	computed : {
		//tb_height: function() { if (this.isMounted) console.log(this.$refs.tb.computedHeight); return 0; },
	},
	methods: {
		select_tab: function(selected) {
			this.tab = selected;
		},
		open_doc: function(doc) {
			this.doc = doc;
			eel.open_doc(this.doc)(this.update_doctext)
			this.docdialog = true;
		},
		describe_token: function(){
			eel.describe_token(this.token)(this.update_description)
		},
		process_boolean: function(){
			eel.process_boolean(this.normalize_bq())(this.update_booldesc)
		},
		process_vectorial: function(){
			eel.process_vectorial(this.vectquery, this.vectmode)(this.update_vectdesc)
		},
		clear_token: function() {
			this.token = "";
			this.description = [ ];
		},
		clear_b_query: function() {
			this.boolquery = "";
			this.booldesc = [ ];
		},
		clear_v_query: function() {
			this.vectquery = "";
			this.vectdesc = [ ];
		},
		normalize_bq: function() {
			q = this.boolquery.replace(" or "," + ");
			q = q.replace(" and "," * ");
			if (q.substr(0,4) == "not ")
				q = " " + q
			q = q.replace(" not "," ! ");
			return q;
		},
		shown_in_page: function(index) {
			return (this.pagesize * (this.vectpage-1) <= index) && (index < this.pagesize * this.vectpage)
		},
		close_doc: function() {
			this.doc = "";
			this.docdialog = false;
			this.doctext = "";
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
		update_vectdesc: function(return_data) {
			this.vectdesc = return_data;
			this.vectpages = Math.ceil(1.0 * return_data.length / this.pagesize);
			this.vectpage = 1;
		},
		update_doctext: function(return_data) {
			this.doctext = return_data
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

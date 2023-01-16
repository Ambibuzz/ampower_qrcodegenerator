// Copyright (c) 2023, ithead@ambibuzz.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Text to QR code', {
	onload:(frm)=>{
		console.log(frm.doc.qr_code_text);
		if(frm.doc.qr_code_base64){
			$(frm.fields_dict['qr_code_image'].wrapper)
				.html('<img style="display:block; width:200px;height:200px;" id="base64image" src="'+frm.doc.qr_code_base64+'" />');
		}else{
			$(frm.fields_dict['qr_code_image'].wrapper)
				.html('');
		}
	},
	generate_qr_code: function(frm) {
		if(!frm.doc.qr_code_text){
			frappe.show_alert('please set Qr code text field first')
			return true;
		}
		frappe.call({
			method: "ampower_qrgenerator.ampower_qrgenerator.doctype.text_to_qr_code.text_to_qr_code.generate_qr_code", //dotted path to server method
			args:{qr_code_text:frm.doc.qr_code_text},
			callback: function(r) {
				console.log(r)
				frm.set_value("qr_code_base64", r.message)
				$(frm.fields_dict['qr_code_image'].wrapper)
				.html('<img style="display:block; width:200px;height:200px;" id="base64image" src="'+r.message+'" />');
				// frm.set_value("test_html", '<img style="display:block; width:100px;height:100px;" id="base64image" src='+r.message+' />')
				frm.dirty();
				frm.save();

			}
		});

	}
});




// text_to_qr_code
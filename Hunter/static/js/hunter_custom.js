// Handler for .ready() called.



$(document).ready(function() {
	'use strict'; 
	
	$('#hunterResultsJumbotron').hide();
	$('#processingDiv').hide();
	
	$('#submitHttpEndPoint').click(function(){
		
		if($('#httpEndPointInput').val() == '' || $('#httpEndPointInput').val() == undefined){

		}
		else{
			$('#processingDiv').show();
			var endpointResults = model.processHttpEndpoint($('#httpEndPointInput').val());
			console.log(endpointResults);
			console.log(conver_string_toArray(endpointResults.tls_one_two_supported_cipher_list));
			console.log(endpointResults.tls_one_two_supported_cipher_list.length);
			console.log(endpointResults.tls_one_two_supported_cipher_list.constructor);
			//console.log(new Array(endpointResults.tls_one_two_supported_cipher_list));
			
			$('#hunterResultsJumbotron').show();
			if(endpointResults.final_score_percentage >= 95){
				$('#overallRatingDiv').show()
				$('#overallRatingADiv').show();
				$('#overallRatingBDiv').hide();
				$('#overallRatingCDiv').hide();
			}
			else if (endpointResults.final_score_percentage < 95 && endpointResults.final_score_percentage >= 70){
				$('#overallRatingDiv').show()
				$('#overallRatingADiv').hide();
				$('#overallRatingBDiv').show();
				$('#overallRatingCDiv').hide();
			}
			else{
				$('#overallRatingDiv').show()
				$('#overallRatingADiv').hide();
				$('#overallRatingBDiv').hide();
				$('#overallRatingCDiv').show();
			}
			
			var htmlToBeAppended = '';
			var cipherlist;
			if(endpointResults.ssl_two_zero_enbled != null && endpointResults.ssl_two_zero_enbled == true){
				
				htmlToBeAppended = '<h4 class="display-6">SSL 2.0 is Enabled</h4>';			
				if(endpointResults.ssl_two_zero_supported_cipher_list != null && endpointResults.ssl_two_zero_supported_cipher_list.length > 0){					
					cipherlist = conver_string_toArray(endpointResults.ssl_two_zero_supported_cipher_list);
					for (var i = 0; i < cipherlist.length; i++) {
						htmlToBeAppended += '<p class="display-6 text-right">'+cipherlist[i]+'</p>';
					} 
				}
				
				$('#allTLSContent').append(htmlToBeAppended);
				$('#cipherResults').show();
				htmlToBeAppended = '';
			}
			if(endpointResults.ssl_three_zero_enbled != null && endpointResults.ssl_three_zero_enbled == true){
				
				htmlToBeAppended = '<h4 class="display-6">SSL 3.0 is Enabled</h4>'	;
				if(endpointResults.ssl_three_zero_supported_cipher_list != null && endpointResults.ssl_three_zero_supported_cipher_list.length > 0){
					cipherlist = conver_string_toArray(endpointResults.ssl_three_zero_supported_cipher_list);
					for (var i = 0; i < cipherlist.length; i++) {
						htmlToBeAppended += '<p class="display-6 text-right">'+cipherlist[i]+'</p>';
					} 
				}						
				$('#allTLSContent').append(htmlToBeAppended);
				$('#cipherResults').show();
				htmlToBeAppended = '';
		    }
			if(endpointResults.tls_one_zero_enbled != null && endpointResults.tls_one_zero_enbled === true){
				
				htmlToBeAppended = '<h4 class="display-6">TLS 1.0 is Enabled</h4>'	;
				if(endpointResults.tls_one_zero_supported_cipher_list != null && endpointResults.tls_one_zero_supported_cipher_list.length > 0){
					cipherlist = conver_string_toArray(endpointResults.tls_one_zero_supported_cipher_list);
					for (var i = 0; i < cipherlist.length; i++) {
						htmlToBeAppended += '<p class="display-6 text-right">'+cipherlist[i]+'</p>';
					} 
				}						

				$('#allTLSContent').append(htmlToBeAppended);
				$('#cipherResults').show();
				htmlToBeAppended = '';
		    }			
			if(endpointResults.tls_one_one_enbled != null && endpointResults.tls_one_one_enbled === true){
				
				htmlToBeAppended = '<h4 class="display-6">TLS 1.1 is Enabled</h4>'	;
				if(endpointResults.tls_one_one_supported_cipher_list != null && endpointResults.tls_one_one_supported_cipher_list.length > 0){
					cipherlist = conver_string_toArray(endpointResults.tls_one_one_supported_cipher_list);
					for (var i = 0; i < cipherlist.length; i++) {
						htmlToBeAppended += '<p class="display-6 text-right">'+cipherlist[i]+'</p>';
					} 
				}
				$('#allTLSContent').append(htmlToBeAppended);
				$('#cipherResults').show();
				htmlToBeAppended = '';
		    }
			if(endpointResults.tls_one_two_enbled != null && endpointResults.tls_one_two_enbled === true){
				
				htmlToBeAppended = '<h4 class="display-6">TLS 1.2 is Enabled</h4>'	;
				if(endpointResults.tls_one_two_supported_cipher_list != null && endpointResults.tls_one_two_supported_cipher_list.length > 0){
					cipherlist = conver_string_toArray(endpointResults.tls_one_two_supported_cipher_list);
					for (var i = 0; i < cipherlist.length; i++) {
						htmlToBeAppended += '<p class="display-6 text-right">'+cipherlist[i]+'</p>';
					} 
				}
				$('#allTLSContent').append(htmlToBeAppended);
				$('#cipherResults').show();
				htmlToBeAppended = '';
		    }			
			
			
		$('#processingDiv').hide();
	  }
	});
	
	
})


function conver_string_toArray(string_to_be_converted) {
	var arrayObj;
	
	string_to_be_converted = string_to_be_converted.replace('[','');
	string_to_be_converted = string_to_be_converted.replace(']','');
	arrayObj = string_to_be_converted.split(',');
	
	return arrayObj
}





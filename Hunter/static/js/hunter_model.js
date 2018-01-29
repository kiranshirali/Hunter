/*
 * This is the 'MODEL' part of my MVC oriented JavaScript Architecture. This file contains all the functions that would send GET and POST
 * requests to my server.
 * 
 * 
 * 
 */

var model = {
		
		processHttpEndpoint : function(httpEndPoint) {
			var responseJsonObject = null;
			$.ajax({
				type : "POST",
				url : "rest/v1/httpEndPointStatus/",
				async : false,
				headers : {
					"Content-Type" : "application/json"
				},
				data : httpEndPoint,
				success : function(serverRespone) {
					console.log(serverRespone);
					responseJsonObject = serverRespone;
				},
				error : function() {
					alert('Error')
				}
			});

			return responseJsonObject;

		}

		
		
}
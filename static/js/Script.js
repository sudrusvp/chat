$(function(){

	var sentHead = "<div class='row' style='margin: 5px 0px;'> <div class='col-sm-offset-4 col-sm-8 text-right' '> <div class='sent text-left' >";
	var receivedHead = "<div class='row' style='margin: 5px 0px;'> <div class='col-sm-8 text-left' '> <div class='received text-left' >";
	var tail = "</div> </div> </div>";
		
	function send() {
		console.log("inside send")
		var data = {
			"message" : $("#message").val(),
			
		};

		$(sentHead+data.message+tail).hide().appendTo('.chatdiv').show("puff", {times : 3}, 200);

		$(".chatdiv").animate({ scrollTop: $('.chatdiv').prop("scrollHeight")}, 1000);
		$("#message").val("");
		
		console.log("calling..")
		$.post("/",data,function(res){
			console.log("inside response")
			console.log(res)


			$(receivedHead+res+tail).hide().appendTo('.chatdiv').show("puff", {times : 3}, 200);

			$(".chatdiv").animate({ scrollTop: $('.chatdiv').prop("scrollHeight")}, 1000);

			});

	};


	$("#message").keypress(function(event) {
		if (event.which == 13) {
			event.preventDefault();

			if( $("#message").val() != "")
				send();
		}
	});

	$("#send").click(function(event){
		console.log("send")
		if( $("#message").val() != "")
			send()
	})

	function setInput(text) {
		$("#message").val(text);
		//send()
	}
});




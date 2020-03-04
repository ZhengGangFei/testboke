function saveh5(){
	var context = document.documentElement.outerHTML;
	// console.log(context);
	$.ajax({
		type:'post',
		url:'/save_h5/',
		data:context,
		success:function(data){
			result = JSON.parse(data)
			alert(result.message);
		}
	});
}
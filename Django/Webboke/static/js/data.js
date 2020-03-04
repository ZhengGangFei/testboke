$(document).ready(function(){ 
	var ul_new = document.getElementById('every_news');
	var ul_text = document.getElementById('every_text');
	var loop = 1;
    $.ajax({
		url:'/get_data/',
		type:'get',
		data:'',
		success:function(data){
			console.log(data);
			for(var i=0; i<data['news'].length; i++){
				var li = document.createElement('li');
				ul_new.appendChild(li);
				li.innerHTML = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;发布时间:'+data['news'][i][3]+'</p>'+'<a href="' +data['news'][i][2] +'" >'+data['news'][i][1]+'</a>'+'<p>';
			}
			for(var i=0; i<data['text'].length; i++){
				var li = document.createElement('li');
				ul_text.appendChild(li);
				li.innerHTML = '</p>'+'<a href="' +data['text'][i][2] +'" >'+data['text'][i][1]+'</a>'+'<p>';
			}
		}
	});
	
	var img = document.getElementById('img');
	setInterval(function(){
	           if (loop<=4 && loop>=0){
				   loop = loop+1;
					
					}else{
						loop = 1;
					}
					
				img.src = "../static/imgs/"+loop+".jpg";
	        },3000)

}); 



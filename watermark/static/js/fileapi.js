'use strict'

window.onload=function(){
    var fileInput = document.getElementById('img1');
	var c=document.getElementById("Canvas1");
	var cxt=c.getContext("2d");

    fileInput.addEventListener('change',function(){
        console.log('change...');
        if (!fileInput.value){
            var img=new Image();
			img.src="static/images/blank.png"
			cxt.drawImage(img,0,0,350,350);
			return ;
        }
        var file = fileInput.files[0];
        if(file.type !== 'image/jpeg' && file.type !== 'image/png' && file.type !== 'image/gif'){
            alert('不是有效的图片文件!');
			var img=new Image();
			img.src="static/images/blank.png"
			cxt.drawImage(img,0,0,350,350);
            return;
        }

        var reader = new FileReader();
        reader.onload=function(e){
            console.log('reader.onload');
            var data = e.target.result;
			var img=new Image();
			img.src= data;
			cxt.drawImage(img,0,0,img.width,img.height);
        };
        reader.readAsDataURL(file);
    });
	
	var fileInput2 = document.getElementById('img2');
	var c2=document.getElementById("Canvas2");
	var cxt2=c2.getContext("2d");

    fileInput2.addEventListener('change',function(){
        console.log('change...');
        if (!fileInput2.value){
			var img=new Image();
			img.src="static/images/blank.png"
			cxt2.drawImage(img,0,0,350,350);
            return ;
        }
        var file = fileInput2.files[0];
        if(file.type !== 'image/jpeg' && file.type !== 'image/png' && file.type !== 'image/gif'){
            alert('不是有效的图片文件!');
			var img=new Image();
			img.src="static/images/blank.png"
			cxt2.drawImage(img,0,0,350,350);
            return;
        }
        var reader = new FileReader();
        reader.onload=function(e){
            console.log('reader.onload');
            var data = e.target.result;
			var img=new Image();
			img.src= data;
			cxt2.drawImage(img,0,0,img.width,img.height);
        };
        reader.readAsDataURL(file);
    });
};
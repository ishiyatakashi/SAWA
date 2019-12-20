const canvas = document.getElementById("canvas");
    let imagePath = "/file/noimg.jpg";
    draw(canvas,imagePath);
    function draw(canvas,imagePath){
        console.log("draw");
        const image = new Image();
        image.src = imagePath;
        console.log(image.sizes)
        image.addEventListener("load",function (){
            $("#canvas").attr("width",image.width);   //←これだったらおｋだった。
	        $("#canvas").attr("height",image.height);
            const ctx = canvas.getContext("2d");
            ctx.drawImage(image,0, 0, image.width, image.height);
            console.log("load!");
        });
    }
     $("#file").change(function() {

         const file = this.files[0];
         console.log('change')
         const image = new Image();
         const reader = new FileReader();

         reader.onload = function (evt) {
             image.onload = function () {

                 //canvas1のサイズを画像サイズに合わせて変更（引き伸ばされる）
                 $("#canvas").attr("width", image.width);   //←これだったらおｋだった。　orz
                 $("#canvas").attr("height", image.height);
                 const ctx = canvas.getContext("2d");
                 ctx.drawImage(image, 0, 0); //canvas1に画像を転写
             }


             image.src = evt.target.result;
         }
         reader.readAsDataURL(file);
     });
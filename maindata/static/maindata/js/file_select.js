
// forked from _shimizu's "input type=file → canvas" http://jsdo.it/_shimizu/5KO3
$("#uploadFile").change(function() {

    var file = this.files[0];
    if (!file.type.match(/^image\/(png|jpeg|gif)$/)) return;

    var image = new Image();
    var reader = new FileReader();

    reader.onload = function(evt) {
        image.onload = function() {


            $("#canvas").attr("width",image.width);
            $("#canvas").attr("height",image.height);


            var canvas = $("#canvas");
            var ctx = canvas[0].getContext("2d");
            ctx.drawImage(image, 0, 0); //canvasに画像を転写

        }


        image.src = evt.target.result;
    }
    reader.readAsDataURL(file);
});

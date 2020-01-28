let canvas = document.getElementById("canvas");
//
let imagePath = "/file/openfile/noimg.jpg";
draw(canvas, imagePath);
let file = null;
let blob = null;

function draw(canvas, imagePath) {
    console.log("draw");
    const image = new Image();
    image.src = imagePath;
    console.log(image.sizes);
    image.addEventListener("load", function () {
        canvas.width = image.width;   //←これだったらおｋだった。
        canvas.height = image.height;
        const ctx = canvas.getContext("2d");
        ctx.drawImage(image, 0, 0, image.width, image.height);
        console.log("load!");
    });
}

$("#file").change(function () {

    file = this.files[0];
    console.log('change');
    const image = new Image();
    const reader = new FileReader();

    reader.onload = function (evt) {
        image.onload = function () {
            var ctx = canvas.getContext('2d');
            canvas.width = image.width;   //←これだったらおｋだった。
            canvas.height = image.height;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            if (image.width > 582) {
                //canvas1のサイズを画像サイズに合わせて変更（引き伸ばされる）
                const wari = 582 / image.width;
                const yoko = image.height * wari;
                canvas.width = 582;   //←これだったらおｋだった。
                canvas.height = yoko;
                ctx.drawImage(image, 0, 0, image.width, image.height, 0, 0, 582, yoko); //canvas1に画像を転写
            } else {
                //canvas1のサイズを画像サイズに合わせて変更（引き伸ばされる）
                ctx.drawImage(image, 0, 0); //canvas1に画像を転写
            }
            let base64 = canvas.toDataURL('image/jpeg');
            make_hidden('base64', base64, 'form');
        };
        image.src = evt.target.result;
    };
    reader.readAsDataURL(file);
});

function checkPhase() {
    if (!file) {
        alert("画像が入っていません！");
        return false;
    }
    document.form.submit();
}

function make_hidden(name, value, formname) {
    const q = document.createElement('input');
    q.type = 'hidden';
    q.name = name;
    q.value = value;
    if (formname) {
        if (document.forms[formname] === undefined) {
            console.error("ERROR: form " + formname + " is not exists.");
        }
        document.forms[formname].appendChild(q);
    } else {
        document.forms[0].appendChild(q);
    }
}
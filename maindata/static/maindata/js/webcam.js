let canvas = document.getElementById("picture");
let base64 = null
function create_canvas64() {
    let base64 = canvas.toDataURL('image/jpeg');
    make_hiddendata('base64', base64,'camera');
    document.form.submit();
}

function make_hiddendata(name, value, formname) {
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

window.onload = () => {
    const video = document.querySelector("#camera");
    const canvas = document.querySelector("#picture");
    const camera = document.getElementById('camera');
    const result = document.getElementById('picture');
    const cancel = document.getElementById('cancel');
    const shutter = document.getElementById('shutter');
    var next = document.getElementById('next');

    /** カメラ設定 */
    const constraints = {
        audio: false,
        video: {
            width: 336,
            height: 336,
            facingMode: "user"   // フロントカメラを利用する
            // facingMode: { exact: "environment" }  // リアカメラを利用する場合
        }
    };

    /**
     * カメラを<video>と同期
     */
    navigator.mediaDevices.getUserMedia(constraints)
        .then((stream) => {
            video.srcObject = stream;
            video.onloadedmetadata = (e) => {
                video.play();
            };
        })
        .catch((err) => {
            alert('カメラが起動してません!!!!');
        });

    /**
     * シャッターボタン
     */
    document.querySelector("#shutter").addEventListener("click", () => {
        const ctx = canvas.getContext("2d");

        setTimeout(() => {
            video.play();    // 0.5秒後にカメラ再開
        }, 500);

        // canvasに画像を貼り付ける
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

        base64 = canvas.toDataURL('image/jpeg');
        camera.style.display = 'none';
        shutter.style.display = 'none';
        result.style.display = 'inline';
        cancel.style.display = 'inline';
        next.style.display = 'inline';

    });
    /**
     * キャンセル
     */
    document.querySelector("#cancel").addEventListener("click", () => {
        camera.style.display = 'inline';
        shutter.style.display = 'inline';
        result.style.display = 'none';
        cancel.style.display = 'none';
        next.style.display = 'none';
    });

};
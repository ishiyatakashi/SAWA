window.onload = () => {
    const video = document.querySelector("#camera");
    const canvas = document.querySelector("#picture");
    var camera = document.getElementById('camera');
    var result = document.getElementById('picture');
    var cancel = document.getElementById('cancel');
    var shutter = document.getElementById('shutter');
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
            console.log(err.name + ": " + err.message);
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

    document.querySelector("#next").addEventListener("click", () => {

    });
};
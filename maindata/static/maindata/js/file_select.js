let canvas = document.getElementById("canvas");
let scal = document.getElementById('scal');
let com = document.getElementById('comment');
let dammy = document.getElementById('dammy');

const img = new Image();
let file = null;

const cw = canvas.width;
const ch = canvas.height;
const out = document.getElementById( 'outCanvas' );
const oh = out.height;
const ow = out.width;

let ix = 0;  // 中心座標
let iy = 0;
let v = 1.0;   // 拡大縮小率()




$("#file").change(function () {

    file = this.files[0];
    console.log('change');
    dammy.style.display = 'none';
    canvas.style.display = 'inline';
    const reader = new FileReader();

    reader.onload = function (evt) {
        img.onload = function () {
            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ix = img.width  / 2;
            iy = img.height / 2;
            let scl = parseInt( cw / img.width * 100 );
            document.getElementById( 'scal' ).value = scl;
            scaling( scl )
        };
        img.src = evt.target.result;
    };
    reader.readAsDataURL(file);
    scal.style.visibility = 'visible';
    com.style.display = 'inline';
});

function checkPhase() {
    if (!file) {
        alert("画像が入っていません！");
        return false;
    }
    const ctx = out.getContext( '2d' );
    ctx.fillStyle = 'rgb(245, 245, 245)';
    ctx.fillRect( 0, 0, ow, oh );    // 背景を塗る
    ctx.drawImage( img,
        0, 0, img.width, img.height,
        (ow/2)-ix*v, (oh/2)-iy*v, img.width*v, img.height*v,
    );
    let base64 = out.toDataURL('image/jpeg');
    make_hidden('base64', base64, 'jpeg');
    document.form.submit();
}
//formnameに対して画像のbase64データ(value)をnameという名前で埋め込む
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

// 試作品(画像切り抜き機能)
    function draw_canvas( _x, _y ){     // 画像更新
        const ctx = canvas.getContext( '2d' );
        ctx.fillStyle = 'rgb(245, 245, 245)';
        ctx.fillRect( 0, 0, cw, ch );    // 背景を塗る
        ctx.drawImage( img,
            0, 0, img.width, img.height,
            (cw/2)-_x*v, (ch/2)-_y*v, img.width*v, img.height*v,
        );
        ctx.strokeStyle = 'rgba(200, 0, 0, 0.8)';
        ctx.strokeRect( (cw-ow)/2, (ch-oh)/2, ow, oh ) // 赤い枠
    }
    function scaling( _v ) {        // スライダーが変わった
        v = parseInt( _v ) * 0.01;
        draw_canvas( ix, iy )       // 画像更新
    }

    let mouse_down = false;      // canvas ドラッグ中フラグ
    let sx = 0;                 // canvas ドラッグ開始位置
    let sy = 0;
    canvas.ontouchstart =
    canvas.onmousedown = function ( _ev ){     // canvas ドラッグ開始位置
        mouse_down = true;
        sx = _ev.pageX;
        sy = _ev.pageY;
        return false // イベントを伝搬しない
    };
    canvas.ontouchend =
    canvas.onmouseout =
    canvas.onmouseup = function ( _ev ){       // canvas ドラッグ終了位置
        if ( mouse_down === false ) return;
        mouse_down = false;
        draw_canvas( ix += (sx-_ev.pageX)/v, iy += (sy-_ev.pageY)/v );
        return false // イベントを伝搬しない
    };
    canvas.ontouchmove =
    canvas.onmousemove = function ( _ev ){     // canvas ドラッグ中
        if ( mouse_down === false ) return;
        draw_canvas( ix + (sx-_ev.pageX)/v, iy + (sy-_ev.pageY)/v );
        return false // イベントを伝搬しない
    };
    canvas.onmousewheel = function ( _ev ){    // canvas ホイールで拡大縮小
        let scl = parseInt( parseInt( document.getElementById( 'scal' ).value ) + _ev.wheelDelta * 0.05 );
        if ( scl < 10  ) scl = 10;
        if ( scl > 400 ) scl = 400;
        document.getElementById( 'scal' ).value = scl;
        scaling( scl );
        console.log(scl);
        return false // イベントを伝搬しない
    };
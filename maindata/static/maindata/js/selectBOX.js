//俳優の全チェック＆解除
function ActorAllChecked(){
      const check = document.getElementById("a_ch0").checked; //マスタ
      const category = document.getElementsByName("actor"); //カテゴリ
      console.log(check);
      //長さ分だけループしてマスタと同じ状態にする
      for (let i = 0; i < category.length; i++) {
          category[i].checked = check;
      }
  }

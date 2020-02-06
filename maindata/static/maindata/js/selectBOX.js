const categorymaster = new Array('actorM');
const category = new Array('actor')

//全選択
  function AllChecked(){
    const check = document.form.all.checked;
    for(let i = 0; i < categorymaster.length; i++){
        if(document.form.elements[categorymaster[i]].checked === check){
            document.form.elements[categorymaster[i]].checked = check;
            CategoryAllChecked(categorymaster[i],category[i]);
        }
    }
  }

  function CategoryAllChecked(master,name){
      const check = document.form.elements[master].checked;
      for (let i = 0; i < document.form.elements[name].length; i++) {
          document.form.elements[name].checked = check;
      }
  }
  // 一つでもチェックを外すと「全て選択」のチェック外れる
 function　DisChecked(master,name){
     const checks = document.form.elements[name];
     let checksCount = 0;
     for (let i=0; i<checks.length; i++){
      if(checks[i].checked === false){
        document.form.elements[master].checked = false;
        document.form.all.checked = false;
      }else{
        checksCount += 1;
        if(checksCount === checks.length){
          document.form.elements[master].checked = true;
          document.form.all.checked = true;
          for(let j = 0; j < categorymaster.length; j++){
              if(document.form.elements[categorymaster[j]].checked === false){
                  document.form.all.checked = false;
              }
          }
        }
      }
    }
  }
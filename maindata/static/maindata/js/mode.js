$(function () {
  $('div','#mode').click(function(){
    $('div','#modecahnge').html(function() {
        "                            <label>\n" +
        "                                <form action=\"nomal/\" method=\"get\">\n" +
        "                                    <span class=\"btn-square mode mode-js-change\">\n" +
        "                                        <span class=\"glyphicon glyphicon-question-sign\" aria-hidden=\"true\"/> 通常モード\n" +
        "                                        <input type=\"button\" style=\"display: none\" name=\"modechange\" id=\"button\">\n" +
        "                                    </span>\n" +
        "                                </form>\n" +
        "                            </label>"
    });
  },function() {
      $('div', '#modecahnge').html(function () {
          "                            <label>\n" +
          "                                <form action=\"nomal/\" method=\"get\">\n" +
          "                                    <span class=\"btn-square mode mode-js-change\">\n" +
          "                                        <span class=\"glyphicon glyphicon-question-sign\" aria-hidden=\"true\"/> 通常モード\n" +
          "                                        <input type=\"button\" style=\"display: none\" name=\"modechange\" id=\"button\">\n" +
          "                                    </span>\n" +
          "                                </form>\n" +
          "                            </label>"
      });
  })
});
window.onload = function(data) {
    var oShow = document.getElementById('show');

    oShow.innerHTML = "";
    for (var i = 0; i <data[i].length; i++) {
        oShow.innerHTML +=
            "<li>\n" +
            "<figure>\n" +
            "<img src=\"../static/img/1.png\" alt=\"img01\">\n" +
            "<figcaption>\n" +
            "<h3>'+data[i].name+'</h3>\n" +
            "<span>'+data[i].author+'</span>\n" +
            "<a href=\"http://dribbble.com/shots/1115632-Camera\">看一看</a>\n" +
            "</figcaption>\n" +
            "</figure>\n" +
            "</li>"
    }
}
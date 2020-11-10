/*
$(document).ready(function () {
    $('#xuanhuan').click(function () {
            console.log("点击")
            request_data('玄幻小说');
        }
    );
    $('#xiuzhen').click(function () {
            console.log("点击")
            request_data('修真小说');
        }
    );
    $('#dushi').click(function () {
            console.log("点击")
            request_data('都市小说');
        }
    );
    $('#chuanyue').click(function () {
            console.log("点击")
            request_data('穿越小说');
        }
    );
    $('#wangyou').click(function () {
            console.log("点击")
            request_data('网游小说');
        }
    );
    $('#kehuan').click(function () {
            console.log("点击")
            request_data('科幻小说');
        }
    );

});

function request_data(type_name) {
    $.ajax({
            //请求方式
            type: "GET",
            //是否异步
            async: false,
            //请求的媒体类型
            contentType: "application/x-www-form-urlencoded;charset=UTF-8",
            //请求地址
            url: "fenlei/",
            //数据，json字符串
            data: {'type': 2},
            beforeSend: function () {
                $("loading").show();
            },
            //请求成功
            success: function () {
                console.log(result);result
                $('#type_content').empty()
                load_data(result)
            },
            //请求失败，包含具体的错误信息
            error: function (e) {
                console.log(e.status);
                console.log(e.responseText);
            }
        }
    );
}

function load_data(data) {
      var html='';
          for(var i=0;i<data.length;i++) {
              html+='<div class="der">'
                    +'<a href="../to_detail?name='+data[i].name+'&author='+data[i].author+'">'
                        +'<img src="'+data[i].imgurl+'" width="90" height="120">'
                    +'</a>'
                    +'<span>'+data[i].name+'</span>'
                +'</div>'
          }
          $('#type_content').append(html)
}

*/

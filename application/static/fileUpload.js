/**
 * jQuery上传文件扩展插件
 * 使用方法示例(方括号中为可选参数)：
 * $.fileUpload({
 *                      url: ...,  // 文件上传地址
 *                      file: "#uploadFile",    // css选择器指定的待上传文件标签
 *                      [fileName:...],     // 上传至服务器的文件名
 *                      [data:{id:1,user:"小明"}],  // 自定义一起上传的参数
 *                      [success: function(data){console.log(data)}]  // 上传成功后的回调函数
 *                     });
 *
 * 注意：本插件IE9及以下不支持
 *
 * author: lixk
 * date: 2016/11/24
 */

var fileUpload = function(params){
    var file = $(params["file"]).get(0) || {}; //文件对象
    var fileName = params["fileName"] || file.name;  //上传至服务器的文件名，默认file的name
    var url = params["url"];  //上传地址
    var data = params["data"] || {}; //自定义参数
    var success = params["success"]; //上传成功的回调函数
    var files = file.files || []; //文件
    var formData = new FormData(); //创建上传表单
    $.each(files, function(i, v){
        formData.append(fileName, v);
    });
    //向表单添加参数
    for(var key in data) {
        formData.append(key, data[key]);
    }
    //向服务器发送表单数据
    $.ajax({
        url: url,
        type: "POST",
        data: formData,
        processData: false,  // 告诉jQuery不要去处理发送的数据
        contentType: false,   // 告诉jQuery不要去设置Content-Type请求头
        success: function(data) { //请求成功，回调
          if(success){
              success(data);
          }
        }
    });
}

//添加jQuery扩展
jQuery.extend({fileUpload: fileUpload});
// ==UserScript==  
// @name         Javascript Injection
// @version      0.8.1
// @author       bugwhen@gmail.com
// @namespace    https://github.com/bugzhu
// @description  Chrome扩展测试：JS注入Demo
// @match        *://www.baidu.com/*
// ==/UserScript== 
function install(callback)
{
    console.log("install");
    if (typeof(jQuery) == "undefined")
    {
        var script = document.createElement("script");
        script.type = "text/javascript";
        script.src = "http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js";
        document.head.appendChild(script);
        console.log(script);
        
        var injection = document.createElement("script");
        injection.type = "text/javascript";
        injection.textContent = "jQuery.noConflict();(" + callback.toString() + ")(jQuery, window);";
        
        script.addEventListener('load', function()
        {
            console.log("jQuery:200");
            document.head.appendChild(injection);
        });
    }
}
install(function($, window)
{   
	console.log(1);
});
/**
这段代码简单地演示了编写chrome扩展插件的方法：首先定义一下插件的名称(@name)、版本号(@version)等信息，其中@match字段是控制插件的作用域，否则会在所有网站生效，然后另存为[name].user.js，并拖拽到chrome扩展界面就可以使用了。
*/

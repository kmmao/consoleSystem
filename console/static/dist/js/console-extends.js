/**
 * Created by apple on 2016/11/28.
 */

/**
 * [storage html5本地存储-localStorage]
 * @type {[type]}
 */
var storage = window.localStorage;

/**
 * [showStorage 展示所有本地存储的数据]
 * @return {[type]} [description]
 */
function showStorage(){
	for (var i = storage.length - 1; i >= 0; i--) {
		console.log(storage.key(i)+":"+storage.getItem(storage.key(i)));
	}
}

/**
 * [getFileContent 得到文件数据]
 * @return {[type]} [description]
 * var jsonData = {
        "file": "/wms/hello",
        "content": "helooasdasdsadasda",
        "backupcount": 5,
        "syncfile": {
            "infos": [{
                "host": "192.168.250.178",
                "file": "/home/testhello",
            }, {
                "host": "192.168.250.278",
                "file": "/home/testlo"
            }]
        }
    };
 */
function getConfigFileInfo(){
	var configFileInfo = window.localStorage.configFileInfo;
	if(typeof(configFileInfo) == 'undefined'){
		//新增
		configFileInfo = {
			"file":"",
			"content":"",
			"backupcount":0,
			"syncfile":{
				"infos":new Array()
			}
		};
	}else{
		configFileInfo = JSON.parse(configFileInfo);
	}
	return configFileInfo;
}

/**
 * [saveConfigFileInfo 保存文件数据]
 * @param  {[type]} configFileInfo [description]
 * @return {[type]}                [description]
 */
function saveConfigFileInfo(configFileInfo){
	window.localStorage.configFileInfo = JSON.stringify(configFileInfo);
}

/**
 * [valuechange 时时更新]
 * @type {Object}
 */
$.event.special.valuechange = {
	teardown:function(namespaces){
		$(this).unbind('.valuechange');
	},
	handler:function(e){
		$.event.special.valuechange.triggerChanged($(this));
	},
	add:function(obj){
		$(this).on('keyup.valuechange cut.valuechange paste.valuechange input.valuechange',obj.selector,$.event.special.valuechange.handler)
	},
	triggerChanged:function(element){
		var current = element[0].contentEditable === 'true' ? element.html() :element.val(),previous = typeof element.data('previous') === 'undefined' ? element[0].defaultValue :element.data('previous')
		if(current !== previous){
			element.trigger('valuechange',[element.data('previous')])
			element.data('previous',current)
		}
	}
}

//调用如下
// $(function(){
// 	$('#text').on('valuechange',function(e,previous){
// 		$('#output').append('previous:'+previous+'--current:'+$(this).val()+'<br/>')
// 	})
// })





























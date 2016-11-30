/**
 * templates file manage for console
 * 
 * Created by liukai on 2016/11/18.
 */

(function($) {
    /**
     * [templatesManage 主体内容]
     * @type {Object}
     */
    var templatesManage = {
        /**
         * init
         */
        init: function() {
            this.layout();
            this.domEvent();
            //other
        },
        /**
         * layout
         */
        layout: function() {
            initTable();
        },
        /**
         * base event
         */
        domEvent: function() {
            /**
             * [编辑]
             * @param  {[type]} event) {                           event.preventDefault();                            } [description]
             * @return {[type]}        [description]
             */
            $(document).on('click', '.edit', function(event) {
                event.preventDefault();
                /* Act on the event */
                $.post('/console/tp/get/', {
                    id: $(this).attr('data-id')
                }, function(res) {
                    $('#fileId').val(res.id);
                    $("#fileName").val(res.name);
                    var unicode = BASE64.decoder(res.content); //返回会解码后的unicode码数组。 
                    var str = '';
                    for (var i = 0, len = unicode.length; i < len; ++i) {
                        str += String.fromCharCode(unicode[i]);
                    }
                    $("#fileContent").val(str);
                    //展示内容
                    layer.open({
                        title: '编辑模板文件',
                        type: 1,
                        area: ['1200px', '760px'],
                        fixed: false, //不固定
                        maxmin: true,
                        content: $("#file-div"),
                        btn: ['保存', '取消'],
                        yes: function() {
                            var jsonData = $("#fileForm").serializeObject();

                            jsonData.fileContent = BASE64.encoder(jsonData.fileContent);
                            $.post('/console/tp/save/', { fileInfo: JSON.stringify(jsonData) }, function(res) {
                                layer.msg(res.msg);
                                if (res.code == 0) {
                                    window.setTimeout(function() {
                                        layer.closeAll();
                                    }, 1000);
                                }
                            }, 'json');
                        },
                        cancel: function() {
                            layer.closeAll();
                        }
                    });
                }, 'json');
            });
            /**
             * [删除]
             * @param  {[type]} event) {                           event.preventDefault();                            } [description]
             * @return {[type]}        [description]
             */
            $(document).on('click', '.delete', function(event) {
                event.preventDefault();
                /* Act on the event */
                $.post('/console/dir/deleteDir/' + window.localStorage.env, {
                    dirPath: $select.attr('data')
                }, function(res) {
                    layer.msg(res.info);
                    if (res.status == 200) {
                        window.setTimeout(function() {
                            layer.closeAll();
                            breadcrumb.pop(0);
                        }, 1000);
                    }
                }, 'json');
            });

            /**
             * [文件添加]
             * @param  {[type]} ){                         } [description]
             * @return {[type]}     [description]
             */
            $("#addFile").click(function() {
                layer.open({
                    title: '新建模板文件',
                    type: 1,
                    area: ['1200px', '760px'],
                    fixed: false, //不固定
                    maxmin: true,
                    content: $("#fileContent"),
                    yes: function() {
                        $.post('/console/dir/renameDir/', {
                            parentDir: parentDir,
                            newName: $("#dirName").val(),
                            oldName: oldName
                        }, function(res) {
                            layer.msg(res.info);
                            if (res.status == 200) {
                                window.setTimeout(function() {
                                    layer.closeAll();
                                    breadcrumb.pop(0);
                                }, 1000);
                            }
                        }, 'json');
                    },
                    cancel: function() {
                        layer.closeAll();
                    }
                });
                //layer.full(index);
            });
        }
    };
    templatesManage.init();
    /**
     * [initTable 动态初始化列表]
     * @return {[type]}      [description]
     */
    function initTable() {
        $('#dataTables-templatesManage').DataTable({
            //destroy: true,
            "ServerSide": true,
            "processing": true,
            "ajax": {
                "url": "/console/getTplist/",
                "type": "POST"
            },
            "language": {
                "lengthMenu": "每页 _MENU_ 条记录",
                "zeroRecords": "",
                "info": "第 _PAGE_ 页 ( 总共 _PAGES_ 页 )",
                "infoEmpty": "无记录",
                "infoFiltered": "(从 _MAX_ 条记录过滤)",
                "loadingRecords": "加载中...",
                "search": "过滤文件名:",
                "sEmptyTable": "",
                "paginate": {
                    "previous": "上一页",
                    "next": "下一页"
                }
            },
            "columnDefs": [{
                "render": function(data, type, row) {
                    return '<button type="button" class="btn btn-link edit" data-id="' + data + '">编辑</button>  <button type="button" class="btn btn-link delete" data-id="' + data + '">删除</button>';
                },
                orderable: false,
                searchable: false,
                targets: 1,
                width: '120px'
            }]
        });
    }
})(jQuery);

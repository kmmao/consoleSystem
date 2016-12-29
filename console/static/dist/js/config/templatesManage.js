/**
 * templates file manage for console
 * 
 * Created by liukai on 2016/11/18.
 */

(function($) {
    var form = $("#fileForm");
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
             * [messages 验证码]
             * @type {Object}
             */
            $.validator.messages = {
                required: "输入不能为空."
            };

            /**
             * [form 表单]
             * @type {[type]}
             */
            form.validate({
                errorPlacement: function errorPlacement(error, element) {
                    layer.tips(error.html(), element, {
                        tips: [1, '#CA1622'],
                        time: 2000,
                        tipsMore: true
                    });
                }
            });

            /**
             * [编辑]
             * @param  {[type]} event) {                           event.preventDefault();                            } [description]
             * @return {[type]}        [description]
             */
            $(document).on('click', '.edit', function(event) {
                event.preventDefault();
                clearContent();
                var loadView = layer.load(1, {
                    shade: [0.5, '#fff'] //0.1透明度的白色背景
                });
                /* Act on the event */
                $.post('/console/tp/get/', {
                    id: $(this).attr('data-id')
                }, function(res) {
                    $('#fileId').val(res.id);
                    $("#fileName").val(res.name);
                    $("#fileContent").val(res.content);
                    layer.close(loadView);
                    //展示内容
                    layer.open({
                        title: '编辑模板文件',
                        type: 1,
                        area: ['1200px', '760px'],
                        skin: 'layui-layer-rim', //加上边框
                        fixed: false, //不固定
                        maxmin: true,
                        content: $("#file-div"),
                        btn: ['保存', '取消'],
                        yes: function() {
                            fileSave();
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
                var id = $(this).attr('data-id');
                /* Act on the event */
                layer.confirm('确认删除？', {
                    btn: ['确认', '取消'] //按钮
                }, function() {
                    $.post('/console/tp/delete/', {
                        id: id
                    }, function(res) {
                        layer.msg(res.msg);
                        if (res.code == 0) {
                            window.setTimeout(function() {
                                //window.location.href = '/console/templatesManage';
                                initTable();
                                layer.closeAll();
                            }, 1000);
                        }
                    }, 'json');
                }, function() {
                    layer.closeAll();
                });
            });

            /**
             * [文件添加]
             * @param  {[type]} ){                         } [description]
             * @return {[type]}     [description]
             */
            $("#addFile").click(function() {
                clearContent();
                layer.open({
                    title: '新建模板文件',
                    type: 1,
                    area: ['1200px', '760px'],
                    skin: 'layui-layer-rim', //加上边框
                    fixed: false, //不固定
                    maxmin: true,
                    content: $("#file-div"),
                    btn: ['保存', '取消'],
                    yes: function() {
                        fileSave();
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
     * [clearContent 清空内容]
     * @return {[type]} [description]
     */
    function clearContent() {
        $('#fileId').val('');
        $("#fileName").val('');
        $('#fileContent').val('');
    }

    /**
     * [fileSave 保存]
     * @return {[type]} [description]
     */
    function fileSave() {
        if (form.valid()) {
            var layerLoad = layer.load(1, {
                shade: [0.1, '#fff'] //0.1透明度的白色背景
            });
            var jsonData = $("#fileForm").serializeObject();

            jsonData.fileContent = BASE64.encoder(jsonData.fileContent);
            $.post('/console/tp/save/', { fileInfo: JSON.stringify(jsonData) }, function(res) {
                layer.msg(res.msg);
                if (res.code == 0) {
                    window.setTimeout(function() {
                        initTable();
                        layer.closeAll();
                    }, 1000);
                }else{
                    layer.close(layerLoad);
                }
            }, 'json');
        } else {
            return form.valid();
        }
    }

    /**
     * [initTable 动态初始化列表]
     * @return {[type]}      [description]
     */
    function initTable() {
        $('#dataTables-templatesManage').DataTable({
            destroy: true,
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
                targets: 2,
                width: '120px'
            }, {
                targets: 1,
                width: '150px'
            }]
        });
    }
})(jQuery);

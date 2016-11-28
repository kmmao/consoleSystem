/**
 * config file manage for console
 * 
 * Created by liukai on 2016/11/18.
 */

(function($) {
    /**
     * [breadcrumb 初始化路径]
     * @type {[type]}
     */
    var breadcrumb = $('#my-breadcrumb').breadcrumb();
    /**
     * [configFileManage 主体内容]
     * @type {Object}
     */
    var configFileManage = {
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
            //定义环境
            window.localStorage.env = $("#envSelect").find("option:selected").text().trim();

            var path = $("#envSelect").val();
            $('#my-breadcrumb').find("li").remove();
            breadcrumb.push(path);
            initTable(path);
        },
        /**
         * base event
         */
        domEvent: function() {
            /**
             * [改变环境下拉框]
             * @param  {[type]} ){                         } [description]
             * @return {[type]}     [description]
             */
            $("#envSelect").change(function() {
                window.localStorage.env = $(this).find("option:selected").text().trim();
                $('#my-breadcrumb').find("li").remove();
                breadcrumb.push($(this).val());
            });
            /**
             * [路径导航改变]
             * @param  {[type]} el    [description]
             * @param  {[type]} path) {                           console.log(path);            } [description]
             * @return {[type]}       [description]
             */
            $('#my-breadcrumb').on('change', function(el, path) {
                initTable(path);
            });
            /**
             * checkbox全选
             * @param  {[]}
             * @return {[type]}
             */
            $("#checkAll").on("click", function() {
                if ($(this).prop("checked") === true) {
                    $("input[name='checkList']").prop("checked", $(this).prop("checked"));
                    $('#dataTables-configFileManage tbody tr').addClass('selected');
                } else {
                    $("input[name='checkList']").prop("checked", false);
                    $('#dataTables-configFileManage tbody tr').removeClass('selected');
                }
            });
            /**
             * 删除选中行
             * @param  {[type]}
             * @return {[type]}
             */
            $('#dataTables-configFileManage').on('click', 'tr input[name="checkList"]', function() {
                if ($(this).prop('checked')) {
                    $('[name=checkList]:checkbox').prop('checked', false);
                    $(this).prop('checked', true);
                } else {
                    $(this).prop('checked', false);
                }
            });

            /**
             * [文件夹点击]
             * @param  {[type]} ){                         } [description]
             * @return {[type]}     [description]
             */
            $("#dataTables-configFileManage").on('click', '.dirClick', function() {
                var path = $(this).attr("data");
                breadcrumb.push(path.split("/").pop());
            });

            /**
             * [文件点击]
             * @param  {[type]} ) {                           var path [description]
             * @return {[type]}   [description]
             */
            $("#dataTables-configFileManage").on('click', '.fileClick', function() {
                //清空localStorage-configFileInfo
                localStorage.removeItem('configFileInfo');
                var path = $(this).attr("data"); //得到全路径
                //获取文件
                $.post('/file/getFile/' + window.localStorage.env, { filePath: path }, function(res) {
                    if (res.status == 200) {
                        //封装到localStorage
                        saveConfigFileInfo(res);
                        window.localStorage.isEditForFile = true;
                        var index = layer.open({
                            title: '文件编辑',
                            type: 2,
                            area: ['1200px', '760px'],
                            fixed: false, //不固定
                            maxmin: true,
                            content: '/fileIframe'
                        });
                    } else {
                        layer.msg('系统异常，请联系管理员。');
                    }
                }, 'json');
            });

            /**
             * [文件重命名]
             * @param  {[type]} )             {                           $("#dirName").val("");                var parentDir [description]
             * @param  {[type]} function(res) {                                                                                              layer.msg(res.info);                                    if (res.status [description]
             * @return {[type]}               [description]
             */
            $("#fileRename").click(function() {
                $("#fileName").val("");
                var parentDir = breadcrumb.extractPwd($('#my-breadcrumb').children('li'));
                var $tmp = $('[name=checkList]:checkbox');
                if ($tmp.filter(':checked').length == 0) {
                    layer.msg("未选择。");
                } else {
                    var $select = $tmp.filter(':checked');
                    if ($select.attr("isdir") == "false") {
                        var oldName = $select.attr("data").split('/').pop();
                        layer.open({
                            type: 1,
                            title: '文件重命名', //不显示标题
                            area: ['auto', 'auto'],
                            btn: ['保存', '取消'],
                            shadeClose: false,
                            content: $("#file-dialog"), //捕获的元素
                            yes: function() {
                                $.post('/file/renameFile/' + window.localStorage.env, {
                                    parentDir: parentDir,
                                    newName: $("#fileName").val(),
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
                    } else {
                        layer.msg("请选择文件");
                    }
                }
            });
            /**
             * [文件夹重命名]
             * @param  {[type]} ){                         } [description]
             * @return {[type]}     [description]
             */
            $("#dirRename").click(function() {
                $("#dirName").val("");
                var parentDir = breadcrumb.extractPwd($('#my-breadcrumb').children('li'));
                var $tmp = $('[name=checkList]:checkbox');
                if ($tmp.filter(':checked').length == 0) {
                    layer.msg("未选择。");
                } else {
                    var $select = $tmp.filter(':checked');
                    if ($select.attr("isdir") == "true") {
                        var oldName = $select.attr("data").split('/').pop();
                        layer.open({
                            type: 1,
                            title: '文件夹重命名', //不显示标题
                            area: ['auto', 'auto'],
                            btn: ['保存', '取消'],
                            shadeClose: false,
                            content: $("#dir-dialog"), //捕获的元素
                            yes: function() {
                                $.post('/dir/renameDir/' + window.localStorage.env, {
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
                    } else {
                        layer.msg("请选择文件夹");
                    }
                }
            });
            /**
             * [删除]
             * @param  {[type]} ){                         } [description]
             * @return {[type]}     [description]
             */
            $("#delete").click(function() {
                var $tmp = $('[name=checkList]:checkbox');
                if ($tmp.filter(':checked').length == 0) {
                    layer.msg("未选择。");
                } else {
                    var $select = $tmp.filter(':checked');
                    if ($select.attr("isdir") == "true") {
                        $.post('/dir/deleteDir/' + window.localStorage.env, {
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
                    } else {
                        $.post('/file/deleteFile/' + window.localStorage.env, {
                            filePath: $select.attr('data')
                        }, function(res) {
                            layer.msg(res.info);
                            if (res.status == 200) {
                                window.setTimeout(function() {
                                    layer.closeAll();
                                    breadcrumb.pop(0);
                                }, 1000);
                            }
                        }, 'json');
                    }
                }
            });
            /**
             * [文件添加]
             * @param  {[type]} ){                         } [description]
             * @return {[type]}     [description]
             */
            $("#addFile").click(function() {
                localStorage.removeItem('configFileInfo');
                window.localStorage.isEditForFile = false;
                var index = layer.open({
                    title: '文件添加',
                    type: 2,
                    area: ['1200px', '760px'],
                    fixed: false, //不固定
                    maxmin: true,
                    content: '/fileIframe'
                });
                //layer.full(index);
            });
            /**
             * [文件夹添加]
             * @param  {[type]} ){} [description]
             * @return {[type]}       [description]
             */
            $("#addDir").click(function() {
                var dirPath = breadcrumb.extractPwd($('#my-breadcrumb').children('li'));
                //清空数据
                $("#dirName").val("");

                layer.open({
                    type: 1,
                    title: '新增文件夹', //不显示标题
                    area: ['auto', 'auto'],
                    btn: ['保存', '取消'],
                    shadeClose: false,
                    content: $("#dir-dialog"), //捕获的元素
                    yes: function() {
                        //进行新增操作
                        $.post('/dir/addDir/' + window.localStorage.env, {
                            dirPath: dirPath + "/" + $("#dirName").val()
                        }, function(res) {
                            layer.msg(res.info);
                            if (res.status == 200) {
                                window.setTimeout(function() {
                                    layer.closeAll();
                                    breadcrumb.pop(0);
                                    //breadcrumb.push(dirPath.split('/').pop());
                                }, 1000);
                            }
                        }, 'json');
                    },
                    cancel: function() {
                        layer.closeAll();
                    }
                });
            });
        }
    };
    configFileManage.init();
    /**
     * [initTable 动态初始化列表]
     * @param  {[type]} path [description]
     * @return {[type]}      [description]
     */
    function initTable(path) {
        $('#dataTables-configFileManage').DataTable({
            destroy: true,
            //retrieve: true,
            responsive: true,
            "ServerSide": true,
            //data: jsonData["infos"],
            //post request
            "processing": true,
            "ajax": {
                "url": "/dir/scan/" + window.localStorage.env,
                "dataSrc": "infos",
                "type": "POST",
                "data": {
                    dirPath: path
                }
            },
            //"sAjaxDataProp": "data.infos"，
            "language": {
                "lengthMenu": "每页 _MENU_ 条记录",
                "zeroRecords": "",
                "info": "第 _PAGE_ 页 ( 总共 _PAGES_ 页 )",
                "infoEmpty": "无记录",
                "infoFiltered": "(从 _MAX_ 条记录过滤)",
                "loadingRecords": "加载中...",
                "search": "过滤目录及文件:",
                "sEmptyTable": "",
                "paginate": {
                    "previous": "上一页",
                    "next": "下一页"
                }
            },
            "columns": [{
                "data": ""
            }, {
                "data": "name"
            }],
            "columnDefs": [{
                "render": function(data, type, row) {
                    if (path == '/') {
                        return '<input type="checkbox" name="checkList" isdir="' + row["isdir"] + '" data="' + path + row["name"] + '">';
                    } else {
                        return '<input type="checkbox" name="checkList" isdir="' + row["isdir"] + '" data="' + path + '/' + row["name"] + '">';
                    }
                },
                orderable: false,
                targets: 0
            }, {
                "render": function(data, type, row) {
                    //console.log(row["isdir"])
                    if (row["isdir"] == true) {
                        if (path == '/') {
                            return '<p><i class="dir"></i>&nbsp&nbsp<a href="javascript:void(0)" class="dirClick" data="' + path + data + '">' + data + '</a></p>';
                        } else {
                            return '<p><i class="dir"></i>&nbsp&nbsp<a href="javascript:void(0)" class="dirClick" data="' + path + '/' + data + '">' + data + '</a></p>';
                        }
                    } else {
                        if (path == '/') {
                            return '<p><i class="file"></i>&nbsp&nbsp<a href="javascript:void(0)" class="fileClick" data="' + path + data + '">' + data + '</a></p>';
                        } else {
                            return '<p><i class="file"></i>&nbsp&nbsp<a href="javascript:void(0)" class="fileClick" data="' + path + '/' + data + '">' + data + '</a></p>';
                        }
                    }

                },
                targets: 1
            }], //第一列禁止排序
            "order": [
                [0, null]
            ], //第一列排序图标改为默认
        });
    }
})(jQuery);

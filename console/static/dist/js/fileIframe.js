/**
 * fileIframe file manage for console
 * 
 * Created by liukai on 2016/11/18.
 */

(function($) {
    var jsonData, tableData = new Array(),
        serverUrlInfos, dirPath = '',
        index = parent.layer.getFrameIndex(window.name); //获取窗口索引;
    /**
     * [fileIframe 主体内容]
     * @type {Object}
     */
    var fileIframe = {
        /**
         * init
         */
        init: function() {
            this.layout();
            this.domEvent();
            this.initData();
            //other
        },
        /**
         * [initData 初始化数据]
         * @return {[type]} [description]
         */
        initData: function() {
            dirPath = parent.$('#my-breadcrumb').breadcrumb().extractPwd(parent.$('#my-breadcrumb').children('li'));
            jsonData = getConfigFileInfo();
            //处理文件列表
            infosHandle();
            if (window.localStorage.isEditForFile == 'true') {
                //文件名只读
                $('#fileName').attr('readonly', 'readonly');
                delete jsonData['status'];
                //delete jsonData['backupfiles'];
                $("#fileName").val(jsonData['file'].split('/').pop());
                //console.log(jsonData['file']);
                $('#fileContent').val(jsonData['content']);
                $('#backupcount').val(jsonData['backupcount']);
                //备份文件显示
                $("#showContent").html('备份文件');
                //封装备份文件列表
                var backupfilesLst = '';
                $.each(jsonData['backupfiles'], function(i, val) {
                    backupfilesLst += '<a href="javascript:void(0)" fileName="' + jsonData['file'] + '" class="list-group-item backupfileClick">' + val + '</a>';
                });
                if (backupfilesLst != '') {
                    //去除无
                    $("#backupfilesLst").find('li').remove();
                    //更新列表
                    $("#backupfilesLst").find('a').after(backupfilesLst);
                }
            } else {
                $("#showContent").html('模板文件');
                $.post('/console/tp/getTpList/', function(data, textStatus, xhr) {
                    var tpFilesList = '';
                    if (data.length > 0) {
                        for (var i = 0; i < data.length; i++) {
                            tpFilesList += '<a href="javascript:void(0)" fileId="' + data[i]['id'] + '" class="list-group-item tpfileClick">' + data[i]['name'] + '</a>';
                        }
                        //去除无
                        $("#backupfilesLst").find('li').remove();
                        //更新列表
                        $("#backupfilesLst").find('a').after(tpFilesList);
                    }
                }, 'json');
            }
            //初始化下拉列表
            $.post('/console/getServerUrlInfo/' + window.localStorage.env, function(res) {
                serverUrlInfos = res.split('|');
                //console.log(serverUrlInfos);
                initTableEdit(tableData);
            });
        },
        /**
         * layout
         */
        layout: function() {

        },
        /**
         * base event
         */
        domEvent: function() {
            /**
             * [模块文件点击事件]
             * @param  {[type]} event)        {                                        event.preventDefault();                                                       $.post('/console/tp/get/', {                    id: $(this).attr('fileId')                } [description]
             * @param  {[type]} function(res) {                                                                   var unicode [description]
             * @param  {[type]} btn:          ['导入'         [description]
             * @param  {[type]} '取消']         [description]
             * @param  {[type]} moveType:     1             [description]
             * @param  {[type]} resize:       false         [description]
             * @param  {[type]} yes:          function(     [description]
             * @return {[type]}               [description]
             */
            $(document).on('click', '.tpfileClick', function(event) {
                event.preventDefault();
                /* Act on the event */
                $.post('/console/tp/get/', {
                    id: $(this).attr('fileId')
                }, function(res) {
                    $('#showBackupFileContent').val(res.content);
                    //展示内容
                    layer.open({
                        type: 1,
                        title: res.name, //不显示标题
                        skin: 'layui-layer-rim', //加上边框
                        area: ['600px', '400px'],
                        closeBtn: 0, //不显示关闭按钮
                        content: $('#showBackupContent'),
                        btn: ['导入', '取消'],
                        moveType: 1,
                        resize: false,
                        yes: function() {
                            //进行确认导入
                            layer.confirm('确认导入？', {
                                btn: ['导入', '取消'] //按钮
                            }, function() {
                                $("#fileContent").val($('#showBackupFileContent').val());
                                layer.closeAll();
                            }, function() {
                                layer.closeAll();
                            });
                        },
                        cancel: function() {
                            layer.closeAll();
                        }
                    });
                }, 'json');
            });
            /**
             * [获取备份文件]
             * @param  {[type]} event)         {                                 event.preventDefault();                                                                 var                                                       backupfile [description]
             * @param  {[type]} function(data, textStatus,   xhr) {                                           $('#showBackupFileContent').val(data['content']);                                                                                                                        layer.open({                                         type: 1,                                       title: backupfile,                         skin: 'layui-layer-rim',                         area: ['600px', '400px'],                        closeBtn: 0,                         content: $('#showBackupContent'),                        btn: ['导入', '取消'],                        moveType: 1,                        resize: false,                        yes: function() {                                                        layer.confirm('确认导入？', {                                btn: ['导入', '取消']                             } [description]
             * @param  {[type]} function()     {                                                                                                                         $("#fileContent").val($('#showBackupFileContent').val());                                                                    layer.closeAll();                                   } [description]
             * @param  {[type]} function(      [description]
             * @return {[type]}                [description]
             */
            $(document).on('click', '.backupfileClick', function(event) {
                event.preventDefault();
                var backupfile = $(this).html().trim();
                /* Act on the event */
                $.post('/console/file/getFileBackup/' + window.localStorage.env, { filePath: $(this).attr('fileName'), backupfile: backupfile }, function(data, textStatus, xhr) {
                    $('#showBackupFileContent').val(data['content']);
                    //取得备份文件数据，并弹窗展现
                    layer.open({
                        type: 1,
                        title: backupfile, //不显示标题
                        skin: 'layui-layer-rim', //加上边框
                        area: ['600px', '400px'],
                        closeBtn: 0, //不显示关闭按钮
                        content: $('#showBackupContent'),
                        btn: ['导入', '取消'],
                        moveType: 1,
                        resize: false,
                        yes: function() {
                            //进行确认导入
                            layer.confirm('确认导入？', {
                                btn: ['导入', '取消'] //按钮
                            }, function() {
                                $("#fileContent").val($('#showBackupFileContent').val());
                                layer.closeAll();
                            }, function() {
                                layer.closeAll();
                            });
                        },
                        cancel: function() {
                            layer.closeAll();
                        }
                    });
                }, 'json');
            });
            /**
             * [添加行]
             * @param  {[type]} ){                         } [description]
             * @return {[type]}     [description]
             */
            $(document).on('click', '#addRow', function() {
                var serverUrlInfo = serverUrlInfos[0].split(':');
                tableData.push({
                    'host': serverUrlInfo[1], //默认第一个URL地址--（这里要处理下，如果没有地址的情况下要怎么处理）
                    'file': '',
                    'modeltype':serverUrlInfo[0]
                });
                initTableEdit(tableData);
            });

            /**
             * [path change]
             * @param  {[type]} e         [description]
             * @param  {[type]} previous) {                           var index [description]
             * @return {[type]}           [description]
             */
            $(document).on('valuechange', '.indexSelect', function(e, previous) {
                var index = $(this).parents('tr').find('.indexSelect').attr('indexvalue');
                var obj = {
                    'host': $(this).parents('tr').find('.indexSelectIp').find("option:selected").text(),
                    'file': $(this).val(),
                    'modeltype':$(this).parents('tr').find('.indexSelectIp').find("option:selected").attr('modeltype')
                };
                tableData.splice(index, 1, obj);
            });

            /**
             * [ip change]
             * @param  {[type]} e         [description]
             * @param  {[type]} previous) {                           var index [description]
             * @return {[type]}           [description]
             */
            $(document).on('valuechange', '.indexSelectIp', function(e, previous) {
                var index = $(this).parents('tr').find('.indexSelect').attr('indexvalue');
                var obj = {
                    'host': $(this).find("option:selected").text(),
                    'file': $(this).parents('tr').find('.indexSelect').val(),
                    'modeltype':$(this).find("option:selected").attr('modeltype')
                };
                tableData.splice(index, 1, obj);
            });

            /**
             * [初始化刪除按钮]
             * @param  {[type]} ) {                           var index [description]
             * @return {[type]}   [description]
             */
            $(document).on('click', '.delRow', function() {
                var index = $(this).parents('tr').find('.indexSelect').attr('indexvalue');
                tableData.splice(index, 1);
                initTableEdit(tableData);
            });

            /**
             * [messages 验证码]
             * @type {Object}
             */
            $.validator.messages = {
                required: "输入不能为空.",
                remote: "用户名已经存在.", // 自己定义
                email: "请输入一个有效的电子邮件地址.",
                url: "请输入一个有效的URL.",
                date: "请输入一个有效的日期.",
                dateISO: "请输入一个有效的日期 ( ISO ) ( 例：2014/08/28 ).",
                number: "请输入一个有效的数字.",
                digits: "请输入一个正整数.",
                creditcard: "请输入一个有效的信用卡号.",
                equalTo: "请再次输入相同的值.",
                maxlength: $.validator.format("请输入不超过{0}个字符."),
                minlength: $.validator.format("请输入至少{0}个字符."),
                rangelength: $.validator.format("请输入一个字符长{0}至{1}的字符."),
                range: $.validator.format("请输入一个{0}至{1}的数."),
                max: $.validator.format("请输入一个值小于或等于{0}的数."),
                min: $.validator.format("请输入一个值大于或等于{0}的数.")
            };

            /**
             * [form 表单]
             * @type {[type]}
             */
            var form = $("#file-form");
            form.validate({
                errorPlacement: function errorPlacement(error, element) {
                    //element.before(error);
                    //element.after(error);
                    //layer.msg('*号必填');
                    layer.tips(error.html(), element, {
                        tips: [1, '#3595CC'],
                        time: 2000,
                        tipsMore: true
                    });
                }
            });

            /**
             * [onStepChanging steps]
             * @param  {[type]} event        [description]
             * @param  {[type]} currentIndex [description]
             * @param  {String} newIndex)    {                                                form.validate().settings.ignore [description]
             * @param  {String} onFinishing: function(event, currentIndex) {                                                                form.validate().settings.ignore      [description]
             * @param  {[type]} onFinished:  function(event, currentIndex) {                                                                layer.msg(JSON.stringify(jsonData));                             }            } [description]
             * @return {[type]}              [description]
             */
            form.children("div").steps({
                headerTag: "h3",
                bodyTag: "section",
                transitionEffect: "slideLeft",
                labels: {
                    next: "下一步",
                    previous: "上一步",
                    finish: "完成"
                },
                /**
                 * [onStepChanging 下一步，上一步前的验证]
                 * @param  {[type]} event        [description]
                 * @param  {[type]} currentIndex [description]
                 * @param  {[type]} newIndex     [description]
                 * @return {[type]}              [description]
                 */
                onStepChanging: function(event, currentIndex, newIndex) {
                    //填写文件-下一步
                    if (currentIndex == 0) {
                        jsonData['file'] = $("#fileName").val();
                        jsonData['content'] = $('#fileContent').val();
                        jsonData['backupcount'] = $('#backupcount').val();
                        console.log('填写文件：' + JSON.stringify(jsonData));

                        form.validate().settings.ignore = ":disabled,:hidden";
                        return form.valid();
                    }
                    //关联主机-下一步
                    if (currentIndex == 1) {
                        $('#showFileName').val(jsonData['file']);
                        $('#showFileContent').val(jsonData['content']);
                        initTableFinal(tableData);
                        console.log('关联主机：' + JSON.stringify(jsonData));
                    }
                    //下发执行（确认）-下一步
                    if (currentIndex == 2 && newIndex == 3) {
                        form.validate().settings.ignore = ":disabled,:hidden";
                        if (form.valid()) {
                            //处理转换
                            //Integer.parseInt(String)
                            if (jsonData['backupcount'] == '') {
                                jsonData['backupcount'] = 5;
                            } else {
                                jsonData['backupcount'] = Number(jsonData['backupcount']);
                            }
                            if (dirPath == '/') {
                                jsonData['file'] = dirPath + jsonData['file'];
                            } else {
                                jsonData['file'] = dirPath + "/" + jsonData['file'];
                            }
                            //封装回到jsonData
                            convJsonData();
                            //console.log(jsonData);
                            //console.log(jsonData['file']);
                            //请求下发数据，并返回数据，展示

                            jsonData['content'] = BASE64.encoder(jsonData['content']);

                            delete jsonData['backupfile'];

                            if (window.localStorage.isEditForFile == 'true') {
                                $.post('/console/file/updateFile/' + window.localStorage.env, { configFileInfo: JSON.stringify(jsonData) }, function(res) {
                                    //layer.msg(res.info);
                                    $("#loading").remove();
                                    $("#opinfo").html(res.info);
                                }, 'json');
                            } else {
                                $.post('/console/file/createFile/' + window.localStorage.env, { configFileInfo: JSON.stringify(jsonData) }, function(res) {
                                    //layer.msg(res.info);
                                    $("#loading").remove();
                                    $("#opinfo").html(res.info);
                                }, 'json');
                            }
                            console.log('下发执行（确认）：' + JSON.stringify(jsonData));
                        } else {
                            return form.valid();
                        }
                    }
                    //执行层内容展示
                    if (currentIndex == 3) {
                        if (currentIndex != newIndex) {
                            layer.msg("已执行下发，不能再进行其他操作。");
                            return false;
                        }
                    }

                    return true;
                },
                /**
                 * [onFinishing 完成前的验证]
                 * @param  {[type]} event        [description]
                 * @param  {[type]} currentIndex [description]
                 * @return {[type]}              [description]
                 */
                onFinishing: function(event, currentIndex) {
                    form.validate().settings.ignore = ":disabled";
                    return form.valid();
                },
                /**
                 * [onFinished 完成操作]
                 * @param  {[type]} event        [description]
                 * @param  {[type]} currentIndex [description]
                 * @return {[type]}              [description]
                 */
                onFinished: function(event, currentIndex) {
                    parent.layer.close(index);
                    parent.$('#my-breadcrumb').breadcrumb().pop(0);
                    //layer.msg(JSON.stringify(jsonData));
                }
            });
        }
    };

    /**
     * [initTableEdit 编辑表格，最主要的表格之一]
     * @param  {[type]} data [description]
     * @return {[type]}      [description]
     */
    function initTableEdit(data) {
        $('#dataTables').DataTable({
            destroy: true,
            data: data,
            "bPaginate": false,
            "bLengthChange": false,
            "bFilter": false,
            "bSort": false,
            "bInfo": false,
            "bProcessing": false,
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
                "data": "host"
            }, {
                "data": "file"
            }, {
                "data": ""
            }],
            "columnDefs": [{
                "render": function(data, type, row) {
                    return createSelect(null, data, false);
                },
                "createdCell": function(td, cellData, rowData, row, col) {
                    $(td).find('select').attr('indexvalueIp', row);
                    $(td).find('select').addClass("indexSelectIp");
                },
                targets: 0
            }, {
                "render": function(data, type, row) {
                    return '<input style="width:100%;" type="text" value="' + data + '"/>';
                },
                "createdCell": function(td, cellData, rowData, row, col) {
                    $(td).find('input').attr('indexvalue', row);
                    $(td).find('input').addClass("indexSelect");
                },
                targets: 1
            }, {
                "render": function(data, type, row) {
                    var file = row['file'];
                    return '<a href="javascript:void(0)" style="padding-left:10px;" class="delRow"><i class="fa fa-minus-circle fa-lg"/></a>';
                },
                targets: 2
            }],
        });
    }

    /**
     * [initTableFinal 最后的展示表格]
     * @param  {[type]} data [description]
     * @return {[type]}      [description]
     */
    function initTableFinal(data) {
        $('#dataTablesFinal').DataTable({
            destroy: true,
            data: data,
            "bPaginate": false,
            "bLengthChange": false,
            "bFilter": false,
            "bSort": false,
            "bInfo": false,
            "bProcessing": false,
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
                "data": "host"
            }, {
                "data": "file"
            }],
            "columnDefs": [{
                "render": function(data, type, row) {
                    return createSelect(null, data, true);
                },
                targets: 0
            }, {
                "render": function(data, type, row) {
                    return '<input style="width:100%;" readonly="readonly" type="text" value="' + data + '"/>';
                },
                targets: 1
            }]
        });
    }

    /**
     * [infosHandle 处理infos数据]
     * @param  {[type]} infos [description]
     * @return {[type]}       [description]
     */
    function infosHandle() {
        $.each(jsonData['syncfile']['infos'], function(index, val) {
            var tableItemData = {};
            tableItemData['host'] = val['host'];
            tableItemData['file'] = val['file'];
            tableItemData['modeltype'] = 'file';
            tableData.push(tableItemData);
        });
        $.each(jsonData['synczookeeper']['infos'], function(index, val) {
            var tableItemData = {};
            tableItemData['host'] = val['name'];
            tableItemData['file'] = val['zkpath'];
            tableItemData['modeltype'] = 'zk';
            tableData.push(tableItemData);
        });
        //console.log(tableData);
    }

    function convJsonData() {
        syncfiles = new Array();
        synczookeepers = new Array();
        $.each(tableData, function(index, val) {
            if (val['modeltype'] == 'file') {
                delete val['modeltype'];
                syncfiles.push(val);
            } else if (val['modeltype'] == 'zk') {
                delete val['modeltype'];
                var synczookeeper = {};
                synczookeeper['name'] = val['host'];
                synczookeeper['zkpath'] = val['file'];
                synczookeepers.push(synczookeeper);
            }
        });
        jsonData['syncfile']['infos'] = syncfiles;
        jsonData['synczookeeper']['infos'] = synczookeepers;
    }

    /**
     * [createSelect 生成select]
     * @param  {[type]} options  [description]
     * @param  {[type]} select   [description]
     * @param  {[type]} disabled [description]
     * @return {[type]}          [description]
     */
    function createSelect(options, select, disabled) {
        // 创建select
        var selectTemp = "";
        if (disabled) {
            selectTemp += "<select disabled='disabled'>";
        } else {
            selectTemp = "<select>";
        }
        // 添加选项
        for (var i = serverUrlInfos.length - 1; i >= 0; i--) {
            var url = serverUrlInfos[i];
            serverUrlInfo = url.split(':');
            if (select == serverUrlInfo[1]) {
                selectTemp += "<option selected='selected' modeltype = '" + serverUrlInfo[0] + "' value='" + i + "'>" + serverUrlInfo[1] + "</option>";
            } else {
                selectTemp += "<option modeltype = '" + serverUrlInfo[0] + "' value='" + i + "'>" + serverUrlInfo[1] + "</option>";
            }

        }
        selectTemp += "</select>";
        return selectTemp;
    }

    fileIframe.init();
})(jQuery);

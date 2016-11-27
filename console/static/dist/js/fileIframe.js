/**
 * fileIframe file manage for console
 * 
 * Created by liukai on 2016/11/18.
 */

(function($) {
    var jsonData = {
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
            //other

        },
        /**
         * layout
         */
        layout: function() {
            initTableEdit(jsonData['syncfile']['infos']);

        },
        /**
         * base event
         */
        domEvent: function() {
            /**
             * [添加行]
             * @param  {[type]} ){                         } [description]
             * @return {[type]}     [description]
             */
            $(document).on('click', '#addRow', function() {
                jsonData['syncfile']['infos'].push({
                    'host': '192.168.250.179',
                    'file': '/home/testhello1'
                });

                console.log(jsonData);

                initTableEdit(jsonData['syncfile']['infos']);
            });

            // 初始化刪除按钮
            $(document).on('click', '.delRow', function() {
                var index = $(this).parents('tr').find('.indexSelect').attr('indexvalue');
                jsonData['syncfile']['infos'].splice(index,1);
                initTableEdit(jsonData['syncfile']['infos']);
            });

            /**
             * [form 表单]
             * @type {[type]}
             */
            var form = $("#file-form");
            form.validate({
                errorPlacement: function errorPlacement(error, element) {
                    element.before(error);
                },
                rules: {
                    confirm: {
                        equalTo: "#password"
                    }
                }
            });
            form.children("div").steps({
                headerTag: "h3",
                bodyTag: "section",
                transitionEffect: "slideLeft",
                labels: {
                    next: "下一步",
                    previous: "上一步",
                    finish: "完成"
                },
                onStepChanging: function(event, currentIndex, newIndex) {
                    form.validate().settings.ignore = ":disabled,:hidden";
                    return form.valid();
                },
                onFinishing: function(event, currentIndex) {
                    form.validate().settings.ignore = ":disabled";
                    return form.valid();
                },
                onFinished: function(event, currentIndex) {
                    alert("Submitted!");
                }
            });
        }
    };

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
                    return createSelect(null, data);
                },
                targets: 0
            }, {
                "render": function(data, type, row) {
                    return '<input style="width:100%;" type="text" value="' + data + '"/>';
                },
                "createdCell": function(td, cellData, rowData, row, col) {
                    $(td).attr('indexvalue', row);
                    $(td).addClass("indexSelect");
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

    function createSelect(options, select) {
        // 创建select
        var selectTemp = "<select>";
        // 添加选项
        selectTemp += "<option value='" + "192.168.250.178" + "'>192.168.250.178</option>";
        selectTemp += "<option value='" + "192.168.250.278" + "'>192.168.250.278</option>";
        selectTemp += "</select>"
        return selectTemp;
    }

    fileIframe.init();
})(jQuery);
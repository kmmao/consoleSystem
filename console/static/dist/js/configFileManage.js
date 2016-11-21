/**
 * config file manage for console
 * 
 * Created by liukai on 2016/11/18.
 */

(function($) {

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
            var path = $("#envSelect").val();
            $('#my-breadcrumb').find("li").remove();
            var breadcrumb = $('#my-breadcrumb').breadcrumb();
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
                $('#my-breadcrumb').find("li").remove();
                var breadcrumb = $('#my-breadcrumb').breadcrumb();
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
                // var $tr = $(this).parents('tr');
                // $tr.toggleClass('selected');
                // var $tmp = $('[name=checkList]:checkbox');
                // $('#checkAll').prop('checked', $tmp.length == $tmp.filter(':checked').length);
            });

            /**
             * [文件夹点击]
             * @param  {[type]} ){                         } [description]
             * @return {[type]}     [description]
             */
            $("#dataTables-configFileManage").on('click', '.dirClick', function() {
                var path = $(this).attr("data");
                var breadcrumb = $('#my-breadcrumb').breadcrumb();
                breadcrumb.push(path.split("/").pop());
            });
            /**
             * [文件夹添加]
             * @param  {[type]} ){} [description]
             * @return {[type]}       [description]
             */
            $("#addDir").click(function() {
                // var $tmp = $('[name=checkList]:checkbox');
                // if($tmp.filter(':checked').length==0){
                //     $.scojs_message('未选择', $.scojs_message.TYPE_ERROR);
                // }else{

                // }
                layer.open({
                    type: 1,
                    title: '新增文件夹', //不显示标题
                    area:['auto','auto'],
                    btn:['保存','取消'],
                    shadeClose: false,
                    content: $("#dir-dialog"), //捕获的元素
                    yes:function(){
                        //进行新增操作
                        $.post()
                    },
                    cancel:function() {
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
                "url": "/dir/scan/",
                "dataSrc": "infos",
                "type": "POST",
                "data": {
                    dirPath: path
                }
            },
            //"sAjaxDataProp": "data.infos"，
            "language": {
                "lengthMenu": "每页 _MENU_ 条记录",
                "zeroRecords": "没有找到记录",
                "info": "第 _PAGE_ 页 ( 总共 _PAGES_ 页 )",
                "infoEmpty": "无记录",
                "infoFiltered": "(从 _MAX_ 条记录过滤)",
                "loadingRecords": "加载中...",
                "search": "过滤目录及文件:",
                "sEmptyTable": "未有相关数据",
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
                    return '<input type="checkbox" name="checkList">';
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
                        return '<p><i class="file"></i>&nbsp&nbsp' + data + '</p>';
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
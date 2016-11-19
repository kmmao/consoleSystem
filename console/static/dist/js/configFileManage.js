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
            var jsonData = [
                [
                    "",
                    "ERP"
                ],
                [
                    "",
                    "AB"
                ],
            ];

            $(document).ready(function() {
                $('#dataTables-configFileManage').DataTable({
                    responsive: true,
                    //'ajax':jsonData.json
                    data: jsonData,
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
                    "columnDefs": [{
                        "render": function(data, type, row) {
                            return '<input type="checkbox" name="checkList">';
                        },
                        orderable: false,
                        targets: 0
                    }], //第一列禁止排序
                    "order": [
                        [0, null]
                    ], //第一列排序图标改为默认
                });

                $("div.toolbar").html('<b style="color:red">自定义文字、图片等等</b>');
            });
        },
        /**
         * base event
         */
        domEvent: function() {
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
                var $tr = $(this).parents('tr');
                $tr.toggleClass('selected');
                var $tmp = $('[name=checkList]:checkbox');
                $('#checkAll').prop('checked', $tmp.length == $tmp.filter(':checked').length);
            });
        }
    };
    configFileManage.init();
})(jQuery);
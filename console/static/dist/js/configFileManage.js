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

            // $.post('/dirScan',{
            //     dirPath:'/'
            // },function(res){
            //     initTable(res);
            // });

            // var jsonData = {
            //     "dir":"/",
            //     "data":[
            //         {
            //             "name":"erp",
            //             "isdir":true
            //         },
            //         {
            //             "name":"AB",
            //             "isdir":false
            //         }
            //     ]
            // };
            // $(document).ready(function() {
                
            // });

            // var jsonData = {"dir":"/","infos":[{"name":"allen","isdir":true},{"name":"erp","isdir":true},{"name":"kaokao","isdir":false},{"name":"qa","isdir":true}]};

            var breadcrumb = $('#my-breadcrumb').breadcrumb();
            breadcrumb.push('/');
            breadcrumb.push('Level');
            breadcrumb.push('Level1');
            breadcrumb.push('Level2');
            breadcrumb.push('Level3');
            //breadcrumb.pop();

            $('#my-breadcrumb').on('change', function (el, path) {
                console.log(path);
            });

            initTable();

            function initTable(){
                $('#dataTables-configFileManage').DataTable({
                    responsive: true,
                    "ServerSide":true, 
                    //data: jsonData["infos"],
                    //post request
                    "processing": true,
                    "ajax": {
                        "url":"/dirScan",
                        "dataSrc":"infos",
                        "type":"POST",
                        "data":{dirPath:"/"}
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
                    "columns": [
                        { "data": "" },
                        { "data": "name" }
                    ],
                    "columnDefs": [{
                        "render": function(data, type, row) {
                            return '<input type="checkbox" name="checkList">';
                        },
                        orderable: false,
                        targets: 0
                    },{
                        "render": function(data, type, row) {
                            //console.log(row["isdir"])
                            if(row["isdir"]==true){
                                return '<p><i class="dir"></i>&nbsp&nbsp'+data+'</p>';
                            }else{
                                return '<p><i class="file"></i>&nbsp&nbsp'+data+'</p>';
                            }
                            
                        },
                        targets: 1
                    }], //第一列禁止排序
                    "order": [
                        [0, null]
                    ], //第一列排序图标改为默认
                });
            }
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
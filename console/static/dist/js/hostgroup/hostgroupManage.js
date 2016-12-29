/**
 * hostgropu manage for console
 *
 * Created by liukai on 2016/12/26.
 */

(function($) {
    /**
     * [hostgroupManage 主体内容]
     * @type {Object}
     */
    var hostgropuManage = {
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
            $("#side-menu li").removeClass("active");
            $("#hostgroupManage_li").addClass('active');
            $('#hostgroupManage_a').addClass('active');
            //initTable();
        },
        /**
         * base event
         */
        domEvent: function() {
            /**
             * [添加分组]
             * @param  {[type]} ) {                                       } [description]
             * @return {[type]}   [description]
             */
            $("#addHost").click(function() {
                window.location.href = '/console/hostEdit';
            });

            /**
             * [编辑]
             * @param  {[type]} event)        {                           event.preventDefault();                                         clearContent();                                             var loadView [description]
             * @param  {[type]} function(res) {                                                      $('#fileId').val(res.id);                                   $("#fileName").val(res.name);                                            $("#fileContent").val(res.content);                    layer.close(loadView);                                        layer.open({                        title: '编辑模板文件',                        type: 1,                        area: ['1200px', '760px'],                        skin: 'layui-layer-rim',                         fixed: false,                         maxmin: true,                        content: $("#file-div"),                        btn: ['保存', '取消'],                        yes: function( [description]
             * @return {[type]}               [description]
             */
            $(document).on('click', '.edit', function(event) {
                event.preventDefault();
                layer.msg($(this).attr('data-ip'));
            });
        }
    };
    hostgropuManage.init();


    /**
     * [initTable 动态初始化列表]
     * @return {[type]}      [description]
     */
    function initTable() {
        $('#dataTables-hostList').DataTable({
            destroy: true,
            "dom": 'rtp',
            "ServerSide": true,
            "processing": true,
            "ajax": {
                "url": "/console/host/manage/",
                "type": "POST",
                "dataSrc": function(json) {
                    return json;
                }
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
            "columns": [
                { "title": "主机名称", "class": "hostName", "data": "host_name" },
                { "title": "外网IP", "class": "ip", "data": "out_ip" },
                { "title": "内网IP", "class": "ip", "data": "inner_ip" },
                { "title": "CPU型号", "class": "CPUModel", "data": "hwinfo_cpu_model" },
                { "title": "内存大小", "class": "memorySize", "data": "hwinfo_memory" },
                { "title": "操作系统版本", "class": "edition", "data": "sysinfo_publish_versions" },
                { "title": "运维负责人", "class": "person", "data": "leader" },
                { "title": "机器类型", "class": "type", "data": "device_type" },
            ],
            "columnDefs": [{
                    "render": function(data, type, row) {
                        return '<a href="javascript:void(0)" class="blue edit" data-ip="' + row['out_ip'] + '">' + data + '</a>';
                    },
                    targets: 0,
                }]
                // "columnDefs": [{
                //     "render": function(data, type, row) {
                //         return '<button type="button" class="btn btn-link edit" data-id="' + data + '">编辑</button>  <button type="button" class="btn btn-link delete" data-id="' + data + '">删除</button>';
                //     },
                //     orderable: false,
                //     searchable: false,
                //     targets: 2,
                //     width: '120px'
                // }, {
                //     targets: 1,
                //     width: '150px'
                // }]
        });
    }
})(jQuery);

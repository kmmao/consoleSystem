/**
 * host edit for console
 *
 * Created by liukai on 2016/12/26.
 */

(function($) {
    /**
     * [templatesManage 主体内容]
     * @type {Object}
     */
    var hostEdit = {
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
            //位置定位
            $("#side-menu li").removeClass("active");
            $("#hostManage_li").addClass('active');
            $('#hostManage_a').addClass('active');
        },
        /**
         * base event
         */
        domEvent: function() {
            var $activate_selectator2 = $('#activate_selectator');
            $activate_selectator2.click(function() {
                $('#selectID').selectator({
                    showAllOptionsOnFocus: true,
                    keepOpen: true
                });
            });
            $activate_selectator2.trigger('click');

            /**
             * [保存]
             * @param  {[type]} event) {                                       } [description]
             * @return {[type]}        [description]
             */
            $('#save').click(function(event) {
                var layerLoad = layer.load(1, {
                    shade: [0.1, '#fff'] //0.1透明度的白色背景
                });
                var jsonData = $("#hostForm").serializeObject();
                console.log(jsonData);
                // $.post('/console/host/file', { param1: 'value1' }, function(data, textStatus, xhr) {
                //     layer.close(layerLoad);
                // });
            });

            /**
             * 取消
             * @param  {[type]} event) {                                       } [description]
             * @return {[type]}        [description]
             */
            $('#cancel').click(function(event) {
                window.location.href = '/console/hostManage';
            });
        }
    };
    hostEdit.init();
})(jQuery);

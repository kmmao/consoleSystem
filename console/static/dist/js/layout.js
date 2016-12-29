
(function($) {
    var page = {
        init : function(){    
            this.sideBar_crt_event();             //左侧菜单切换   
            this.autoComplete_search_event();     //左侧菜单自动搜索功能          
            this.content_height_event();          //调整左侧菜单栏与右侧内容的高度  
            this.dialog_maxHeight_event();        //弹窗最大高度
        },

        //左侧菜单切换 
        sideBar_crt_event : function(){
            $('dl').each(function(index){
                $(this).click(function(){
                    $('dl').removeClass("active");
                    $('dl').eq(index).addClass("active");
                })
            }); 

            $('dl dd').each(function(index){
                $(this).click(function(){
                    $('dl dd').removeClass("crt");
                    $('dl dd').eq(index).addClass("crt");
                })
            }); 
        },

        //左侧菜单自动搜索功能     
        autoComplete_search_event : function(){
            $("#searchBtn").click(function(){

                var iptValue=$("#tags").val();

                $("#sideBar dl").removeClass("active");

                $("#sideBar dl dd").find("a").each(function(i){
                    if($(this).html()==iptValue){
                        $(this).parent().addClass("crt");
                        $(this).parent().parent().addClass("active");
                    }else{
                        $(this).parent().removeClass("crt");
                    }

                });        
                
            });
        },

        //调整左侧菜单栏与右侧内容的高度
        content_height_event : function(){
            var leftNav_height = $(document).height() - $('.header').height() - $('.footer').height() - 24;
            var contentWrap_height = leftNav_height - $('.crumb-wrap').outerHeight(true) + 5;
            var rightCnt_height = $('.right-cnt').height();
            if(rightCnt_height < leftNav_height){
                $('.left-nav').css({'min-height':leftNav_height});
                $('.content-wrap').css({'min-height':contentWrap_height});
            }else{
                $('.left-nav').css({'min-height':rightCnt_height-10});
            }
        },

        //弹窗最大高度
        dialog_maxHeight_event : function(){
            if($(".dialog-content").length > 0){
                var docHeight = $(window).height();
                var maxHeight = docHeight-50;       //50：留一点空隙，防止小屏幕下撑出屏幕；
                $(".dialog-content").css("max-height",maxHeight);
            }
        }
    }
    page.init();

})(jQuery);


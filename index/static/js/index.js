// 扩展jQuery对象的方法
!function () {
    !function () {
        "use strict";
        let index = $('#sidebar>ul>li')
        index.click(function () {
            index.removeClass('active')
            $(this).addClass('active');
        })
    }()
    !function () {
    // index 选择
        let li = $('li[name][class="nav-item"]')
        li.click(function () {
            let src = $(this).attr('name')
            let iframe = `<iframe class="embed" src="/${src}/" style="width: 100%;height: 100%"></iframe>`
            $('#main-box').html(iframe)
        })

    }()
}()

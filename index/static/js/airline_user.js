var add_checkbox_html = `<td class="text-center">
                            <input class="form-check-input" type="checkbox" value=""
                                   style="width:13px;vertical-align:text-top; margin-top:0;margin-left: -7px"
                                    name="data-check"
                            >
                        </td>`

!function () {
    // add_checkbox
    let tr = $('#data-table > thead > tr:gt(0)')
    let add_html = `<td class="text-center">
                                <input class="form-check-input" type="checkbox" value=""
                                       style="width:13px;vertical-align:text-top; margin-top:0;margin-left: -7px"
                                        name="data-check"
                                >
                            </td>`
    tr.append(add_html)
}()

let check_state_ls = function () {
    // check_state 选框装态
    let check_ls = $('#data-table > thead > tr > td > input')
    let check_state_ls = [];
    for (let i = 0; i < check_ls.length; i++) {
        check_state_ls.push($(check_ls[i]).prop('checked'));
    }
    return check_state_ls
}


!function () {
    // 全选反选
    $('button[name="invert"]').click(function () {
        let check_ls = $('#data-table > thead > tr > td > input')
        for (let i = 0; i < check_ls.length; i++) {
            if ($(check_ls[i]).prop('checked')) {
                $(check_ls[i]).prop('checked', false)
            } else {
                $(check_ls[i]).prop('checked', true)
            }
        }
    })
    $('button[name="uncheck"]').click(function () {
        let check_ls = $('#data-table > thead > tr > td > input')
        check_ls.prop('checked', false)
    })
}()

!function () {
    // query
    $('button[name="query"]').click(function () {
        let query_input = $('#query-form > div > div> input')
        let data = 'mode=query', key_ls = ['name', 'source', 'state', 'admin'];
        for (let i = 0; i < query_input.length; i++) {
            let form_q = $(query_input[i]).val();
            data += `&${key_ls[i]}=${form_q}`;
        }
        $.post(
            '/airline_user/',
            data, function (data) {
                let result_data = data['data']
                $('#data-table > thead > tr').not(":first").remove()
                let thead = $('#data-table > thead')
                for (let i = 0; i < result_data.length; i++) {
                    let html = '<tr>'
                    for (let j = 0; j < result_data[i].length; j++) {
                        if (j === 3 || j === 4) {
                            result_data[i][j] = result_data[i][j].replace('T', ' ').replace('Z', ' ').slice(0, 19)
                        }
                        html += `<td class="text-center">${result_data[i][j]}</td>`
                    }
                    html += add_checkbox_html
                    html += '</tr>'
                    thead.append(html)
                }
            })
    })
}()

!function () {
    // add
    $('button[name="add-submit"]').click(function () {
        let add_input = $('#add-form > div > div> input').serialize()
        let data = 'mode=add&' + add_input
        $.post('/airline_user/', data, function (data) {
            toastr.success(data['data']);
        })
    })
}()

!function () {
    // delete
    $('button[name="delete"]').click(function () {
        let check_ls = check_state_ls()
        let data = 'mode=delete'
        for (let i = 0; i < check_ls.length; i++) {
            if (check_ls[i]) {
                let user = $(`#data-table > thead > tr:nth-child(${i + 2}) > td:nth-child(2)`).html()
                let password = $(`#data-table > thead > tr:nth-child(${i + 2}) > td:nth-child(3)`).html()
                let source = $(`#data-table > thead > tr:nth-child(${i + 2}) > td:nth-child(9)`).html()
                data += `&${i}=` + user + '--' + password + '--' + source
            }
        }
        if (data !== 'mode=delete' && confirm('确认删除吗？')) {
            $.post('/airline_user/', data, function (data) {
                toastr.warning(data['data'])
                for (let i = 0; i < check_ls.length; i++) {
                    if (check_ls[i]) {
                        $(`#data-table > thead > tr:nth-child(${i+2})`).remove()
                    }
                }
            })
        } else {
            toastr.info('请选择一条数据')
        }
    })
}()

!function () {
    // alter
    $(".dropdown-item").click(function () {
        console.log(this)
        let key = ''
        switch (this.innerHTML) {
            case '正在使用':
                key = 'open'
                break
            case '停止使用':
                key = 'close'
                break
            default:
                break
        }
        let check_ls = check_state_ls()
        let data = 'mode=alter&key=' + key
        for (let i = 0; i < check_ls.length; i++) {
            if (check_ls[i]) {
                let user = $(`#data-table > thead > tr:nth-child(${i + 2}) > td:nth-child(2)`).html()
                let password = $(`#data-table > thead > tr:nth-child(${i + 2}) > td:nth-child(3)`).html()
                let source = $(`#data-table > thead > tr:nth-child(${i + 2}) > td:nth-child(9)`).html()
                data += `&${i}=` + user + '--' + password + '--' + source
            }
        }
        if (data !== 'mode=alter&key=' + key) {
            $.post('/airline_user/', data, function (data) {
                toastr.success(data['data'])
            })

            for (let i = 0; i < check_ls.length; i++) {
                if (check_ls[i]) {
                    $(`#data-table > thead > tr:nth-child(${i + 2}) > td:nth-child(6)`).html(this.innerHTML)
                }
            }
        } else {
            toastr.info('请选择一条数据')
        }


    })
}()
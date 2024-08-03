$(document).ready(function () {

    $('.btn1').click(function () {
        
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                if ($('.btn1')['0'].className == 'btn btn-lg btn-outline-success btn1 w-100') {
                    $('.btn1')['0'].className = 'btn btn-lg btn-success btn1 w-100'
                    $('.btn1')['0'].innerHTML = "<h2>Выполнено</h2>"
                }

                else {
                    $('.btn1')['0'].className = 'btn btn-lg btn-outline-success btn1 w-100'
                    $('.btn1')['0'].innerHTML = "<h2>Выполнить</h2>"
                }

                if (($('.btn1')['0'] == undefined || $('.btn1')['0'].className == 'btn btn-lg btn-success btn1 w-100') &&
                    ($('.btn2')['0'] == undefined || $('.btn2')['0'].className == 'btn btn-lg btn-success btn2 w-100') &&
                    ($('.btn3')['0'] == undefined || $('.btn3')['0'].className == 'btn btn-lg btn-success btn3 w-100') &&
                    ($('.btn4')['0'] == undefined || $('.btn4')['0'].className == 'btn btn-lg btn-success btn4 w-100') &&
                    ($('.btn5')['0'] == undefined || $('.btn5')['0'].className == 'btn btn-lg btn-success btn4 w-100')) {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            }
        })

    })

    $('.btn2').click(function () {
        
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                if ($('.btn2')['0'].className == 'btn btn-lg btn-outline-success btn2 w-100') {
                    $('.btn2')['0'].className = 'btn btn-lg btn-success btn2 w-100'
                    $('.btn2')['0'].innerHTML = "<h2>Выполнено</h2>"
                }

                else {
                    $('.btn2')['0'].className = 'btn btn-lg btn-outline-success btn2 w-100'
                    $('.btn2')['0'].innerHTML = "<h2>Выполнить</h2>"
                }

                if (($('.btn1')['0'] == undefined || $('.btn1')['0'].className == 'btn btn-lg btn-success btn1 w-100') &&
                    ($('.btn2')['0'] == undefined || $('.btn2')['0'].className == 'btn btn-lg btn-success btn2 w-100') &&
                    ($('.btn3')['0'] == undefined || $('.btn3')['0'].className == 'btn btn-lg btn-success btn3 w-100') &&
                    ($('.btn4')['0'] == undefined || $('.btn4')['0'].className == 'btn btn-lg btn-success btn4 w-100') &&
                    ($('.btn5')['0'] == undefined || $('.btn5')['0'].className == 'btn btn-lg btn-success btn4 w-100')) {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            }
        })

    })

    $('.btn3').click(function () {
        
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '3'
            },
            success: function (response) {

                if ($('.btn3')['0'].className == 'btn btn-lg btn-outline-success btn3 w-100') {
                    $('.btn3')['0'].className = 'btn btn-lg btn-success btn3 w-100'
                    $('.btn3')['0'].innerHTML = "<h2>Выполнено</h2>"
                }

                else {
                    $('.btn3')['0'].className = 'btn btn-lg btn-outline-success btn3 w-100'
                    $('.btn3')['0'].innerHTML = "<h2>Выполнить</h2>"
                }

                if (($('.btn1')['0'] == undefined || $('.btn1')['0'].className == 'btn btn-lg btn-success btn1 w-100') &&
                    ($('.btn2')['0'] == undefined || $('.btn2')['0'].className == 'btn btn-lg btn-success btn2 w-100') &&
                    ($('.btn3')['0'] == undefined || $('.btn3')['0'].className == 'btn btn-lg btn-success btn3 w-100') &&
                    ($('.btn4')['0'] == undefined || $('.btn4')['0'].className == 'btn btn-lg btn-success btn4 w-100') &&
                    ($('.btn5')['0'] == undefined || $('.btn5')['0'].className == 'btn btn-lg btn-success btn4 w-100')) {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            }
        })

    })

    $('.btn4').click(function () {
        
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '4'
            },
            success: function (response) {

                if ($('.btn4')['0'].className == 'btn btn-lg btn-outline-success btn4 w-100') {
                    $('.btn4')['0'].className = 'btn btn-lg btn-success btn4 w-100'
                    $('.btn4')['0'].innerHTML = "<h2>Выполнено</h2>"
                }

                else {
                    $('.btn4')['0'].className = 'btn btn-lg btn-outline-success btn4 w-100'
                    $('.btn4')['0'].innerHTML = "<h2>Выполнить</h2>"
                }

                if (($('.btn1')['0'] == undefined || $('.btn1')['0'].className == 'btn btn-lg btn-success btn1 w-100') &&
                    ($('.btn2')['0'] == undefined || $('.btn2')['0'].className == 'btn btn-lg btn-success btn2 w-100') &&
                    ($('.btn3')['0'] == undefined || $('.btn3')['0'].className == 'btn btn-lg btn-success btn3 w-100') &&
                    ($('.btn4')['0'] == undefined || $('.btn4')['0'].className == 'btn btn-lg btn-success btn4 w-100') &&
                    ($('.btn5')['0'] == undefined || $('.btn5')['0'].className == 'btn btn-lg btn-success btn4 w-100')) {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            }
        })

    })
})
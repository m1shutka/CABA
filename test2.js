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

                $('.btn1')['0'].className = 'btn btn-lg btn-success btn1 w-100'
                if ($('.btn2')['0'] != undefined)
                    $('.btn2')['0'].className = 'btn btn-lg btn-outline-success btn2 w-100'
                if ($('.btn3')['0'] != undefined)
                    $('.btn3')['0'].className = 'btn btn-lg btn-outline-success btn3 w-100'
                if ($('.btn4')['0'] != undefined)
                    $('.btn4')['0'].className = 'btn btn-lg btn-outline-success btn4 w-100'
                if ($('.btn5')['0'] != undefined)
                    $('.btn5')['0'].className = 'btn btn-lg btn-outline-success btn5 w-100'
                if ($('.btn6')['0'] != undefined)
                    $('.btn6')['0'].className = 'btn btn-lg btn-outline-success btn6 w-100'
                if ($('.btn7')['0'] != undefined)
                    $('.btn7')['0'].className = 'btn btn-lg btn-outline-success btn7 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
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

                $('.btn2')['0'].className = 'btn btn-lg btn-success btn2 w-100'
                if ($('.btn1')['0'] != undefined)
                    $('.btn1')['0'].className = 'btn btn-lg btn-outline-success btn1 w-100'
                if ($('.btn3')['0'] != undefined)
                    $('.btn3')['0'].className = 'btn btn-lg btn-outline-success btn3 w-100'
                if ($('.btn4')['0'] != undefined)
                    $('.btn4')['0'].className = 'btn btn-lg btn-outline-success btn4 w-100'
                if ($('.btn5')['0'] != undefined)
                    $('.btn5')['0'].className = 'btn btn-lg btn-outline-success btn5 w-100'
                if ($('.btn6')['0'] != undefined)
                    $('.btn6')['0'].className = 'btn btn-lg btn-outline-success btn6 w-100'
                if ($('.btn7')['0'] != undefined)
                    $('.btn7')['0'].className = 'btn btn-lg btn-outline-success btn7 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
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

                $('.btn3')['0'].className = 'btn btn-lg btn-success btn3 w-100'
                if ($('.btn1')['0'] != undefined)
                    $('.btn1')['0'].className = 'btn btn-lg btn-outline-success btn1 w-100'
                if ($('.btn2')['0'] != undefined)
                    $('.btn2')['0'].className = 'btn btn-lg btn-outline-success btn2 w-100'
                if ($('.btn4')['0'] != undefined)
                    $('.btn4')['0'].className = 'btn btn-lg btn-outline-success btn4 w-100'
                if ($('.btn5')['0'] != undefined)
                    $('.btn5')['0'].className = 'btn btn-lg btn-outline-success btn5 w-100'
                if ($('.btn6')['0'] != undefined)
                    $('.btn6')['0'].className = 'btn btn-lg btn-outline-success btn6 w-100'
                if ($('.btn7')['0'] != undefined)
                    $('.btn7')['0'].className = 'btn btn-lg btn-outline-success btn7 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
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

                $('.btn4')['0'].className = 'btn btn-lg btn-success btn4 w-100'
                if ($('.btn1')['0'] != undefined)
                    $('.btn1')['0'].className = 'btn btn-lg btn-outline-success btn1 w-100'
                if ($('.btn2')['0'] != undefined)
                    $('.btn2')['0'].className = 'btn btn-lg btn-outline-success btn2 w-100'
                if ($('.btn3')['0'] != undefined)
                    $('.btn3')['0'].className = 'btn btn-lg btn-outline-success btn3 w-100'
                if ($('.btn5')['0'] != undefined)
                    $('.btn5')['0'].className = 'btn btn-lg btn-outline-success btn5 w-100'
                if ($('.btn6')['0'] != undefined)
                    $('.btn6')['0'].className = 'btn btn-lg btn-outline-success btn6 w-100'
                if ($('.btn7')['0'] != undefined)
                    $('.btn7')['0'].className = 'btn btn-lg btn-outline-success btn7 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn5').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '5'
            },
            success: function (response) {

                $('.btn5')['0'].className = 'btn btn-lg btn-success btn5 w-100'
                if ($('.btn1')['0'] != undefined)
                    $('.btn1')['0'].className = 'btn btn-lg btn-outline-success btn1 w-100'
                if ($('.btn2')['0'] != undefined)
                    $('.btn2')['0'].className = 'btn btn-lg btn-outline-success btn2 w-100'
                if ($('.btn3')['0'] != undefined)
                    $('.btn3')['0'].className = 'btn btn-lg btn-outline-success btn3 w-100'
                if ($('.btn4')['0'] != undefined)
                    $('.btn4')['0'].className = 'btn btn-lg btn-outline-success btn4 w-100'
                if ($('.btn6')['0'] != undefined)
                    $('.btn6')['0'].className = 'btn btn-lg btn-outline-success btn6 w-100'
                if ($('.btn7')['0'] != undefined)
                    $('.btn7')['0'].className = 'btn btn-lg btn-outline-success btn7 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn6').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '6'
            },
            success: function (response) {

                $('.btn6')['0'].className = 'btn btn-lg btn-success btn6 w-100'
                if ($('.btn1')['0'] != undefined)
                    $('.btn1')['0'].className = 'btn btn-lg btn-outline-success btn1 w-100'
                if ($('.btn2')['0'] != undefined)
                    $('.btn2')['0'].className = 'btn btn-lg btn-outline-success btn2 w-100'
                if ($('.btn3')['0'] != undefined)
                    $('.btn3')['0'].className = 'btn btn-lg btn-outline-success btn3 w-100'
                if ($('.btn4')['0'] != undefined)
                    $('.btn4')['0'].className = 'btn btn-lg btn-outline-success btn4 w-100'
                if ($('.btn5')['0'] != undefined)
                    $('.btn5')['0'].className = 'btn btn-lg btn-outline-success btn5 w-100'
                if ($('.btn7')['0'] != undefined)
                    $('.btn7')['0'].className = 'btn btn-lg btn-outline-success btn7 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn7').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '7'
            },
            success: function (response) {

                $('.btn7')['0'].className = 'btn btn-lg btn-success btn7 w-100'
                if ($('.btn1')['0'] != undefined)
                    $('.btn1')['0'].className = 'btn btn-lg btn-outline-success btn1 w-100'
                if ($('.btn2')['0'] != undefined)
                    $('.btn2')['0'].className = 'btn btn-lg btn-outline-success btn2 w-100'
                if ($('.btn3')['0'] != undefined)
                    $('.btn3')['0'].className = 'btn btn-lg btn-outline-success btn3 w-100'
                if ($('.btn4')['0'] != undefined)
                    $('.btn4')['0'].className = 'btn btn-lg btn-outline-success btn4 w-100'
                if ($('.btn5')['0'] != undefined)
                    $('.btn5')['0'].className = 'btn btn-lg btn-outline-success btn5 w-100'
                if ($('.btn6')['0'] != undefined)
                    $('.btn6')['0'].className = 'btn btn-lg btn-outline-success btn6 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })
})
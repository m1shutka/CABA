$(document).ready(function () {

    $('.btn41').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {
                
                $('.btn41')['0'].className = 'btn btn-lg btn-success btn41 w-100'
                $('.btn42')['0'].className = 'btn btn-lg btn-outline-warning btn42 w-100'
                $('.btn43')['0'].className = 'btn btn-lg btn-outline-warning btn43 w-100'
                $('.btn44')['0'].className = 'btn btn-lg btn-outline-danger btn44 w-100'
                
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn42').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn41')['0'].className = 'btn btn-lg btn-outline-success btn41 w-100'
                $('.btn42')['0'].className = 'btn btn-lg btn-warning btn42 w-100'
                $('.btn43')['0'].className = 'btn btn-lg btn-outline-warning btn43 w-100'
                $('.btn44')['0'].className = 'btn btn-lg btn-outline-danger btn44 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>SOS. Обеспечение проходимости дыхательных путей</h2>"
            }
        })
    })

    $('.btn43').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '3'
            },
            success: function (response) {

                $('.btn41')['0'].className = 'btn btn-lg btn-outline-success btn41 w-100'
                $('.btn42')['0'].className = 'btn btn-lg btn-outline-warning btn42 w-100'
                $('.btn43')['0'].className = 'btn btn-lg btn-warning btn43 w-100'
                $('.btn44')['0'].className = 'btn btn-lg btn-outline-danger btn44 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>SOS. Дыхательная недостаточность</h2>"
            }
        })
    })

    $('.btn44').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '4'
            },
            success: function (response) {

                $('.btn41')['0'].className = 'btn btn-lg btn-outline-success btn41 w-100'
                $('.btn42')['0'].className = 'btn btn-lg btn-outline-warning btn42 w-100'
                $('.btn43')['0'].className = 'btn btn-lg btn-outline-warning btn43 w-100'
                $('.btn44')['0'].className = 'btn btn-lg btn-danger btn44 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-danger w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>SOS. Реанимация!!!</h2>"
            }
        })
    })

    $('.btn51').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn51')['0'].className = 'btn btn-lg btn-warning btn51 w-100'
                $('.btn52')['0'].className = 'btn btn-lg btn-outline-warning btn52 w-100'
                $('.btn53')['0'].className = 'btn btn-lg btn-outline-warning btn53 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>SOS. Отёк гортани</h2>"
            }
        })
    })

    $('.btn52').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn51')['0'].className = 'btn btn-lg btn-outline-warning btn51 w-100'
                $('.btn52')['0'].className = 'btn btn-lg btn-warning btn52 w-100'
                $('.btn53')['0'].className = 'btn btn-lg btn-outline-warning btn53 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>SOS. Бронхообструкция</h2>"
            }
        })
    })

    $('.btn53').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '3'
            },
            success: function (response) {

                $('.btn51')['0'].className = 'btn btn-lg btn-outline-warning btn51 w-100'
                $('.btn52')['0'].className = 'btn btn-lg btn-outline-warning btn52 w-100'
                $('.btn53')['0'].className = 'btn btn-lg btn-warning btn53 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>SOS. Отёк лёгких</h2>"
            }
        })
    })

    $('.btn61').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn61')['0'].className = 'btn btn-lg btn-success btn61 w-100'
                $('.btn62')['0'].className = 'btn btn-lg btn-outline-danger btn62 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn62').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn61')['0'].className = 'btn btn-lg btn-outline-success btn61 w-100'
                $('.btn62')['0'].className = 'btn btn-lg btn-danger btn62 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-danger w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>SOS. Реанимация!!!</h2>"
            }
        })
    })

    $('.btn81').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn81')['0'].className = 'btn btn-lg btn-success btn81 w-100'
                $('.btn82')['0'].className = 'btn btn-lg btn-outline-warning btn82 w-100'
                $('.btn83')['0'].className = 'btn btn-lg btn-outline-warning btn83 w-100'
                $('.btn84')['0'].className = 'btn btn-lg btn-outline-danger btn84 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn82').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn81')['0'].className = 'btn btn-lg btn-outline-success btn81 w-100'
                $('.btn82')['0'].className = 'btn btn-lg btn-warning btn82 w-100'
                $('.btn83')['0'].className = 'btn btn-lg btn-outline-warning btn83 w-100'
                $('.btn84')['0'].className = 'btn btn-lg btn-outline-danger btn84 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>SOS. Гипертонический криз</h2>"
            }
        })
    })

    $('.btn83').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '3'
            },
            success: function (response) {

                $('.btn81')['0'].className = 'btn btn-lg btn-outline-success btn81 w-100'
                $('.btn82')['0'].className = 'btn btn-lg btn-outline-warning btn82 w-100'
                $('.btn83')['0'].className = 'btn btn-lg btn-warning btn83 w-100'
                $('.btn84')['0'].className = 'btn btn-lg btn-outline-danger btn84 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>SOS. Артериальная гипотония</h2>"
            }
        })
    })

    $('.btn84').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '4'
            },
            success: function (response) {

                $('.btn81')['0'].className = 'btn btn-lg btn-outline-success btn81 w-100'
                $('.btn82')['0'].className = 'btn btn-lg btn-outline-warning btn82 w-100'
                $('.btn83')['0'].className = 'btn btn-lg btn-outline-warning btn83 w-100'
                $('.btn84')['0'].className = 'btn btn-lg btn-danger btn84 w-100'

                $('.btn-next')['0'].className = 'btn btn-lg btn-danger w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>SOS. Реанимация!!!</h2>"
            }
        })
    })

    $('.btn181').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn181')['0'].className = 'btn btn-lg btn-success btn181 w-100'
                $('.btn182')['0'].className = 'btn btn-lg btn-outline-danger btn182 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn182').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn181')['0'].className = 'btn btn-lg btn-outline-success btn181 w-100'
                $('.btn182')['0'].className = 'btn btn-lg btn-danger btn182 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn191').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn191')['0'].className = 'btn btn-lg btn-success btn191 w-100'
                $('.btn192')['0'].className = 'btn btn-lg btn-outline-danger btn192 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn192').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn191')['0'].className = 'btn btn-lg btn-outline-success btn191 w-100'
                $('.btn192')['0'].className = 'btn btn-lg btn-danger btn192 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn221').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn221')['0'].className = 'btn btn-lg btn-success btn221 w-100'
                $('.btn222')['0'].className = 'btn btn-lg btn-outline-danger btn222 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn222').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn221')['0'].className = 'btn btn-lg btn-outline-success btn221 w-100'
                $('.btn222')['0'].className = 'btn btn-lg btn-danger btn222 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn231').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn231')['0'].className = 'btn btn-lg btn-success btn231 w-100'
                $('.btn232')['0'].className = 'btn btn-lg btn-outline-danger btn232 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn232').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn231')['0'].className = 'btn btn-lg btn-outline-success btn231 w-100'
                $('.btn232')['0'].className = 'btn btn-lg btn-danger btn232 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn241').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn241')['0'].className = 'btn btn-lg btn-success btn241 w-100'
                $('.btn242')['0'].className = 'btn btn-lg btn-outline-danger btn242 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn242').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn241')['0'].className = 'btn btn-lg btn-outline-success btn241 w-100'
                $('.btn242')['0'].className = 'btn btn-lg btn-danger btn242 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn251').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn251')['0'].className = 'btn btn-lg btn-success btn251 w-100'
                $('.btn252')['0'].className = 'btn btn-lg btn-outline-danger btn252 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn252').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn251')['0'].className = 'btn btn-lg btn-outline-success btn251 w-100'
                $('.btn252')['0'].className = 'btn btn-lg btn-danger btn252 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })
})
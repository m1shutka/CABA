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

    $('.btn2321').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn2321')['0'].className = 'btn btn-lg btn-success btn2321 w-100'
                $('.btn2322')['0'].className = 'btn btn-lg btn-outline-danger btn2322 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn2322').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn2321')['0'].className = 'btn btn-lg btn-outline-success btn2321 w-100'
                $('.btn2322')['0'].className = 'btn btn-lg btn-danger btn2322 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn3321').click(function () {
        console.log('p')
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn3321')['0'].className = 'btn btn-lg btn-danger btn3321 w-100'
                $('.btn3322')['0'].className = 'btn btn-lg btn-outline-success btn3322 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-danger w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>SOS. Оценить дыхание!</h2>"
            }
        })
    })

    $('.btn3322').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn3321')['0'].className = 'btn btn-lg btn-outline-danger btn3321 w-100'
                $('.btn3322')['0'].className = 'btn btn-lg btn-success btn3322 w-100'
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

                $('.btn191')['0'].className = 'btn btn-lg btn-danger btn191 w-100'
                $('.btn192')['0'].className = 'btn btn-lg btn-outline-success btn192 w-100'
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

                $('.btn191')['0'].className = 'btn btn-lg btn-outline-danger btn191 w-100'
                $('.btn192')['0'].className = 'btn btn-lg btn-success btn192 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn2641').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn2641')['0'].className = 'btn btn-lg btn-success btn2641 w-100'
                $('.btn2642')['0'].className = 'btn btn-lg btn-outline-success btn2642 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })

    $('.btn2642').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn2641')['0'].className = 'btn btn-lg btn-outline-success btn2641 w-100'
                $('.btn2642')['0'].className = 'btn btn-lg btn-success btn2642 w-100'
                $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
            }
        })
    })
})
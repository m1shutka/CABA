$(document).ready(function () {

    $('.btn31').click(function () {
    
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {
                
                $('.btn31')['0'].className = 'btn btn-lg btn-success btn31 w-100'
                $('.btn32')['0'].className = 'btn btn-lg btn-outline-danger btn32 w-100'

                if ($('.btn31')['0'].className == 'btn btn-lg btn-success btn31 w-100' && $('.btn34')['0'].className == 'btn btn-lg btn-success btn34 w-100') { 
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn31')['0'].className == 'btn btn-lg btn-success btn31 w-100' && $('.btn33')['0'].className == 'btn btn-lg btn-danger btn33 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>SOS. Судороги</h2>"
                }
                else if ($('.btn32')['0'].className == 'btn btn-lg btn-danger btn32 w-100' && $('.btn33')['0'].className == 'btn btn-lg btn-danger btn33 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-danger w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>SOS. Оценить дыхание!</h2>"
                }
                else if ($('.btn32')['0'].className == 'btn btn-lg btn-danger btn32 w-100' && $('.btn34')['0'].className == 'btn btn-lg btn-success btn34 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-danger w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>SOS. Оценить дыхание!</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            }
        })
    })

    $('.btn32').click(function () {
   
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn32')['0'].className = 'btn btn-lg btn-danger btn32 w-100'
                $('.btn31')['0'].className = 'btn btn-lg btn-outline-success btn31 w-100'

                if ($('.btn31')['0'].className == 'btn btn-lg btn-success btn31 w-100' && $('.btn34')['0'].className == 'btn btn-lg btn-success btn34 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn31')['0'].className == 'btn btn-lg btn-success btn31 w-100' && $('.btn33')['0'].className == 'btn btn-lg btn-danger btn33 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>SOS. Судороги</h2>"
                }
                else if ($('.btn32')['0'].className == 'btn btn-lg btn-danger btn32 w-100' && $('.btn33')['0'].className == 'btn btn-lg btn-danger btn33 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-danger w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>SOS. Оценить дыхание!</h2>"
                }
                else if ($('.btn32')['0'].className == 'btn btn-lg btn-danger btn32 w-100' && $('.btn34')['0'].className == 'btn btn-lg btn-success btn34 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-danger w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>SOS. Оценить дыхание!</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            }
        })
    })

    $('.btn33').click(function () {

        console.log('.btn33')
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '3'
            },
            success: function (response) {

                $('.btn33')['0'].className = 'btn btn-lg btn-danger btn33 w-100'
                $('.btn34')['0'].className = 'btn btn-lg btn-outline-success btn34 w-100'

                if ($('.btn31')['0'].className == 'btn btn-lg btn-success btn31 w-100' && $('.btn34')['0'].className == 'btn btn-lg btn-success btn34 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn31')['0'].className == 'btn btn-lg btn-success btn31 w-100' && $('.btn33')['0'].className == 'btn btn-lg btn-danger btn33 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>SOS. Судороги</h2>"
                }
                else if ($('.btn32')['0'].className == 'btn btn-lg btn-danger btn32 w-100' && $('.btn33')['0'].className == 'btn btn-lg btn-danger btn33 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-danger w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>SOS. Оценить дыхание!</h2>"
                }
                else if ($('.btn32')['0'].className == 'btn btn-lg btn-danger btn32 w-100' && $('.btn34')['0'].className == 'btn btn-lg btn-success btn34 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-danger w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>SOS. Оценить дыхание!</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            }
        })
    })

    $('.btn34').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '4'
            },
            success: function (response) {

                $('.btn34')['0'].className = 'btn btn-lg btn-success btn34 w-100'
                $('.btn33')['0'].className = 'btn btn-lg btn-outline-danger btn33 w-100'

                if ($('.btn31')['0'].className == 'btn btn-lg btn-success btn31 w-100' && $('.btn34')['0'].className == 'btn btn-lg btn-success btn34 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn31')['0'].className == 'btn btn-lg btn-success btn31 w-100' && $('.btn33')['0'].className == 'btn btn-lg btn-danger btn33 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>SOS. Судороги</h2>"
                }
                else if ($('.btn32')['0'].className == 'btn btn-lg btn-danger btn32 w-100' && $('.btn33')['0'].className == 'btn btn-lg btn-danger btn33 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-danger w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>SOS. Оценить дыхание!</h2>"
                }
                else if ($('.btn32')['0'].className == 'btn btn-lg btn-danger btn32 w-100' && $('.btn34')['0'].className == 'btn btn-lg btn-success btn34 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-danger w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>SOS. Оценить дыхание!</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            }
        })
    })

    $('.btn111').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn111')['0'].className = 'btn btn-lg btn-danger btn111 w-100'
                $('.btn112')['0'].className = 'btn btn-lg btn-outline-success btn112 w-100'

                if ($('.btn111')['0'].className == 'btn btn-lg btn-danger btn111 w-100' && $('.btn114')['0'].className == 'btn btn-lg btn-success btn114 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn111')['0'].className == 'btn btn-lg btn-danger btn111 w-100' && $('.btn113')['0'].className == 'btn btn-lg btn-danger btn113 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn112')['0'].className == 'btn btn-lg btn-success btn112 w-100' && $('.btn113')['0'].className == 'btn btn-lg btn-danger btn113 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn112')['0'].className == 'btn btn-lg btn-success btn112 w-100' && $('.btn114')['0'].className == 'btn btn-lg btn-success btn114 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-warning w-100 btn-next disabled'
            }
        })
    })

    $('.btn112').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn112')['0'].className = 'btn btn-lg btn-success btn112 w-100'
                $('.btn111')['0'].className = 'btn btn-lg btn-outline-danger btn111 w-100'

                if ($('.btn111')['0'].className == 'btn btn-lg btn-danger btn111 w-100' && $('.btn114')['0'].className == 'btn btn-lg btn-success btn114 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn111')['0'].className == 'btn btn-lg btn-danger btn111 w-100' && $('.btn113')['0'].className == 'btn btn-lg btn-danger btn113 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn112')['0'].className == 'btn btn-lg btn-success btn112 w-100' && $('.btn113')['0'].className == 'btn btn-lg btn-danger btn113 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn112')['0'].className == 'btn btn-lg btn-success btn112 w-100' && $('.btn114')['0'].className == 'btn btn-lg btn-success btn114 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-warning w-100 btn-next disabled'
            }
        })
    })

    $('.btn113').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '3'
            },
            success: function (response) {

                $('.btn113')['0'].className = 'btn btn-lg btn-danger btn113 w-100'
                $('.btn114')['0'].className = 'btn btn-lg btn-outline-success btn114 w-100'

                if ($('.btn111')['0'].className == 'btn btn-lg btn-danger btn111 w-100' && $('.btn114')['0'].className == 'btn btn-lg btn-success btn114 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn111')['0'].className == 'btn btn-lg btn-danger btn111 w-100' && $('.btn113')['0'].className == 'btn btn-lg btn-danger btn113 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn112')['0'].className == 'btn btn-lg btn-success btn112 w-100' && $('.btn113')['0'].className == 'btn btn-lg btn-danger btn113 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn112')['0'].className == 'btn btn-lg btn-success btn112 w-100' && $('.btn114')['0'].className == 'btn btn-lg btn-success btn114 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-warning w-100 btn-next disabled'
            }
        })
    })

    $('.btn114').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '4'
            },
            success: function (response) {

                $('.btn114')['0'].className = 'btn btn-lg btn-success btn114 w-100'
                $('.btn113')['0'].className = 'btn btn-lg btn-outline-danger btn113 w-100'

                if ($('.btn111')['0'].className == 'btn btn-lg btn-danger btn111 w-100' && $('.btn114')['0'].className == 'btn btn-lg btn-success btn114 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn111')['0'].className == 'btn btn-lg btn-danger btn111 w-100' && $('.btn113')['0'].className == 'btn btn-lg btn-danger btn113 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn112')['0'].className == 'btn btn-lg btn-success btn112 w-100' && $('.btn113')['0'].className == 'btn btn-lg btn-danger btn113 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn112')['0'].className == 'btn btn-lg btn-success btn112 w-100' && $('.btn114')['0'].className == 'btn btn-lg btn-success btn114 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-warning w-100 btn-next disabled'
            }
        })
    })

    $('.btn151').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn151')['0'].className = 'btn btn-lg btn-success btn151 w-100'
                $('.btn152')['0'].className = 'btn btn-lg btn-outline-danger btn152 w-100'

                if ($('.btn151')['0'].className == 'btn btn-lg btn-success btn151 w-100' && $('.btn154')['0'].className == 'btn btn-lg btn-danger btn154 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn151')['0'].className == 'btn btn-lg btn-success btn151 w-100' && $('.btn153')['0'].className == 'btn btn-lg btn-success btn153 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn152')['0'].className == 'btn btn-lg btn-danger btn152 w-100' && $('.btn153')['0'].className == 'btn btn-lg btn-success btn153 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn152')['0'].className == 'btn btn-lg btn-danger btn152 w-100' && $('.btn154')['0'].className == 'btn btn-lg btn-danger btn154 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-warning w-100 btn-next disabled'
            }
        })
    })

    $('.btn152').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn152')['0'].className = 'btn btn-lg btn-danger btn152 w-100'
                $('.btn151')['0'].className = 'btn btn-lg btn-outline-success btn151 w-100'

                if ($('.btn151')['0'].className == 'btn btn-lg btn-success btn151 w-100' && $('.btn154')['0'].className == 'btn btn-lg btn-danger btn154 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn151')['0'].className == 'btn btn-lg btn-success btn151 w-100' && $('.btn153')['0'].className == 'btn btn-lg btn-success btn153 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn152')['0'].className == 'btn btn-lg btn-danger btn152 w-100' && $('.btn153')['0'].className == 'btn btn-lg btn-success btn153 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn152')['0'].className == 'btn btn-lg btn-danger btn152 w-100' && $('.btn154')['0'].className == 'btn btn-lg btn-danger btn154 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-warning w-100 btn-next disabled'
            }
        })
    })

    $('.btn153').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '3'
            },
            success: function (response) {

                $('.btn153')['0'].className = 'btn btn-lg btn-success btn153 w-100'
                $('.btn154')['0'].className = 'btn btn-lg btn-outline-danger btn154 w-100'

                if ($('.btn151')['0'].className == 'btn btn-lg btn-success btn151 w-100' && $('.btn154')['0'].className == 'btn btn-lg btn-danger btn154 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn151')['0'].className == 'btn btn-lg btn-success btn151 w-100' && $('.btn153')['0'].className == 'btn btn-lg btn-success btn153 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn152')['0'].className == 'btn btn-lg btn-danger btn152 w-100' && $('.btn153')['0'].className == 'btn btn-lg btn-success btn153 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn152')['0'].className == 'btn btn-lg btn-danger btn152 w-100' && $('.btn154')['0'].className == 'btn btn-lg btn-danger btn154 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-warning w-100 btn-next disabled'
            }
        })
    })

    $('.btn154').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '4'
            },
            success: function (response) {

                $('.btn154')['0'].className = 'btn btn-lg btn-danger btn154 w-100'
                $('.btn153')['0'].className = 'btn btn-lg btn-outline-success btn153 w-100'

                if ($('.btn151')['0'].className == 'btn btn-lg btn-success btn151 w-100' && $('.btn154')['0'].className == 'btn btn-lg btn-danger btn154 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn151')['0'].className == 'btn btn-lg btn-success btn151 w-100' && $('.btn153')['0'].className == 'btn btn-lg btn-success btn153 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn152')['0'].className == 'btn btn-lg btn-danger btn152 w-100' && $('.btn153')['0'].className == 'btn btn-lg btn-success btn153 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn152')['0'].className == 'btn btn-lg btn-danger btn152 w-100' && $('.btn154')['0'].className == 'btn btn-lg btn-danger btn154 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-warning w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-warning w-100 btn-next disabled'
            }
        })
    })

    $('.btn2311').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '1'
            },
            success: function (response) {

                $('.btn2311')['0'].className = 'btn btn-lg btn-danger btn2311 w-100'
                $('.btn2312')['0'].className = 'btn btn-lg btn-outline-success btn2312 w-100'

                if ($('.btn2311')['0'].className == 'btn btn-lg btn-danger btn2311 w-100' && $('.btn2314')['0'].className == 'btn btn-lg btn-success btn2314 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn2311')['0'].className == 'btn btn-lg btn-danger btn2311 w-100' && $('.btn2313')['0'].className == 'btn btn-lg btn-danger btn2313 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn2312')['0'].className == 'btn btn-lg btn-success btn2312 w-100' && $('.btn2313')['0'].className == 'btn btn-lg btn-danger btn2313 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn2312')['0'].className == 'btn btn-lg btn-success btn2312 w-100' && $('.btn2324')['0'].className == 'btn btn-lg btn-success btn2314 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-warning w-100 btn-next disabled'
            }
        })
    })

    $('.btn2312').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '2'
            },
            success: function (response) {

                $('.btn2312')['0'].className = 'btn btn-lg btn-success btn2312 w-100'
                $('.btn2311')['0'].className = 'btn btn-lg btn-outline-danger btn2311 w-100'

                if ($('.btn2311')['0'].className == 'btn btn-lg btn-danger btn2311 w-100' && $('.btn2314')['0'].className == 'btn btn-lg btn-success btn2314 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn2311')['0'].className == 'btn btn-lg btn-danger btn2311 w-100' && $('.btn2313')['0'].className == 'btn btn-lg btn-danger btn2313 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn2312')['0'].className == 'btn btn-lg btn-success btn2312 w-100' && $('.btn2313')['0'].className == 'btn btn-lg btn-danger btn2313 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn2312')['0'].className == 'btn btn-lg btn-success btn2312 w-100' && $('.btn2324')['0'].className == 'btn btn-lg btn-success btn2314 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-warning w-100 btn-next disabled'
            }
        })
    })

    $('.btn2313').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '3'
            },
            success: function (response) {

                $('.btn2313')['0'].className = 'btn btn-lg btn-danger btn2313 w-100'
                $('.btn2314')['0'].className = 'btn btn-lg btn-outline-success btn2314 w-100'

                if ($('.btn2311')['0'].className == 'btn btn-lg btn-danger btn2311 w-100' && $('.btn2314')['0'].className == 'btn btn-lg btn-success btn2314 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn2311')['0'].className == 'btn btn-lg btn-danger btn2311 w-100' && $('.btn2313')['0'].className == 'btn btn-lg btn-danger btn2313 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn2312')['0'].className == 'btn btn-lg btn-success btn2312 w-100' && $('.btn2313')['0'].className == 'btn btn-lg btn-danger btn2313 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn2312')['0'].className == 'btn btn-lg btn-success btn2312 w-100' && $('.btn2324')['0'].className == 'btn btn-lg btn-success btn2314 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-warning w-100 btn-next disabled'
            }
        })
    })

    $('.btn2314').click(function () {

        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_number: '4'
            },
            success: function (response) {

                $('.btn2314')['0'].className = 'btn btn-lg btn-success btn2314 w-100'
                $('.btn2313')['0'].className = 'btn btn-lg btn-outline-danger btn2313 w-100'

                if ($('.btn2311')['0'].className == 'btn btn-lg btn-danger btn2311 w-100' && $('.btn2314')['0'].className == 'btn btn-lg btn-success btn2314 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn2311')['0'].className == 'btn btn-lg btn-danger btn2311 w-100' && $('.btn2313')['0'].className == 'btn btn-lg btn-danger btn2313 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn2312')['0'].className == 'btn btn-lg btn-success btn2312 w-100' && $('.btn2313')['0'].className == 'btn btn-lg btn-danger btn2313 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else if ($('.btn2312')['0'].className == 'btn btn-lg btn-success btn2312 w-100' && $('.btn2324')['0'].className == 'btn btn-lg btn-success btn2314 w-100') {
                    $('.btn-next')['0'].className = 'btn btn-lg btn-success w-100 btn-next'
                    $('.btn-next')['0'].innerHTML = "<h2>Далее</h2>"
                }
                else
                    $('.btn-next')['0'].className = 'btn btn-lg btn-outline-warning w-100 btn-next disabled'
            }
        })
    })
})





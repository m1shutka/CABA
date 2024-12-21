function timer(){
    var countdown = setInterval(function() {
      
        var now = new Date().getTime();
        
        var remain = now - localStorage.getItem('start_time');
        
        var min = Math.floor( (remain % (1000 * 60 * 60)) / (1000 * 60) );
        var sec = Math.floor( (remain % (1000 * 60)) / 1000 );
        
        sec = sec < 10 ? "0" + sec : sec;
        
        //console.log(min + ":" + sec)
        document.getElementById("timer").innerHTML = min + ":" + sec;
    
        // если время вышло
        if (min > 10) {
          // останавливаем отсчёт
          clearInterval(countdown);
         }
      }, 1000);
  }
  
timer()
started = false

function start() {

  if (started) {return};
  
  var start_time = new Date().getTime();
  localStorage.setItem('start_time', start_time); 
  
  started = true;
}
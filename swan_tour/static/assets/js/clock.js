var countDownDate = new Date("feb 15, 2024 15:37:25").getTime();


var x = setInterval(function() {

  // Get today's date and time
  var presentTime = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - presentTime;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementById("day").innerHTML = days;
  document.getElementById("hrs").innerHTML = hours;
  document.getElementById("min").innerHTML = minutes;
  document.getElementById("sec").innerHTML = seconds;

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("day").innerHTML = "EXPIRED";
    document.getElementById("hrs").innerHTML = "EXPIRED";
    document.getElementById("min").innerHTML = "EXPIRED";
    document.getElementById("sec").innerHTML = "EXPIRED";
  }
}, 1000);


function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    const countdownBox = document.getElementById("countdown-box")

    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = duration;
            countdownBox.innerHTML = 'time expired'
            
            const get= document.getElementById('button');
            get.click();
        }
    }, 1000);
}

window.onload = function () {
    var Minutes = 60 * 0.30,
        display = document.querySelector('#time');
    startTimer(Minutes, display);

    
};


function clickEvent() {
    console.log("Click Event triggered")
}


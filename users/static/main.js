console.log('hello world')

//new Date().toLocaleDateString('en-us', { month:"short", day:"numeric", year:"numeric", hour:"numeric", minute:"numeric", second:"numeric"}) 
const date = new Date().toLocaleDateString('en-us', { month:"short", day:"numeric"})
const year = new Date().toLocaleDateString('en-us', { year:"numeric"})
const hour = new Date().getHours()
const minute = new Date().getMinutes() + 60
const second = new Date().getSeconds() 

const eventBox = date + ', ' + year + ' ' + hour + ':' + minute + ':' + second
const countdownBox = document.getElementById("countdown-box")

const eventDate = Date.parse(eventBox)
console.log(eventDate)

const myCountdown = setInterval(() =>{
    const now = new Date().getTime()
    console.log(now)

    const diff = eventDate - now

    const d = Math.floor(eventDate / (1000 * 60 * 60 * 24) - (now / (1000 * 60 * 60 * 24)))
    const h = Math.floor((eventDate / (1000 * 60 * 60) - (now / (1000 * 60 * 60))) % 24)
    const m = Math.floor((eventDate / (1000 * 60) + 60 - (now / (1000 * 60))) % 60)
    const s = Math.floor((eventDate / (1000) - (now / (1000))) % 60)
    console.log(s)

    if (diff>0){
        countdownBox.innerHTML = m + " m : " + s + " s "

    }else{
        
        clearInterval(myCountdown)
        countdownBox.innerHTML = 'time expired'
        
        //const get= document.getElementById('button');
        //get.click();

        }
    
}, 1000 )

function clickEvent() {
    console.log("Click Event triggered")
}

window.onbeforeunload = function() {
    return "Dude, are you sure you want to leave? Think of the kittens!";
}

//function disableF5(e) { if ((e.which || e.keyCode) == 116 || (e.which || e.keyCode) == 82) e.preventDefault(); };

//$(document).ready(function(){
  //   $(document).on("keydown", disableF5);
//});


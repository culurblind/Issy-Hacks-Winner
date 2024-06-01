/*
    home.js runs the front end code by making the buttons work and updating the balance after every game is done
*/

function handleButtonClick(url) {
    
    window.location.href = url;
}

function openForm() {
    document.getElementById("myForm").style.display = "block";
  }
  
function closeForm() {
    document.getElementById("myForm").style.display = "none";
}
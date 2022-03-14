// console.log('Hello world!');

let nameInp = document.getElementById("name_input");
let ageInp = document.getElementById("age_input");
let passwordInp = document.getElementById("password_input");
let formBtn = document.getElementById("form_btn")

function sendData(data) {
    fetch("http://localhost:8000/users", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json;charset=utf-8",
        },
    });
}

formBtn.addEventListener('click', (e) => {
    e.preventDefault()
    let userObj = {
        name: nameInp.value,
        age: ageInp.value,
        password: passwordInp.value
    }
    nameInp.value = ''
    ageInp.value = ''
    passwordInp.value = ''
    sendData(userObj)
})



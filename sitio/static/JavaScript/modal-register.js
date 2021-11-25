const formularioModal = document.getElementById("formulario");
const modalBtn = document.getElementById("changePasswordText");
const modalBg = document.querySelector(".model_bg");
const closeModal = document.querySelector(".close-modal");

let mailModal = false;

modalBtn.addEventListener("click", () => {
  modalBg.classList.add("bg_active");
  mailModal = true;
  if (mailModal == true) {
    console.log("abrido");
    rellenar();
}
});

closeModal.addEventListener("click", () => {
  modalBg.classList.remove("bg_active");
  mailModal = false;
  if (mailModal == false) {
    console.log("cerrido");
}
    borrar();
});

const rellenar = () => {
    formularioModal.email.value = "abc@gmail.com"
    formularioModal.password.value = "12345"
}

const borrar = () => {
    formularioModal.email.value = ""
    formularioModal.password.value = ""
}

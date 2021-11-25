const formularioModal = document.getElementById("formulario");
const modalBtn = document.getElementById("changePasswordText");
const modalBg = document.querySelector(".model_bg");
const closeModal = document.querySelector(".close-modal");

let mailModal = false;
let returner = false;

modalBtn.addEventListener("click", () => {
  modalBg.classList.add("bg_active");
  rellenar();
  returner = true;
});

closeModal.addEventListener("click", () => {
  modalBg.classList.remove("bg_active");
  borrar();
  returner = false;
});

const estaValidadoModal = () => returner;

const rellenar = () => {
  formularioModal.email.value = "abc@gmail.com";
  formularioModal.password.value = "12345";
};

const borrar = () => {
  formularioModal.email.value = "";
  formularioModal.password.value = "";
};

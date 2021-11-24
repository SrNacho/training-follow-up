//Aparicion del Modal

const modalBtn = document.querySelector(".model_btn");
const modalBg = document.querySelector(".model_bg");
const closeModal = document.querySelector(".close-modal");

modalBtn.addEventListener("click", () => {
  modalBg.classList.add("bg_active");
});

closeModal.addEventListener("click", () => {
  modalBg.classList.remove("bg_active");
});

//Validacion del input tiempo

const formulario = document.getElementById("formulario");
const inputs = document.querySelectorAll("#formulario input");

const expresiones = {
  tiempo: /^[1-5]{1,1}$/,
};

const campos = {
  tiempo: false,
};


let fueValidado = false;

const validarFormulario = (e) => {
  switch (e.target.name) {
    case "tiempo":
      const result = validarCampo(expresiones.tiempo, e.target, "tiempo");
      fueValidado = result;
      break;
  }
};

const estaValidado = () => fueValidado;

const validarCampo = (expresion, input, campo) => {
  if (expresion.test(input.value)) {
    document
      .getElementById(`grupo__${campo}`)
      .classList.remove("formulario__grupo-incorrecto");
    document
      .getElementById(`grupo__${campo}`)
      .classList.add("formulario__grupo-correcto");
    document.getElementById(`checkElement`).classList.add("fa-check-circle");
    document.getElementById(`checkElement`).classList.remove("fa-times-circle");
    campos[campo] = true;
    return true;
  } else {
    document
      .getElementById(`grupo__${campo}`)
      .classList.add("formulario__grupo-incorrecto");
    document
      .getElementById(`grupo__${campo}`)
      .classList.remove("formulario__grupo-correcto");
    document.getElementById('checkElement').classList.add("fa-times-circle");
    document.getElementById(`checkElement`).classList.remove("fa-check-circle");
    campos[campo] = false;
    document.getElementById("checkElement").classList.add("fa-times-circle");
    document.getElementById(`checkElement`).classList.remove("fa-check-circle");
    campos[campo] = false;
    return false;
  }
};

inputs.forEach((input) => {
  input.addEventListener("keyup", validarFormulario);
  input.addEventListener("blur", validarFormulario);
});

formulario.addEventListener("submit", () => {
  if (campos.tiempo) {
    document
      .querySelectorAll(".formulario__grupo-correcto")
      .forEach((icono) => {
        icono.classList.remove("formulario__grupo-correcto");
      });
  } else {
    document
      .getElementById("formulario__mensaje")
      .classList.add("formulario__mensaje-activo");
  }
});

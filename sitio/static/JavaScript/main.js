const navMenu = document.getElementById('nav-menu'),
toggleMenu = document.getElementById('toggle-menu'),
closeMenu = document.getElementById('close-menu')


toggleMenu.addEventListener('click', () => {
    navMenu.classList.toggle('show')
})

closeMenu.addEventListener('click', () => {
    navMenu.classList.remove('show')
})


//Aparicion Modal


const modalBtn = document.querySelector('.model_btn');
const modalBg = document.querySelector('.model_bg');
const closeModal = document.querySelector('.close-modal');

modalBtn.addEventListener('click', () => {
    modalBg.classList.add('bg_active');
});

closeModal.addEventListener('click', () => {
    modalBg.classList.remove('bg_active');
});


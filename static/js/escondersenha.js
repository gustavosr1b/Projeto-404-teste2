const hideIcon = document.querySelector('.form__icon--hide');
        const passField = document.querySelector('.form__input--pass');
    
        hideIcon.addEventListener('click', () => {
          hideIcon.classList.toggle('far fa-eye-slash');
          hideIcon.classList.toggle('far fa-eye');
    
          if(hideIcon.classList.contains('far fa-eye')){
            passField.type = 'text';
          }else{
            passField.type = 'password';
          }
        });
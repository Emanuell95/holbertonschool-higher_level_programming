document.addEventListener('DOMContentLoaded', function () {
    const toggleHeader = document.getElementById('toggle_header');
    const header = document.querySelector('header');
  
    toggleHeader.addEventListener('click', function () {
      if (header.classList.contains('red')) {
        header.classList.replace('red', 'green');
      } else if (header.classList.contains('green')) {
        header.classList.replace('green', 'red');
      }
    });
  });
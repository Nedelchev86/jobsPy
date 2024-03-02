const counters = document.querySelectorAll('.numberAnimated');
const speed = 400;

counters.forEach( counter => {
   const animate = () => {
      const value = +counter.getAttribute('data-number');
      const data = +counter.innerText;

      const time = value / speed;
     if(data < value) {
          counter.innerText = Math.ceil(data + time);
          setTimeout(animate, 400);
        }else{
          counter.innerText = value;
        }

   }

   animate();
});



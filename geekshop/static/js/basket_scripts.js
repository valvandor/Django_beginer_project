'use strict'
window.onload = function () {
    async function fetch_product(event) {
     const response = await fetch("/basket/edit/" + event.target.name + "/" + event.target.value + "/",
         {
             method: 'GET',
             headers: { 'X-Requested-With': 'XMLHttpRequest' }
         }
     );

     return await response.json();
    }
    let basket_list = document.querySelector('.basket_list');
    basket_list.addEventListener('click', (event) => {
        fetch_product(event).then(
            data => basket_list.innerHTML = data.result
        )
    });
}
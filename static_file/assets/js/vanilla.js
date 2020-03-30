  $(document).ready(function () {
    // GLOBAL VARIABLES
      let xhr = new XMLHttpRequest();
      let update = document.querySelectorAll('#update');
      var update_task= undefined;
      let create = $("#create");


      // create a task function
      function createtask() {

        url = document.URL;
        let title = $('#id_title').val();
        let complete = $('#id_complete').val();
        let data = `title=${title}&complete=${complete}&csrfmiddlewaretoken=${csrftoken}`;

        // open 
        xhr.open('POST', url, true);

        //send header information
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        xhr.onload = function () {
          if (xhr.status == 200) {
            console.log('yes');
          }
        }

        //send request 
        xhr.send(data);
      }

    function get_task_form(e) {
      e.preventDefault();
      id= $(this).attr('data-id');
      console.log(id);
      url_update = `/tasks/update/${id}`;
      xhr.open('GET', url_update)
      xhr.onload = function () {
        if (xhr.status == 200) {

          let div = $('#update-form-ajax');
          div[0].innerHTML = xhr.response;
          let change = document.querySelector('#update-form-ajax .card-update')
          div[0].innerHTML = change.outerHTML;
          document.querySelector('.switch-card').innerHTML = div[0].innerHTML;
          update_task= document.querySelector('.update-task');
           div[0].style.innserHTML = '<b> update </b>'

        }
      }
      xhr.send();

      return id;

    }

    function stop(e) {
   e.preventDefault();
   alert("hi");
}

    function updatetask(e) {
      
      let title = $('#id_title').val();
      let complete = $('#id_complete').val();
      let data = `title=${title}&complete=${complete}&csrfmiddlewaretoken=${csrftoken}`;
     let id = updatetask(); 
     console.lgo(id);
      //xhr.open('POST', `/tasks/`)
    }


  // handle click on create button
  create.click((e) => {
      e.preventDefault();
      createtask();
    });
  

for(let index=0; index < update.length ; index++) {
      update[index].addEventListener('click', get_task_form);
}



  })


  document.body.addEventListener('visibilitychange', function() {
    console.log('what');
  })

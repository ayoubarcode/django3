    $(document).ready(function() {

        let btn_create = $('#create-task')
        let form = $('.form-create-task');
        let btn_delete_task = $('.delete-task');
        function get_tasks() {
            $.ajax({
                url:'/tasks/tasks',
                type:'get',
                beforeSend:function(){
                }, 
                success:function(data) {
                    $('tbody').html(data);
                    btn_delete_task = $('.delete-task') 
                    
                  
                }
            });
        }


        
        

        console.log(btn_delete_task);
        
       // create task processing
        btn_create.click(function(e) {
            e.preventDefault();
            $.ajax({
                url :'/tasks/create_task',
                data: form.serialize(),
                type:'post',
                dataType:'json',
                success: function(data) {
                    $('#id_title').val('');
                    $.notify("Task successufully created !! ", "success");
                    get_tasks();
                },
                error: function(error) {
                    $.notify(" request error ", "warn");
                    
                }
            })
        });



        
        

     
      
    })

    function get_tasks() {
        $.ajax({
            url:'/tasks/tasks',
            type:'get',
            beforeSend:function(){
            }, 
            success:function(data) {
                $('tbody').html(data);
                btn_delete_task = $('.delete-task') 
                
              
            }
        });
    }

    function update_task(id,e) {
        e.preventDefault();
        $.ajax({
            url:`/tasks/update/${id}`,
            type:'get',
            beforeSend:function() {
                $('#orangeModalSubscription').modal('show')
            },
            success: function(data) {
                $('.modal-body').html(data)
            }
        })
    }

    function update_final(e) {
        e.preventDefault();
        let form = $('.update-form');
        $.ajax({
            url:`/tasks/update_task_json`,
            type:'post',
            dataType:'json',
            data: form.serialize(),
            beforeSend:function() {

            }, 
            success: function(data) {
                get_tasks()
            }

        })
    }
  

    function delete_task(id,e) {
        e.preventDefault();
        $.ajax({
            url:'/tasks/delete_task',
            type:'post',
            data: {
                'id': id,
                'csrfmiddlewaretoken':csrftoken
            },
            dataType: 'json',
            beforeSend:function() {

            }, success: function(data) {
                get_tasks();
            }
        })
    }
  



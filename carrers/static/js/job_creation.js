
var csrftoken = getCookie('csrftoken'); // Function to get the CSRF token from cookies
$.ajax({
    // ...
    headers: { "X-CSRFToken": csrftoken },
    // ...
});

$(document).ready(function () {
    // Initialize datepickers
    $('.datepicker').datepicker({
      format: 'yyyy-mm-dd',
      autoclose: true,
    });

    
    
    $("#createJobForm").submit(function(event) {
      event.preventDefault();
  
      var formData = new FormData(this);
      formData.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
      $.ajax({
          type: "POST",
          url: "{% url 'job_creation' %}",  // Update with your URL
          data: formData,
          processData: false,
          contentType: false,
          success: function(response) {
              console.log("Job created successfully!");
              $("#message").text("Job created successfully!");
              // Display a success message or handle it as needed
          },
          error: function(error) {
              console.log("Error creating job:", error);
              
          }
      });
  });
  
});

fetch('/locations/')
  .then(response => response.json())
  .then(data =>{
      const locationSelect =document.getElementById('location');
      data.locations.forEach(location => {
          const option =document.createElement('option');
          option.value =location.name;
          option.text=location.name;
          locationSelect.appendChild(option);
      })
  })



  $(document).ready(function () {
      // Initialize datepickers
      $('.datepicker').datepicker({
        format: 'yyyy-mm-dd',
        autoclose: true,
      });
    
      $("input[type='text'], textarea, select").focus(function () {
        $(this).addClass("active");
      });
    
      $("input[type='text'], textarea, select").blur(function () {
        $(this).removeClass("active");
      });

  });


  // Assuming you have a "Apply" button with a class "apply-button" for each job listing



function login(){
    debugger;
    const email = $("#email").val()
    const password = $("#password").val()
    // if (!validateMobile(email)) {
    //     show_error('Invalid mobile number');
    //     return;
    // }
    let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
    const loginData = {
        email: email,
        password: password,
        csrfmiddlewaretoken: csrfmiddlewaretoken
        };
    $.ajax({
        url: '/',
        method: 'POST',
        data: loginData,
        success: function(response) {
            if (response.status === "success") {
                window.location.href = response.redirect_url;
            } else {
                show_error(response.message);
            }
        },
        error: function(response) {
            show_error(response.responseJSON?.message || "An unexpected error occurred.");
        }
    })
  }

//   function validateMobile(mobile) {
//     const mobilePattern = /^[0-9]{10}$/;
//     return mobilePattern.test(mobile);
// }
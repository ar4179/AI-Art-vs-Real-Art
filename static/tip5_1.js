$(document).ready(function () {

    var startTime = Date.now();
    function sendTime() {
        var endTime = Date.now();
        var duration = (endTime - startTime) / 1000; // Duration in seconds
        $.post('/update_time', JSON.stringify({
            page: window.location.pathname,
            duration: duration
        }), function(response) {
            console.log("Time updated:", response.updated_time);
        }, 'json');

        let data_to_save = {"page":window.location.pathname,"duration":duration};
        
        $.ajax({
            type: "POST",
            url: "/update_time",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_save),
            success: function(result){
                console.log(result);
            },
            error: function(request, status, error){
                console.log(error);
            }
        });
    }

    // Send time when the user is about to leave the page
    $(window).on('beforeunload', function() {
        sendTime();
    });

})
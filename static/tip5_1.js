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

    function imageZoom(imgID, resultID) {
        let img = $("#" + imgID);
        let result = $("#" + resultID);
        let lens = $("<div class='img-zoom-lens'></div>");

        img.before(lens);

        let cx = result.width() / lens.width();
        let cy = result.height() / lens.height();

        result.css({
            'backgroundImage': 'url(' + img.attr('src') + ')',
            'backgroundSize': (img.width() * cx) + 'px ' + (img.height() * cy) + 'px'
        });

        lens.add(img).mousemove(function(e) {
            moveLens(e);
        });

        lens.add(img).mouseout(function() {
            result.hide();
        });

        lens.add(img).mouseover(function() {
            result.show();
        });

        function moveLens(e) {
            e.preventDefault();
            let pos = getCursorPos(e);
            let x = pos.x - (lens.width() / 2);
            let y = pos.y - (lens.height() / 2);
            x = Math.max(0, Math.min(x, img.width() - lens.width()));
            y = Math.max(0, Math.min(y, img.height() - lens.height()));
            lens.css({ left: x, top: y });
            result.css('backgroundPosition', '-' + (x * cx) + 'px -' + (y * cy) + 'px');
        }

        function getCursorPos(e) {
            let a = img.offset();
            let x = e.pageX - a.left;
            let y = e.pageY - a.top;
            return {x: x, y: y};
        }
    }

    imageZoom("img1", "zoom-result1");
    imageZoom("img2", "zoom-result2");
})
$(document).ready(function () {
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
            lens.hide();
        });

        lens.add(img).mouseover(function() {
            result.show();
            lens.show();
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

    $('.correct-btn').click(function() {
        $.post('/increment_score', function(data) {
            // Update UI with the new score
            $('#score').text(data.score);
        });
    });

    imageZoom("img1", "zoom-result1");
    imageZoom("img2", "zoom-result2");
})
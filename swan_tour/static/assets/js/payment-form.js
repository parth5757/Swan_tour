$(document).ready(function () {
    $('input[type="radio"]').on('click', (function () {
        var inputValue = $(this).attr("value");
        var targetBox = $("." + inputValue);
        $(".payment_toggle").not(targetBox).hide();
        $(targetBox).show();
    })
    )
});
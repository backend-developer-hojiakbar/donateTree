
$(document).ready(function() {
    $("#news-slider").owlCarousel({
        items : 5,
        itemsDesktop:[1199,5],
        itemsDesktopSmall:[980,3],
        itemsMobile : [600,2],
        navigation:true,
        navigationText:["",""],
        pagination:true,
        autoPlay:true
    });
});
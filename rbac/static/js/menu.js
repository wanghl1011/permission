$(".menu-title").on("click",function () {
   $(this).next().removeClass("hide");
   $(this).next().addClass("show");
   $(".menu-body").each(function () {
      if (!$(this).hasClass("show")){
         $(this).addClass("hide")
      }
   });
   $(this).next().removeClass("show");
});
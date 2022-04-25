/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    var x = document.getElementById("myTopnav");
    var y = document.getElementById("navContainer");
    var menuIcon = document.getElementById("menuIcon");
    if (x.className === "navlinks") {
      x.className += " responsive";
      y.className +=" responsive"
      menuIcon.className= "fa fa-2x fa-times"
    } else {
      x.className = "navlinks";
      y.className = "topnav"
      menuIcon.className= "fa fa-2x fa-bars"
    }
  }



  ('.topnav a').click(function(){   
    $(this).addClass('active');
    $(this).siblings().removeClass('active');
   });
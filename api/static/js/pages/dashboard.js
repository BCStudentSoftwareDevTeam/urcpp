$(document).ready(animate);

function animate(){
  var progressBar = $(".project-progress-bar");
  var projStatus = progressBar.data('status');
  console.log("projStatus: " + projStatus);
  // if (projStatus == "Reject"){
  //   var accept = $("#accept");
  //   accept.attr("id", "reject");
  //   document.getElementById("accept").setAttribute("id", "reject");
    
  //   accept.find("label").text("Denied");
  // }
  //TODO if applications are still open:
  var point = progressBar.find("#" + projStatus);
  //TODO if applications are closed: point = "#abstract_submission"
  point.addClass('point--active');
  point.prevAll().addClass('point--complete');
  point.nextAll().removeClass('point--complete');
  
  fillProgressBar(projStatus);
}

function fillProgressBar(projStatus) {
  console.log(projStatus);
  var fillPercent = 33.3;
  var step = 0;
  switch (projStatus) {
    case "AllClosed":
      step = 3;
      break;
    case "Abstract":
      step = 2;
      break;
    case "Reject":
      step = 3;
      break;
    case "Accept":
      //TODO if applications are close, abstracts are open, step = 2
      //TODO if abstracts are past due, step = 3
      step = 2;
      break;
    case "Pending":
      //TODO if applications are close, step = 3
      step = 2;
      break;
    case "Incomplete":
      //TODO if applications are closed, step = 3 
      step = 1;
      break;
    case "start":
      //TODO if applications are closed, step = 3
      step = 0;
      break;
    default:
      step = 4;
  }
  console.log(step * fillPercent);
  document.getElementById("bar_fill").style.width = (step*fillPercent) + "%";
}


/*
Point Animation

$('.point').on('click', function(e) {
  var getTotalPoints = $('.point').length,
    getIndex = $(this).index(),
    getCompleteIndex = $('.point--active').index();

  TweenMax.to($('.bar__fill'), 0.6, {
    width: (getIndex - 1) / (getTotalPoints - 1) * 100 + '%'
  });

  if (getIndex => getCompleteIndex) {
    $('.point--active').addClass('point--complete').removeClass('point--active');

    $(this).addClass('point--active');
    $(this).prevAll().addClass('point--complete');
    $(this).nextAll().removeClass('point--complete');
  }
});
 */

/*
  Demo Purposes

var progressAnimation = function() {
  var getTotalPoints = $('.point').length,
    getIndex = Math.floor(Math.random() * 4) + 1,
    getCompleteIndex = $('.point--active').index();

  TweenMax.to($('.bar__fill'), 0.6, {
    width: (getIndex - 1) / (getTotalPoints - 1) * 100 + '%'
  });

  if (getIndex => getCompleteIndex) {
    $('.point--active').addClass('point--complete').removeClass('point--active');

    $('.point:nth-child(' + (getIndex + 1) + ')').addClass('point--active');
    $('.point:nth-child(' + (getIndex + 1) + ')').prevAll().addClass('point--complete');
    $('.point:nth-child(' + (getIndex + 1) + ')').nextAll().removeClass('point--complete');
  }
};
*/

api = urcpp("v1")

function checkSameUsername() {

  dropdown = $(".selectpicker");
  
  // console.log(dropdown.length);
  // console.log((jQuery('.selectpicker').val()))
  
  
  checkNames = []

  for (var i=0; i < dropdown.length; i++) {
    
    // console.log("Specific username: " + dropdown[i].value);
      if (checkNames.includes(dropdown[i].value)){  //Checks to see if the value on dropdown is the same as one already in checkNames
        // console.log("You have inputed the same username more than once. Failure.");
        $("#failedSameUsername").show();
        return;
      }
      else { 
        checkNames.push(dropdown[i].value);
        // console.log(checkNames); 
        
        for (var b=0; b < checkNames.length; b++) {
          if (checkNames.includes("")) {
            $("#failedNoEntry").show();
            return;
          }
        }
      }
    }
    
  // console.log("You used unique usernames for each input! You win at life!");
  submitData(); 

};



function submitData() {  
  console.log($("#collabForm"));
  /* Ajax the data to /budget */
  $("#collabForm")[0].submit();  
  //console.log("Submitted");
};
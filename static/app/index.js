var arr = [ "alaknanda", "budh vihar", "chhattarpur", "chittaranjan park", "commonwealth games village", "dilshad garden", "dwarka", "friends colony", "greater kailash", "hauz khas", "kalkaji", "karol bagh", "kirti nagar", "lajpat nagar", "laxmi nagar", "mahavir enclave", "malviya nagar", "mehrauli", "narela", "okhla", "paschim vihar", "patel nagar", "punjabi bagh", "rohini", "safdarjung enclave", "saket", "sarita vihar", "shahdara", "sheikh sarai", "sultanpur", "uttam nagar", "vasant kunj", "vasundhara enclave"];
      var options="<option >Select one</option>";
      arr.map((op,i)=>{
         options+=`<option value="${op}" id="${i}" ">${op}</option>`
      })

      document.getElementById("Location").innerHTML=options;


      document.addEventListener('DOMContentLoaded', function() {
         // Get the submit button
         var submitBtn = document.querySelector('.submit');
       
         // Add event listener to the button
         submitBtn.addEventListener('click', function() {
           // Trigger the form submission
           document.querySelector('form').submit();
         });
       });
       
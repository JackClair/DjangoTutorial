var name = prompt("Enter Your Name: ");
var age = prompt("Enter ypur Age: ");
var hei = prompt("Enter your Height: ");
var pet = prompt("Ente your pet Name");

var ans = 0;
var len = name.lenght;

for (var i = 0; i < name.length; i++) {
  if (name[i] == " ") {
    if (name[0] == name[i+1]) {
      ans++;
    }
  }
}

if (age > 20 && age < 30){
  ans++;
}

if (hei > 170) {
  ans++;
}

var pey=pet.lenght;
alert(pet[pey-1]);
if (pet[len-1]==="y") {
  ans++;
}
alert(ans);
if (ans == 4) {
  console.log("Thats my man");
}
else {
  console.log("Nothing here to see");
}

var admin = require("firebase-admin");
var serviceAccount = require("./privateKey.json");
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://beacon-reader-b5179-default-rtdb.asia-southeast1.firebasedatabase.app"
});
var db = admin.database();
var dataRef = db.ref("beacon");


//for (let i = 0; i < 50; i++) {
  // Generate a unique key for each object (replace with preferred method if needed)
  //const uniqueKey = Math.random().toString(36).substring(2, 15); // Random alphanumeric string

  //const objectToAdd = {
    //namespace: "kambing",
    //rssi: "-50"
  //};

  // Add data using the unique key
  //dataRef.child(uniqueKey).set(objectToAdd);
//}

//dataRef.on('value', (snapshot) => {
  //const data = snapshot.val(); // Get the data as a JavaScript object
//   Display the data (see below for options)
 // console.log("data", data)
//});
dataRef.on('value', (snapshot) => {
const data = snapshot.val();
  const dataArray = Array.from(Object.values(data)); // Convert object values to an array

  // Now you can iterate over dataArray using traditional array methods
  dataArray.forEach((object) => {
    console.log(`Namespace: ${object.namespace}, RSSI: ${object.rssi}`);
  });
})

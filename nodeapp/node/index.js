const admin = require('firebase-admin');
const serviceAccount = require('./privateKey.json');
const express = require('express'); // Assuming you're using Express
const cors = require("cors")
const bodyParser = require('body-parser');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://beacon-reader-b5179-default-rtdb.asia-southeast1.firebasedatabase.app"
});

const db = admin.database();
const dataRef = db.ref("beacon");

const app = express();
app.use(cors({ origin: true }));
app.use(bodyParser.json());

app.get('/firebase-data', (req, res) => {
  dataRef.on('value', (snapshot) => {
    const data = snapshot.val();
    res.json(data); // Send the data as JSON to the client
  });
});

app.post('/beacon/insert', (req, res) => {
  console.log("data", req.body)
  dataRef.set({
    rssi: req.body.rssi,
    namespace: req.body.additional_info.namespace
  })
  res.send('Beacon data received!');
});

app.listen(3000, () => console.log('Server listening on port 3000'));

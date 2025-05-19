const express = require('express');
const mongoose = require('mongoose');
const { GoogleSpreadsheet } = require('google-spreadsheet');
const fs = require('fs');
const rawData = fs.readFileSync('./answers.json');
const jsonData = JSON.parse(rawData);
console.log(jsonData)
const app = express();
const port = 5002;

// Updated Mongoose connection with proper error handling
const MONGODB_URI = process.env.MONGODB_URI;
mongoose.connect(MONGODB_URI, {
  serverSelectionTimeoutMS: 5000,
  socketTimeoutMS: 45000,
})
.then(() => console.log('MongoDB connected successfully'))
.catch((err) => {
  console.error('MongoDB connection error:', err);
  process.exit(1);
});

const YourSchema = new mongoose.Schema({
  timeStamp:{type:String},
  answer:{type:String},
  answer2:{type:String},
  answer3:{type:String},
});

const YourModel = mongoose.model('YourModel', YourSchema);
const creds = require('./credentials.json');

const doc = new GoogleSpreadsheet('1dYS5jnA30LYiito0ebQElK53r4WZpULV0l0W7PKSMcM');
app.get('/sync-data', async (req, res) => {
  try {
    
    await YourModel.insertMany(jsonData);

    res.status(200).json({ success: true, message: 'Data synced successfully.' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ success: false, message: 'Internal Server Error' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://${MONGODB_URI}:${port}`);
});

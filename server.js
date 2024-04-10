const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');
const app = express();
const port = 3000;

app.use(bodyParser.json());

// Serve the HTML page
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/ui.html');
});

// Handle user input
app.post('/user_input', (req, res) => {
  const userInput = req.body.input;
  
  // Execute the Python script
  const pythonProcess = spawn('python', ['cookassist.py']);
  
  // Pass user input to Python script
  pythonProcess.stdin.write(userInput + '\n');
  pythonProcess.stdin.end();
  
  // Collect output from Python script
  let output = '';
  pythonProcess.stdout.on('data', (data) => {
    output += data.toString();
  });

  // When Python script finishes, send response back to client
  pythonProcess.on('close', (code) => {
    res.json({message: output});
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

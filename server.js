const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');
const path = require('path'); // Import the 'path' module

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Serve the HTML page
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/ui.html');
});

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public'), {
    setHeaders: (res, filePath) => {
        if (filePath.endsWith('.css')) {
            res.setHeader('Content-Type', 'text/css');
        }
    }
}));

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

const express = require("express");
const app = express();
const path = require("path");
const cors = require('cors');
const { spawn } = require('child_process');
let result = '';

// middleware for parsing data to json
app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// setting view engine
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// path for serving static files
app.use(express.static(path.join(__dirname, "public")));

app.get('/CropPredict',(req,res)=>{
    res.render("home.ejs");
})

app.post('/CropPredict/model', (req,res)=>{
    const state = req.body.State;
    const rainfall = parseFloat(req.body.Rainfall);
    const ph = parseFloat(req.body.PH);
    const temperature = parseFloat(req.body.Temperature);
    const soil_type = req.body.Soil_type;

    // Use the correct Python path for your system
    const pythonPath = 'C:\\Users\\KOVIDH V. S. BHATI\\AppData\\Local\\Programs\\Python\\Python312\\python.exe';  // Update with your actual path
    const scriptPath = path.resolve(__dirname, './pred_model/main.py');

    console.log('Spawning Python process with:', pythonPath, scriptPath);

    const pythonProcess = spawn(pythonPath, ['-u', "D:\\Academics\\VIT\\Project Exhibition - Final Review\\pred_model\\main.py", state, rainfall, ph, temperature, soil_type],{
        cwd: 'D:\\Academics\\VIT\\Project Exhibition - Final Review\\pred_model'  // Set the working directory
    });

    result = '';
    pythonProcess.stdout.on('data', (data) => {
        console.log('Python stdout:', data.toString());
        result += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error('Python stderr:', data.toString());
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python process exited with code: ${code}`);
        if (code !== 0 || !result.trim()) {
            console.error('Error or empty result:', result);
            res.status(500).send('Python script failed or no output received');
        } else {
            console.log('Final result from Python:', result);
            // res.send(result.trim());
            res.redirect("/CropPredict/model");
        }
    });

    pythonProcess.on('error', (err) => {
        console.error('Error spawning Python process:', err);
        res.status(500).send('Failed to execute Python script');
    });
});

app.get('/CropPredict/model', (req, res)=>{
    res.render("index.ejs", {Crop: result});
});
// app.post('/CropPredict', (req, res)=>{
//     res.render("index.ejs", {Crop : "Wheat"});
// });

app.listen(process.env.PORT || 5000);
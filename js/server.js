const express = require('express');
const path = require('path');
const { PORT, UPLOADS_DIR } = require('./config');
const { ensureFolderExists } = require('./utils/fileUtils');
const mockupRoutes = require('./routes/mockupRoutes');

const app = express();

// Ensure folders
ensureFolderExists(UPLOADS_DIR);
ensureFolderExists(path.join(__dirname, '../sample_outputs'));

// Serve static folders
app.use('/sample_outputs', express.static(path.join(__dirname, '../sample_outputs')));
app.use('/uploads', express.static(UPLOADS_DIR));
app.use(express.static(path.join(__dirname, 'public')));

// Routes
app.use('/', mockupRoutes);

app.listen(PORT, () => {
  console.log(`Mock Product Visualizer running at http://localhost:${PORT}`);
});

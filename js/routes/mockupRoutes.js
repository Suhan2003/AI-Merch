const express = require('express');
const multer = require('multer');
const { UPLOADS_DIR } = require('../config');
const { createMockup } = require('../controllers/mockupController');
const { ensureFolderExists } = require('../utils/fileUtils');
const path = require('path');
const fs = require('fs');

ensureFolderExists(UPLOADS_DIR);

const router = express.Router();

// Multer setup for uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, UPLOADS_DIR),
  filename: (req, file, cb) => cb(null, 'uploaded_product.png'),
});
const upload = multer({ storage });

// Home route
router.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../public', 'index.html'));
});

// Upload route
router.post('/upload', upload.single('product_image'), async (req, res) => {
  console.log("Image uploaded:", req.file.path);
  const mockupData = await createMockup(req.file.path);
  res.json(mockupData);
});

module.exports = router;

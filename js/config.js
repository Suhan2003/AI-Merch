const path = require('path');

module.exports = {
  PORT: 3000,
  TEMPLATE_PATH: path.join(__dirname, '../assets/template.jpeg'),
  UPLOADS_DIR: path.join(__dirname, 'uploads'),
  OUTPUT_PATH: path.join(__dirname, '../sample_outputs/mockup.png'),
  JSON_OUTPUT: path.join(__dirname, '../sample_outputs/mockup.json'),
};

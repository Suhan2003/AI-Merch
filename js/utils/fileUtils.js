const fs = require('fs');

function ensureFolderExists(folderPath) {
  fs.mkdirSync(folderPath, { recursive: true });
}

module.exports = { ensureFolderExists };

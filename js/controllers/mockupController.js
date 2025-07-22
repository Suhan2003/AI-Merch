const fs = require('fs');
const { createCanvas, loadImage } = require('canvas');
const path = require('path');
const { TEMPLATE_PATH, OUTPUT_PATH, JSON_OUTPUT } = require('../config');

async function createMockup(uploadedImagePath) {
  const canvas = createCanvas(800, 800);
  const ctx = canvas.getContext('2d');

  const template = await loadImage(TEMPLATE_PATH);
  const product = await loadImage(uploadedImagePath);

  ctx.drawImage(template, 0, 0, 800, 800);
  ctx.drawImage(product, 200, 200, 400, 400);

  fs.writeFileSync(OUTPUT_PATH, canvas.toBuffer('image/png'));

  const mockupData = {
    message: "✅ Uploaded successfully!",
    mockup_url: '/sample_outputs/mockup.png',
    original_image: '/uploads/uploaded_product.png',
    product_id: 'mock' + Math.floor(Math.random() * 1000),
    variant: 't-shirt',
    image_position: 'center',
    caption: 'A funny t-shirt mockup generated automatically',
    tags: ['funny', 't-shirt', 'programmer', 'AI', 'mockup']
  };

  fs.writeFileSync(JSON_OUTPUT, JSON.stringify(mockupData, null, 2));
  console.log("✅ Mockup generated and saved successfully!");
  return mockupData;
}

module.exports = { createMockup };

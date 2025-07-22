<?php
if ($_SERVER['REQUEST_METHOD']==='POST') {
    shell_exec('python ../python/generate_product.py');
    shell_exec('node ../js/generate_mockup.js');
    $json = json_decode(file_get_contents('../sample_outputs/mockup.json'), true);
}
?>



<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🛍️ AI Merch Maker Lite</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">



  
  <style>
    body {
      font-family: 'Inter', sans-serif;
      background: linear-gradient(to bottom, #f9fafb, #e5e7eb);
      color: #333;
      margin: 0;
      padding: 0;
      text-align: center;
    }

    header {
      background-color: #111827;
      color: white;
      padding: 40px 0 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    h1 {
      font-size: 2.5rem;
      margin: 0;
    }

    main {
      padding: 40px 20px;
      max-width: 800px;
      margin: auto;
    }

    button {
      background: #2563eb;
      color: white;
      border: none;
      padding: 15px 30px;
      font-size: 1.1rem;
      border-radius: 10px;
      cursor: pointer;
      transition: background 0.3s ease;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    button:hover {
      background: #1e40af;
    }

    .mockup {
      margin-top: 40px;
    }

    img {
      width: 400px;
      border-radius: 12px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    ul {
      list-style: none;
      padding: 0;
      font-size: 18px;
      text-align: left;
      margin: 20px auto;
      display: inline-block;
    }

    li {
      margin-bottom: 10px;
    }

    footer {
      padding: 30px 10px;
      background: #f1f5f9;
      font-size: 0.9rem;
      color: #6b7280;
      margin-top: 40px;
    }

  </style>
</head>



<body>
  <header>
    <h1>🛍️ AI Merch Maker Lite</h1>
    <p style="margin-top: 10px; font-weight: 400;">Create stylish mockups with one click using AI</p>
  </header>




  <main>
    <form method="POST">
      <button type="submit">✨ Generate New Merch</button>
    </form>

    <?php if (!empty($json)): ?>
      <div class="mockup">
        <h2 style="margin-top: 40px;">✅ Generated Mockup</h2>
        <img src="mockup.png" alt="Mockup Preview">
        
        <h3 style="margin-top: 30px;">📄 Product Details</h3>
        <ul>
          <li>🆔 <strong>Product ID:</strong> <?php echo htmlspecialchars($json['product_id']); ?></li>
          <li>👕 <strong>Variant:</strong> <?php echo htmlspecialchars($json['variant']); ?></li>
          <li>📍 <strong>Image Position:</strong> <?php echo htmlspecialchars($json['image_position']); ?></li>

          <?php if (isset($json['caption'])): ?>
            <li>🖼️ <strong>Caption:</strong> <?php echo htmlspecialchars($json['caption']); ?></li>
          <?php endif; ?>

          <?php if (isset($json['tags']) && is_array($json['tags'])): ?>
            <li>🏷️ <strong>Tags:</strong> <?php echo htmlspecialchars(implode(', ', $json['tags'])); ?></li>
          <?php endif; ?>
        </ul>
      </div>
    <?php endif; ?>
  </main>



  <footer>
    Built with ❤️ by Sheetal Rao | AI + PHP + Node + Python
  </footer>

</body>
</html>

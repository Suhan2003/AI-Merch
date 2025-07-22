<?php
// Accepts JSON product data and returns a fake product ID
header('Content-Type: application/json');

// Get raw POST body
$data = json_decode(file_get_contents('php://input'), true);

// Log/display the incoming data
file_put_contents("received_product.json", json_encode($data, JSON_PRETTY_PRINT));

// Return a fake product ID
$response = [
    "status" => "success",
    "product_id" => "fake-prod-" . rand(1000, 9999)
];

echo json_encode($response);
?>

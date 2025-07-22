<?php
$mockupFile = '../sample_outputs/mockup.json';
$outputCSV = '../sample_outputs/mockup.csv';

if (!file_exists($mockupFile)) {
    echo "Mockup JSON not found.";
    exit;
}

$data = json_decode(file_get_contents($mockupFile), true);

$fp = fopen($outputCSV, 'w');
fputcsv($fp, array_keys($data));
fputcsv($fp, array_values($data));
fclose($fp);

echo "✅ CSV exported to $outputCSV";
?>

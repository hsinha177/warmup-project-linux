<?php
    
    $img = $_POST['image'];
    $folderPath = "snaps/";
  
    $image_parts = explode(";base64,", $img);
    $image_type_aux = explode("image/", $image_parts[0]);
    $image_type = $image_type_aux[1];
  
    $image_base64 = base64_decode($image_parts[1]);
    $fileName = 'image' . '.jpg';
  
    $file = $folderPath . $fileName;
    file_put_contents($file, $image_base64);
  
    echo "successfully saved snap. Snap id : ";
    print_r($fileName);

    $namefile = "imageid.txt";
    $fp = fopen($namefile, "w");
    fwrite($fp,$fileName);
    fclose($fp)
  
?>

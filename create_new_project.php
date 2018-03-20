
Project name: <?php echo $_POST["projectName"]; ?><br>
Project description: <?php echo $_POST["projectDescription"]; ?><br>
Management style: <?php echo $_POST["managementStyle"]; ?><br>
GitHub user: <?php echo $_POST["githubUser"]; ?><br>

<?php
$data = $_POST["projectName"] . '~' . $_POST["projectDescription"] . '~' . $_POST["managementStyle"] . '~' . $_POST["githubUser"];
$ret = file_put_contents('/var/www/html/uploads/usrinput.txt', $data, FILE_APPEND | LOCK_EX);
if($ret === false) {
    die('There was an error writing this file');
}
else {
    echo "$ret bytes written to file";
}
?>

<br>

<br>

<?php
//Upload the image file
$target_dir = "uploads/";
$target_file = $target_dir . "mainpicture.jpg";
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["projectImage"]["tmp_name"]);
    if($check !== false) {
        echo "File is an image - " . $check["mime"] . ".";
        $uploadOk = 1;
    } else {
        echo "File is not an image.";
        $uploadOk = 0;
    }
}
// Check if file already exists
if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}
// Check file size
if ($_FILES["projectImage"]["size"] > 500000) {
    echo "Sorry, your file is too large.";
    $uploadOk = 0;
}
// Allow certain file formats
if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
&& $imageFileType != "gif" ) {
    echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
    $uploadOk = 0;
}
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["projectImage"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["projectImage"]["name"]). " has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your file.";
        echo $target_file;
    }
}
?>

<br>

<br>

<?php
//Upload the zip file
$target_dir = "uploads/";
$target_file = $target_dir . "userUpload.zip";
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["projectFiles"]["tmp_name"]);
}
// Check if file already exists
if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}
// Check file size
if ($_FILES["projectFiles"]["size"] > 500000) {
    echo "Sorry, your file is too large.";
    $uploadOk = 0;
}
// Allow certain file formats
if($imageFileType != "zip") {
    echo "Sorry, only zip files are allowed.";
    $uploadOk = 0;
}
// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["projectFiles"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["projectFiles"]["name"]). " has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your file.";
        echo $target_file;
    }
}
?>

<br>

<br>


<?php
    // run the script which will create the repository
    $output=shell_exec('sh /var/www/html/createRepo.sh');
    echo $output;
?>
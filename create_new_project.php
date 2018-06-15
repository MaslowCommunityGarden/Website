<html>

<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Open+Sans">
</head>

<body>
    <header class = 'header'>
        <div class='inner-header'>
            <a href='index.html'>
                <img src='logo.png' style='width:auto;height:90px;border:0;'>
            </a>
            <nav class='navigation'>
                <a href='howdoesthegardenwork.html' class='nav-link button one-col'>How Does the Garden Work?</a>
                <a href='addaproject.html' class='nav-link button one-col'>Add A Project</a>
                <a href='index.html' class='nav-link button one-col'>Browse Projects</a>
            </nav>
        </div>
    </header>


<h1>Your project is being generated!</h1>

<p>If your project generates properly, you will receive an email inviting you to access the project and it will appear when the website regenerates in one minute.</p>

<br>

<p>While waiting for your project to be created check out the instructions tab <a href="http://maslowcommunitygarden.org/Website.html">here</a> for tips on how to interact with your new project.</p>

<br>
<br>
<br>

<p>The output from the php and python scripts which uploads and tests your files is: </p>

<div style = "background-color: lightgray;">
<?php
$data = htmlspecialchars($_POST["projectName"]) . '~' . htmlspecialchars($_POST["projectDescription"]) . '~' . htmlspecialchars($_POST["managementStyle"]) . '~' . htmlspecialchars($_POST["githubUser"]) . '~' . htmlspecialchars($_POST["category"]);
$ret = file_put_contents('/var/www/html/uploads/usrinput.txt', $data, FILE_APPEND | LOCK_EX);
if($ret === false) {
    die('The script was unable to write your inputs to the file');
}
else {
    echo "$ret bytes written to file";
}

//Upload the image file
$target_dir = "uploads/";
$target_file = $target_dir . "mainpicture.jpg";
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["projectImage"]["tmp_name"]);
    if($check !== false) {
        echo "The image file looks good - " . $check["mime"] . ".";
        $uploadOk = 1;
    } else {
        echo "That file was not an image!.";
        $uploadOk = 0;
    }
}
// Check if file already exists
if (file_exists($target_file)) {
    echo "Oh no! That file already exists.";
    $uploadOk = 0;
}
// Check file size
if ($_FILES["projectImage"]["size"] > 5000000) {
    echo "Sorry, your image is too large. The limit is 5MB";
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
    echo "Sorry, your image file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["projectImage"]["tmp_name"], $target_file)) {
        echo "\nThe file ". basename( $_FILES["projectImage"]["name"]). " has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your image file.";
        echo $target_file;
    }
}

//Upload the zip file
$target_dir = "uploads/";
$target_file = $target_dir . "userUpload.zip";
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

// Check if file already exists
if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}
// Check file size
if ($_FILES["projectFiles"]["size"] > 50000000) {
    echo "Sorry, your zip file is too large. The limit is 50mb. To add larger files upload them directly to GitHub once the project is created.";
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
        echo "There was an error uploading your zip file.";
        echo $target_file;
    }
}
    // run the script which will create the repository
    $pythonOutput=shell_exec('/var/www/html/createRepo.sh 2>&1');
    
    $atestinput = "this input > is for < testing";
    
    preg_match("/(?<=\>)(.*?)(?=\<)/", $pythonOutput, $githubURL);
    
    echo "Python output: \n\n";
    
    //echo $pythonOutput;
    
    echo "\n\n:End python output     ";
    
    echo gettype($pythonOutput);
    
    echo "    matches:   ";
    
    $gitLinkURL = $githubURL[0]."/invitations";
    $gitLinkURL = str_replace(' ', '', $gitLinkURL);
    
    echo $gitLinkURL;
    
?>

</div>


<a href='<?php echo $gitLinkURL;?>' class='nav-link button one-col' target="_blank" >Accept Invitation</a>

<br>

<br>

<br>

</body>
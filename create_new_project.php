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


<h1>A GitHub repository, a forums thread, and a page in the Community Garden are being generated for your project!</h1>

<br>

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
    
    preg_match("/(?<=\>)(.*?)(?=\<)/", $pythonOutput, $githubURL);
    
    
    //echo $pythonOutput;
    
    $gitLinkURL = $githubURL[0]."/invitations";
    $gitLinkURL = str_replace(' ', '', $gitLinkURL);
    
?>

</div>


<a href='<?php echo $gitLinkURL;?>' class='nav-link button one-col' target="_blank" >Accept Invitation</a> 

<br>

You are invited to be given access to manage your project's GitHub repository which stores all of your projects files. You will also recieve an email inviting you to access them.

<br>
<br>

<a href='http://maslowcommunitygarden.org/Website.html?instructions=true' class='nav-link button one-col' target="_blank" >Read Instructions</a>  
<br>
Read the instructions for how to interact with and manage your new project

<br>
<br>

<a href='https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet' class='nav-link button one-col' target="_blank" >Markdown Guide</a>  
<br>
Learn more about how to format your Community Garden page with Markdown

<br>
<br>
<br>
<br>
<br>

Log from the python script which creates the github repo:

<div style = "background-color: lightgray;">

<?php
    echo $pythonOutput;
?>

</div>

</body>
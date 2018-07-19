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

    <section class="content new-project">
            
        <h1>A GitHub repository, a forums thread, and a page in the Community Garden are being generated for your project!</h1>
        
        <br>
        
        <div>
        
            <a href='<?php echo $gitLinkURL;?>' class='nav-link button one-col' target="_blank" >Accept Invitation</a> 
        
            <p class="two-col">You are invited to be given access to manage your project's GitHub repository which stores all of your projects files. You will also receive an email inviting you to access them.</p>
        </div>
        
        <br>
        
        <div>
        
            <a href='http://maslowcommunitygarden.org/Website.html?instructions=true' class='nav-link button one-col' target="_blank" >Read Instructions</a>  
            
            <p class="two-col">Read the instructions for how to interact with and manage your new project</p>
            
        </div>
        
        <br>
        
        <div>
        
            <a href='https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet' class='nav-link button one-col' target="_blank" >Markdown Guide</a>  

            <p class="two-col">Learn more about how to format your Community Garden page with Markdown</p>
        
        </div>
            
        <br>
        
        <div>
                    
            <button title="script-log" type="button" class="button one-col" style="float: left;" onclick="if(document.getElementById('spoiler') .style.display=='none') {document.getElementById('spoiler') .style.display=''}else{document.getElementById('spoiler') .style.display='none'}">View the Script Log</button>
            
            <p class="two-col" style="float: right;">Log from the python script which creates the github repo.</p>
            
            <div id="spoiler" style="display:none" class="three-col">
                
                <br>
                <br>
                <br>
                
                <div class="log">
                    <?php
                    $data = htmlspecialchars($_POST["projectName"]) . '~' . htmlspecialchars($_POST["projectDescription"]) . '~' . htmlspecialchars($_POST["managementStyle"]) . '~' . htmlspecialchars($_POST["githubUser"]) . '~' . htmlspecialchars($_POST["category"]);
                    $ret = file_put_contents('/var/www/html/uploads/usrinput.txt', $data, FILE_APPEND | LOCK_EX);
                    if($ret === false) {
                        die('The script was unable to write your inputs to the file');
                    }
                    else {
                        echo "<br> $ret bytes written to file";
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
                            echo "<br> The image file looks good - " . $check["mime"] . ".";
                            $uploadOk = 1;
                        } else {
                            echo "<br> That file was not an image!.";
                            $uploadOk = 0;
                        }
                    }
                    // Check if file already exists
                    if (file_exists($target_file)) {
                        echo "<br> Oh no! That file already exists.";
                        $uploadOk = 0;
                    }
                    // Check file size
                    if ($_FILES["projectImage"]["size"] > 5000000) {
                        echo "<br> Sorry, your image is too large. The limit is 5MB";
                        $uploadOk = 0;
                    }
                    // Allow certain file formats
                    if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
                    && $imageFileType != "gif" ) {
                        echo "<br> Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
                        $uploadOk = 0;
                    }
                    // Check if $uploadOk is set to 0 by an error
                    if ($uploadOk == 0) {
                        echo "<br> Sorry, your image file was not uploaded.";
                    // if everything is ok, try to upload file
                    } else {
                        if (move_uploaded_file($_FILES["projectImage"]["tmp_name"], $target_file)) {
                            echo "<br> \nThe file ". basename( $_FILES["projectImage"]["name"]). " has been uploaded.";
                        } else {
                            echo "<br> Sorry, there was an error uploading your image file.";
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
                        echo "<br> Sorry, file already exists.";
                        $uploadOk = 0;
                    }
                    // Check file size
                    if ($_FILES["projectFiles"]["size"] > 50000000) {
                        echo "<br> Sorry, your zip file is too large. The limit is 50mb. To add larger files upload them directly to GitHub once the project is created.";
                        $uploadOk = 0;
                    }
                    // Allow certain file formats
                    if($imageFileType != "zip") {
                        echo "<br> Sorry, only zip files are allowed.";
                        $uploadOk = 0;
                    }
                    // Check if $uploadOk is set to 0 by an error
                    if ($uploadOk == 0) {
                        echo "<br> Sorry, your file was not uploaded.";
                    // if everything is ok, try to upload file
                    } else {
                        if (move_uploaded_file($_FILES["projectFiles"]["tmp_name"], $target_file)) {
                            echo "<br> The file ". basename( $_FILES["projectFiles"]["name"]). " has been uploaded.";
                        } else {
                            echo "<br> There was an error uploading your zip file.";
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
                
                <br>
                <br>
                <br>
                
                <?php
                    echo $pythonOutput;
                ?>
                <br>
                </div>
            </div>
        
        </div>
        
    </section>
    
    <footer class='footer-basic-centered' style='clear: both;'>

        <p class='footer-company-motto three-col'>The garden is a project of the <a href='http://www.maslowcnc.com'>Maslow CNC</a> community.</p>

        <div class='footer-links content'>
            <a href='http://maslowcommunitygarden.org/howdoesthegardenwork.html' class='button'>Why</a>
            
            <a href='#' class='button'>How</a>
            
            <a href='http://maslowcommunitygarden.org/addaproject.html' class='button'>Add</a>
            
            <a href='http://maslowcommunitygarden.org/index.html' class='button'>See</a>
            
            <a href='http://www.maslowcnc.com/' class='button'>Maslow CNC</a>
            
            <a href='http://www.maslowcnc.com/forums' class='button'>Forums</a>
            
        </div>

        <p class='footer-company-name three-col'>All content available under license of creator</p>

    </footer>

</body>
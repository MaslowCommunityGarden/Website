# How to create a project

To create a new project click the "Add A Project" button at the top of the page. This will take you to a simple form to create a new project.

![create a new project](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/CreateAProject/BlankForm.JPG)

The form is designed to allow you to create a new project quickly and easily. Most of the elements of the project can be changed later if you want.

The form will ask you for the following things:

- **Project Title** This is the name of the project. It cannot be changed later because it will be used to choose the URL for the project.
- **A Project Description** A short description of what the project is.
- **Your GitHub Username** This is your username for [GitHub](https://github.com/). This is important because GitHub is the system we use for collaboration. You will automatically be sent an email invitation through github giving you access to edit the project files. Don't have an account? Make a free one [here](https://github.com/join).
- **A Main Picture** This picture will show up in the list of projects in the community garden.
- **A Zip Folder of Project Files** These are the files which your project will start off with. Files can easily be updated, added, or removed later. If the project has very large files it is probably easier to upload them later.
- **How do you want the project controlled** If you select "community managed" the community will be able to vote to approve or reject proposed changes to the project (you will still be able to make changes as the creator). If you choose that you want to manage then ONLY YOU will be able to approve changes to the project.

When you are ready click "Create" and your project will be generated! 

The website refreshes every few minutes so it may be several minutes before your project shows up.

Questions or comments? Let us know in [the forums](https://forums.maslowcnc.com)

# How to edit, update, or add files to a project you created

As soon as your project is created an invitation will be emailed to you inviting you to have direct access to the project. The invitation looks like this:

![github invitation](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditYourProject/Invitation.JPG)

After accepting the invitation you can:

### Edit any page

Edit any page by clicking the the "Edit this page" button on any page

![edit this page](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditYourProject/Editthispage.JPG)

and then clicking the pen icon in the upper right corner to edit the file.

![edit this file](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditYourProject/Editfile.JPG)

It can take several minutes for your changes to show up on the website.

The "What's Markdown" section below can help you make your page look beautiful.

### Remove any file

To remove any file press the "Source" button from your project's page

![source btn](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditYourProject/SourceBtn.JPG)

Click the file you want to delete, then click the trash can icon in the upper right.

![delete this file](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditYourProject/Deletefile.JPG)

### Upload new files

To remove any file press the "Source" button from your project's page

![source btn](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditYourProject/SourceBtn.JPG)

Then click the "Upload Files" button in the upper right.

![upload files](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditYourProject/Uploadfiles.JPG)

# How to edit, update, or add files to a project created by someone else

The real power of GitHub is that anyone can edit any file or page. There is one big difference between when the creator of a project edits a page and when anyone else does and that is that while the creator of a project can simply make changes at will, everyone else has to propose a change and have it approved by the project creator or the community.

The process of contributing to a project that you didn't create is similar to the instructions above for a project you did create with the additional step of needing to ask permission.

Let's demonstrate by editing the text on one of the project pages. First click the "Edit this page" button on any page.

![click the edit button](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditAnyPage/clickedit.png)

Then click the pencil icon on in the upper right corner.

![click the edit file pencil](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditAnyPage/editpencil.png)

Notice that there will be a notice at the top of the file. Scroll down and make your edits.

![see warning and edit](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditAnyPage/editthefile.png)

When you are ready to propose your changes, click the "Propose a change" button at the bottom of the page.

![click propose a change](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditAnyPage/clickproposefilechange.png)

Requests to change a file in GitHub are called "Pull Requests". Press the "Create pull request" button to create one

![create a pull request](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditAnyPage/presscreatepullrequest.png)

Enter a description of what changes you made and why they should be included, then press "Send pull request". Your changes have now been submitted for approval! Congratulations! 

![send pull request](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditAnyPage/sendpullrequest.png?raw=true)

# What's Markdown?

Markdown is a language which lets you edit the feel of a file with from a text editor. It supports behaviors like bold text, hyperlinks, imbeded images, lists and tables, and more!

[This Markdown quick reference guide](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) can help you get a better understanding of how to format your text...or just leave it plain if you don't want to bother.

# How to add pictures to a page

To add a picture to your page embed it with the markdown text `![some description of the picture](link-to-the-picture)`

For us the images are usually hosted within the github repository for the project. To find the link to the picture click on the picture in the project repository, then right click and select "Open image in new tab".

![open image in a new tab](https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/ImbedAnImage/openinnewtab.JPG)

Use the URL at the top of the page for the link to the picture. It should be something like

`https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditYourProject/Editfile.JPG` 

Note that URLs which look like 

`https://raw.githubusercontent.com/MaslowCommunityGarden/Website/master/Instructions/EditYourProject/Editfile.JPG` 

will render properly on github itself, but the image won't show up on the project page in the community garden.

# Cisco Live Instructor led lab web page core
This repository is for the core base of the LTR lab used by engineers in the SVS team to 
present students lab material. To be able to share the core base code, the repository is
split in two separate components. The tree structure looks like the following:

```
/
/core
  /docker
  /static
  /templates
/lab
  /static
  /templates
  /yaml
```

You just need to pull from git one single repository, but underneath it really is two separate repositories. One is managed by the core side that we want to share with across all the labs to avoid wasting time. And the second under the root and /lab portions are where the meat of the template work will live. 

The docker container folder underneath the /core directory contains everything to instantiate the APP. You would run the docker-compose from that directory. You do have to setup a specific environment file to give the port execution. More on this in a moment.

## The whole GIT subtree process
To accomplish sharing the core amongst the labs, we will be using GIT ```sub-tree``` instead of git ```sub-modules```. The big advantage of sub-tree is that it gets incorporated into your git repo just like any other directory. With this we can easily push and update on the server side. With ```sub-tree``` you can make changes to the git repo that lives underneath your primary git tree and even pull changes that are incorporated. 

The one criticism is that the changes in these ```sub-tree``` modules will be listed with yours. So for example, if you did this with the bootstrap code straight from github, all those commits would suddenly show up and make your commit history hard to read. You can squash these, but in this case for what we do I think we would want to see them as those commits would tell us what changes happened to the shared libraries.

So for this reason the ```/core``` structure is a subtree in ```/```. And any changes that are made in ```/core``` need to be double committed. In the normal process they will be added/committed into your repository. But any changes you will want to push back and manage to the ```/core``` repository for everyone to get the updates and also to make sure **you can update going forward** or you will have to manage loosing track of ```HEAD``` with conflicts.

### Step 1
The first step will be to clone this repository, aka the LAB portion.
```
git clone git@svs-rtp-web-git.cisco.com:SVS/webltr-lab.git <directory_name>
```
This will clone everything into your environment.

### Step 2
This sounds nuts, but you now need to delete the .git repository from this pull. The reason is that this is just an example template of the lab portion. You don't want to commit back to this repository.

### Step 3
Initialize a new REPO on GITLAB/GITHUB. Remember that if this is for the DMZ, the DMZ servers can't reach the internal GITHUB servers. You can use public github if you wish or you can request access to our internal gitlab DMZ instance.

### Step 4
Take the steps to initialize git in this new folder. In gitlab it provides the directions for you for existing folder. Don't forget that for SSH you are going to need to have all the proper keys setup with the gitlab/github instance. They should be similar to the following:
```
 git init
 git remote add origin git@<url>
 git add .
 git commit -m "Initial commit"
 git push -u origin master
```

### Step 5
Now you are ready to add the subtree of the CORE component.

### Step 6
Now you have to add the remote location. First we add the remote repo
```
git remote add core-subtree git@svs-rtp-web-git.cisco.com:SVS/webltr-core.git
```
Then we add the remote sub-tree
```
git subtree add --prefix=core/ core-subtree master
```
Now you are going to add this into **your origin**
```
git push origin master
```
What this will do is that it will push everything back to your new LAB repo, including the new subtree.

### Going forward and GIT

You have to do ALL the git commands from the root directory. You will commit all the changes as you would normally do. The difference now is that any changes you make in the ```/core``` subdirectory you will have to either git pull or git push using the subtree subcommands. Don't forget the branch and the prefix. The following examples might be helpfull. The branches are important.
```
git subtree push --prefix=core/ core-subtree master
git subtree pull --prefix=core/ core-subtree master
```


## The docker compose environment variable.
In the ```/core``` directory is a file called ```env.sample``` that is a file that contains variables that is read by docker-compose. These variables set the port number that **gunicorn** will use to host the app. You need to copy the env.sample into ```.env``` so that it is read by compose. The file is ignored by GIT so you have to set this up for every place you want to run and set the proper port number for location execution.

# Day to day workflow
Now that you have the repository and everything setup, the first thing is going to be to start the internal micro-services containers. You will do this from the ```/core``` directory with:
```
docker-compose up
```
The first time this is going to pull and build the different containers into your machine. If you ever need to rebuild the containers you can just do the command:
```
docker-compose build
```
This will bring up various containers. The primary FLASK container and the two containers that watch over the scss files to compile them into regular CSS. SASS is a much better way to deal with CSS because it simplifies working with CSS inheritance. These containers watch the folder and compile into the CSS folder that you reference from the browser. If you don't wish to work with SASS then just don't place anything in the folders.

As you are working and making changes you should commit frequently back into the repo. The git commit command:
```
git commit -a -m "reason"
git push
```
If you add any files make sure to add them with the ```git add``` commmand.

# Templates
The whole structure of this application is that it uses Python and JINJA to create live documents. These documents
are written in HTML. Inside the HTML are Jinja template variables that make it possible to inject programmatically inside the HTML code specific values. These are read from the ```pod_data.py``` file.

For anything related to the lab, the templates will be located under the ```/lab/templates``` structure. These are unique to your lab. These templates **extend** one of the core templates. For a detailed understanding of how this works with flask you an read [Jinja with Flask](https://flask.palletsprojects.com) in the flask documentation. With the examples provided you should have sufficient ground to work with.

## IMG MAN
Part of the functionality that is provided in the framework is the IMGMAN code. This is a python code that uses [Pillow](https://pypi.org/project/Pillow/) to annotate images. The framework reads a CSV file with the data to process based on the request coming into the system to display an image. The primary purpose of this function is to manipulate images to give the students very concise documentation. For example a screen shot of an image from the GUI of an application can be appended with TEXT that is specific to that user like the IP address to use and other factors.
The python code reads the CSV file that is called ```imgdata.csv``` and is located under the ```/lab``` structure.

The structure of the CSV file is:
```
Index,TYPE,ACTION(POINT/TXT),ImageFilename,X,Y,TextRotation,FontSize,TextColor,BoxColor,BoxFill,Font,Align,Text
```
There is an example in the REPO. These images are invoked via a specific route in flask, processed and sent to the browser as a new image. The new part of this is the font files, as the path now needs to be more complete/accurate to accommodate the WOFF format. 



# Reference
* [ Git Subtrees Explanations](https://medium.com/@v/git-subtrees-a-tutorial-6ff568381844)
* [ Git Subtrees Explanations 2](https://lostechies.com/johnteague/2014/04/04/using-git-subtrees-to-split-a-repository/)
* [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Bootstrap File tree](https://www.jqueryscript.net/other/Nice-File-Tree-View-Plugin-with-jQuery-Bootstrap-File-Tree.html)

### CSS Related
* [ CSS Animation 1](https://codyhouse.co/gem/animated-intro-section)
* [ CSS Animation 2](https://webdesign.tutsplus.com/articles/quickly-build-a-swish-teaser-page-with-css3--webdesign-6532)
* [ CSS Animation 3](https://codepen.io/wifeo/pen/ukzLD)
* [ Animista Animation CSS Builder ](http://animista.net/)
* [ CSS Animation Snippets ](https://envato.com/blog/pure-css-animation-snippets/)
* [ CSS Slide in text animation](https://www.html.am/html-codes/marquees/css-slide-in-text.cfm)
* [CSS Gradient generator](https://www.colorzilla.com/gradient-editor/)
* [Color wheel for Cisco color - Indigo Blue](https://www.colorhexa.com/005073)
* [Color wheel for Cisco color - Vibrante Blue](https://www.colorhexa.com/017cad)
* [Color wheel for Cisco color - Cisco Blue](https://www.colorhexa.com/00bceb)
* [Color wheel for Cisco color - Status Blue](https://www.colorhexa.com/64bbe3)
* [Color wheel for Cisco color - Light Blue](https://www.colorhexa.com/f2fbfd)
* [Color wheel for Cisco color - Green](https://www.colorhexa.com/6ebe4a)
* [Color wheel for Cisco color - Orange](https://www.colorhexa.com/fbab18)
* [Color wheel for Cisco color - Red ](https://www.colorhexa.com/e2231a)



### Other
* [Great page on new WOFF Font capabilities](https://css-tricks.com/understanding-web-fonts-getting/)
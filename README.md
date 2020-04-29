# PLANitManual

- We use the entire repo's master branch for github pages (not just the docs dir) because
	the repo only contains the manual and no source
	

# HUGO

- We use Hugo as our static website creator. It allows us to write all our content
in markdown files in a separate repo. 

- We then run Hugo to create the HTML equivalents which are committed to this repo 

## Setting it up for development
- Installing HUGO (https://gohugo.io/getting-started/installing/)
-- We use the binary approach collected from  https://github.com/gohugoio/hugo/releases
-- currently we are utilising version 0.69.2   
-- make sure the contents of the binary are placed in a directory that is part of the system path (or add it)
-- verify it runs by running "hugo -version" on the command line. It should output some version info

### New site (not used typically as we build on the existing site, see next heading)
-- go to the repo that will host the new site contents. 
-- Note: this should not be the repository that hosts the compiled Hugo site but a different repo

- How to combine hugo and hosting on github using pages

https://gohugo.io/hosting-and-deployment/hosting-on-github/
This GitHub action triggers on a PR review update (comment, requested changes, approve changes).  

##Setup
#Step 1
Insert secrets in to Github secrets. The keys has to be as follows:
EMAIL_USERNAME, eg. name@server.com
EMAIL_PASSWORD, eg. passwordToEmail
EMAIL_DOMAIN, eg. smtp.gmail.com

#Step 2
copy the following into your workflow:
uses: isacarvid/python-action@v1
with: 
  filePath: ${{ steps.get-diff.outputs.files}}
  usernameSecret: ${{ secrets.EMAIL_USERNAME }}
  passwordSecret: ${{ secrets.EMAIL_PASSWORD }}
  domainSecret: ${{ secrets.EMAIL_DOMAIN }}
  keyword: '#notify'



This GitHub action triggers on a PR review update (comment, requested changes, approve changes).  

# Setup
### Pre-requisites
Add secrets to your repository's Github secrets. The keys are as follows:

EMAIL_USERNAME, eg. name@server.com

EMAIL_PASSWORD, eg. passwordToEmail

EMAIL_DOMAIN, eg. smtp.gmail.com

    
### Inputs

:heavy_exclamation_mark: = Required

<table>
  <thead>
    <tr>
      <th width="1%">&nbsp;</th>
      <th width="20%">Input</th>
      <th width="69%">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>:heavy_exclamation_mark:</td>
      <td>filePath</td>
      <td>Path to the readme. Where notification addresses are to be found. Computed by the steps in workflow.</td>
    </tr>
    <tr>
      <td>:heavy_exclamation_mark:</td>
      <td>usernameSecret</td>
      <td>The username to the Email to send notifications from. Fetched from secrets.</td>
    </tr>
    <tr>
      <td>:heavy_exclamation_mark:</td>
      <td>passwordSecret</td>
      <td>
        Password to email to send notification from. Fetched from secrets.
       </td>
    </tr>
    <tr>
      <td>:heavy_exclamation_mark:</td>
      <td>domainSecret</td>
      <td>smtp server to send email from. Eg. smtp.gmail.com</td>
    </tr>
    <tr>
      <td>:heavy_exclamation_mark:</td>
      <td>keyword</td>
      <td>
       Keyword to be included in a PR-readme if notification is to be enabled.
      </td>
    </tr>
  </tbody>
</table>
          
### Example workflow
```yaml
name: someName
on:
  pull_request_review:
    types: [edited, dismissed, submitted]
  
jobs:
  Notifier:
    name: someName
    runs-on: ubuntu-latest
    steps:
      - name: Set up Python 3.7
        uses: actions/setup-python@v2
        with:
          python-version: "3.7"
      - name: Checkout
        uses: actions/checkout@v2
      - name: Get README.md
        run: |
          git fetch --quiet
          diffFiles=$(git diff origin/master HEAD --name-only)
          diffFiles="${diffFiles//'%'/'%25'}"
          diffFiles="${diffFiles//$'\n'/'%0A'}"
          diffFiles="${diffFiles//$'\r'/'%0D'}"
          echo "::set-output name=files::$diffFiles"
        id: get-diff
      - name: run python
        uses: isacarvid/ isacarvid/PR-review-notification@v1.2
        with:
          filePath: ${{ steps.get-diff.outputs.files}}
          usernameSecret: ${{ secrets.EMAIL_USERNAME }}
          passwordSecret: ${{ secrets.EMAIL_PASSWORD }}
          domainSecret: ${{ secrets.EMAIL_DOMAIN }}
          keyword: '#notify'


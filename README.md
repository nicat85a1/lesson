# fatal: Authentication failed

## option 1:

[get_browser] (https://github.com/settings/tokens/new)

## Expiration 1 Year

## Select scopes All

## Generate token

`git remote set-url origin https://TOKEN@github.com/username/repositories`

`git push origin main`

## or option 2:

### download:

[gcm_linux_download_link] (https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.4.1/gcm-linux_amd64.2.4.1.deb)

### open project on terminal:
### root yetkisi: `sudo su`
`dpkg -i <gcm-linux_amd64.2.4.1.deb>`
`git-credential-manager configure`

`git config --global credential.credentialStore secretservice` or `git config --global credential.credentialStore gpg`

`gpg --gen-key`

`git config --global credential.credentialStore plaintext`

### done.

-----------------------------------------------------------

open project on terminal

`sudo su`

`git add .`

`git status`

`git commit -m "fatal password control"`

`git push -u origin main`

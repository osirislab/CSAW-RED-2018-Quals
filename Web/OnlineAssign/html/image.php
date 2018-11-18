<?php

if (!isset($_GET['path'])) {
    die("'path' param required");
}

$full_path = realpath(dirname(__FILE__) . '/' . $_GET['path']);

if ($full_path === false) {
    die("No such image");
}

$script_path = realpath(dirname(__FILE__));

if (substr($full_path, 0, strlen($script_path)) !== $script_path) {
    die("Solve the challenge the right way :P");
}

header('Content-Type: image/jpg');
echo file_get_contents($full_path);
